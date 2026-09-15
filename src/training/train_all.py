from __future__ import annotations

import json
import time
from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import StratifiedKFold, cross_val_score

from src.config import RANDOM_STATE
from src.data.dataset import load_training_data
from src.training.pipeline import build_model_pipeline
from src.training.split import create_train_test_split
from src.training.config import (
    get_dataset_config,
    get_model_output_dir,
    get_result_output_dir,
)


def evaluate_predictions(model, x_test, y_test):
    predictions = model.predict(x_test)

    probabilities = None
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(x_test)[:, 1]

    metrics = {
        "accuracy": float(accuracy_score(y_test, predictions)),
        "precision": float(
            precision_score(y_test, predictions, zero_division=0)
        ),
        "recall": float(
            recall_score(y_test, predictions, zero_division=0)
        ),
        "f1": float(
            f1_score(y_test, predictions, zero_division=0)
        ),
    }

    if probabilities is not None:
        metrics["roc_auc"] = float(
            roc_auc_score(y_test, probabilities)
        )
    else:
        metrics["roc_auc"] = None

    tn, fp, fn, tp = confusion_matrix(
        y_test,
        predictions,
        labels=[0, 1],
    ).ravel()

    metrics["true_negative"] = int(tn)
    metrics["false_positive"] = int(fp)
    metrics["false_negative"] = int(fn)
    metrics["true_positive"] = int(tp)

    return metrics


def train_single_model(
    disease: str,
    model_name: str,
    test_size: float = 0.20,
):
    features, target = load_training_data(disease)

    x_train, x_test, y_train, y_test = create_train_test_split(
        features,
        target,
        test_size=test_size,
    )

    model = build_model_pipeline(
        x_train,
        model_name,
    )

    start_time = time.perf_counter()

    model.fit(x_train, y_train)

    training_seconds = time.perf_counter() - start_time

    test_metrics = evaluate_predictions(
        model,
        x_test,
        y_test,
    )

    cv = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=RANDOM_STATE,
    )

    cv_scores = cross_val_score(
        model,
        x_train,
        y_train,
        cv=cv,
        scoring="roc_auc",
        n_jobs=1,
    )

    model_dir = get_model_output_dir(disease)
    model_dir.mkdir(parents=True, exist_ok=True)

    model_path = model_dir / f"{model_name}.joblib"

    joblib.dump(model, model_path)

    config = get_dataset_config(disease)

    return {
        "disease": disease,
        "model": model_name,
        "dataset_rows": int(len(features)),
        "feature_count": int(features.shape[1]),
        "train_rows": int(len(x_train)),
        "test_rows": int(len(x_test)),
        "training_seconds": round(training_seconds, 4),
        "cv_roc_auc_mean": float(cv_scores.mean()),
        "cv_roc_auc_std": float(cv_scores.std()),
        "test_metrics": test_metrics,
        "model_path": str(model_path),
        "target": config["target"],
    }


def train_all_models():
    diseases = [
        "diabetes",
        "heart",
        "ckd",
        "breast_cancer",
    ]

    model_names = [
        "logistic_regression",
        "decision_tree",
        "random_forest",
        "svm",
        "knn",
        "xgboost",
    ]

    results = []

    total_experiments = len(diseases) * len(model_names)

    print("=" * 70)
    print("REAL MULTI-DISEASE TRAINING")
    print(f"Experiments: {total_experiments}")
    print("=" * 70)

    experiment_number = 0

    for disease in diseases:
        print(f"\n{'=' * 70}")
        print(f"DISEASE: {disease}")
        print(f"{'=' * 70}")

        for model_name in model_names:
            experiment_number += 1

            print(
                f"\n[{experiment_number}/{total_experiments}] "
                f"{disease} -> {model_name}"
            )

            result = train_single_model(
                disease,
                model_name,
            )

            results.append(result)

            metrics = result["test_metrics"]

            print(
                f"Accuracy={metrics['accuracy']:.4f} | "
                f"Precision={metrics['precision']:.4f} | "
                f"Recall={metrics['recall']:.4f} | "
                f"F1={metrics['f1']:.4f} | "
                f"ROC-AUC={metrics['roc_auc']:.4f}"
            )

            print(
                f"CV ROC-AUC={result['cv_roc_auc_mean']:.4f} "
                f"+/- {result['cv_roc_auc_std']:.4f}"
            )

            print(
                f"Saved: {result['model_path']}"
            )

    results_dir = get_result_output_dir()
    results_dir.mkdir(parents=True, exist_ok=True)

    json_path = results_dir / "model_training_results.json"

    with json_path.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            results,
            file,
            indent=2,
        )

    rows = []

    for result in results:
        metrics = result["test_metrics"]

        rows.append(
            {
                "disease": result["disease"],
                "model": result["model"],
                "dataset_rows": result["dataset_rows"],
                "feature_count": result["feature_count"],
                "train_rows": result["train_rows"],
                "test_rows": result["test_rows"],
                "training_seconds": result["training_seconds"],
                "cv_roc_auc_mean": result["cv_roc_auc_mean"],
                "cv_roc_auc_std": result["cv_roc_auc_std"],
                "accuracy": metrics["accuracy"],
                "precision": metrics["precision"],
                "recall": metrics["recall"],
                "f1": metrics["f1"],
                "roc_auc": metrics["roc_auc"],
                "true_negative": metrics["true_negative"],
                "false_positive": metrics["false_positive"],
                "false_negative": metrics["false_negative"],
                "true_positive": metrics["true_positive"],
                "model_path": result["model_path"],
            }
        )

    dataframe = pd.DataFrame(rows)

    csv_path = results_dir / "model_comparison.csv"

    dataframe.to_csv(
        csv_path,
        index=False,
    )

    best_models = {}

    for disease in diseases:
        disease_results = dataframe[
            dataframe["disease"] == disease
        ].copy()

        disease_results = disease_results.sort_values(
            by=[
                "cv_roc_auc_mean",
                "f1",
                "recall",
            ],
            ascending=False,
        )

        best = disease_results.iloc[0]

        best_models[disease] = {
            "model": best["model"],
            "cv_roc_auc_mean": float(
                best["cv_roc_auc_mean"]
            ),
            "test_accuracy": float(
                best["accuracy"]
            ),
            "test_precision": float(
                best["precision"]
            ),
            "test_recall": float(
                best["recall"]
            ),
            "test_f1": float(
                best["f1"]
            ),
            "test_roc_auc": float(
                best["roc_auc"]
            ),
            "model_path": best["model_path"],
        }

    best_path = results_dir / "best_models.json"

    with best_path.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            best_models,
            file,
            indent=2,
        )

    print("\n" + "=" * 70)
    print("TRAINING COMPLETE")
    print("=" * 70)

    print("\nBEST MODEL PER DISEASE:")

    for disease, best in best_models.items():
        print(
            f"{disease:15} -> "
            f"{best['model']:20} "
            f"CV ROC-AUC={best['cv_roc_auc_mean']:.4f} | "
            f"Test ROC-AUC={best['test_roc_auc']:.4f}"
        )

    print("\nRESULT FILES:")
    print(json_path)
    print(csv_path)
    print(best_path)

    return results


if __name__ == "__main__":
    train_all_models()
