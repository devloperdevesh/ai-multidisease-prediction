from pathlib import Path
import json

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
RESULTS_DIR = PROJECT_ROOT / "reports" / "results"

DATASETS = {
    "diabetes": {
        "file": "pima_diabetes.csv",
        "target": "Outcome",
    },
    "heart": {
        "file": "uci_heart_disease.csv",
        "target": "num",
    },
    "ckd": {
        "file": "uci_chronic_kidney_disease.csv",
        "target": "class",
    },
    "breast_cancer": {
        "file": "uci_breast_cancer_diagnostic.csv",
        "target": "Diagnosis",
    },
}


def clean_column_name(value):
    return str(value).strip()


def audit_dataset(disease, config):

    path = RAW_DATA_DIR / disease / config["file"]

    print("\n" + "=" * 70)
    print(f"{disease.upper()} DATASET")
    print("=" * 70)

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    dataframe = pd.read_csv(path)

    dataframe.columns = [
        clean_column_name(column)
        for column in dataframe.columns
    ]

    print(f"File       : {path.name}")
    print(f"Shape      : {dataframe.shape}")
    print(f"Rows       : {len(dataframe)}")
    print(f"Columns    : {len(dataframe.columns)}")
    print(f"Target     : {config['target']}")

    print("\n--- COLUMNS ---")
    for index, column in enumerate(dataframe.columns, start=1):
        print(f"{index:>3}. {column}")

    print("\n--- DATA TYPES ---")
    print(dataframe.dtypes.to_string())

    print("\n--- MISSING VALUES ---")

    missing = dataframe.isna().sum()
    missing = missing[missing > 0]

    if missing.empty:
        print("No pandas NaN values found.")
    else:
        print(missing.to_string())

    print("\n--- BLANK / '?' VALUES ---")

    suspicious = {}

    for column in dataframe.select_dtypes(
        include=["object", "string"]
    ).columns:

        series = dataframe[column].astype("string")

        blank_count = int(
            series.str.strip().eq("").sum()
        )

        question_count = int(
            series.str.strip().eq("?").sum()
        )

        if blank_count or question_count:
            suspicious[column] = {
                "blank": blank_count,
                "question_mark": question_count,
            }

    if not suspicious:
        print("No blank or '?' values found.")
    else:
        for column, values in suspicious.items():
            print(
                f"{column}: "
                f"blank={values['blank']}, "
                f"?={values['question_mark']}"
            )

    print("\n--- DUPLICATES ---")

    duplicate_count = int(
        dataframe.duplicated().sum()
    )

    print(f"Duplicate rows: {duplicate_count}")

    print("\n--- NUMERIC COLUMNS ---")

    numeric_columns = dataframe.select_dtypes(
        include=["number"]
    ).columns.tolist()

    print(numeric_columns)

    print("\n--- CATEGORICAL / TEXT COLUMNS ---")

    categorical_columns = dataframe.select_dtypes(
        exclude=["number"]
    ).columns.tolist()

    print(categorical_columns)

    print("\n--- TARGET ANALYSIS ---")

    target = config["target"]

    if target not in dataframe.columns:
        print(
            f"WARNING: target '{target}' was not found."
        )
        target_distribution = {}
    else:
        target_values = dataframe[target].astype("string").str.strip()

        target_distribution = {
            str(key): int(value)
            for key, value in target_values.value_counts(
                dropna=False
            ).items()
        }

        print(
            target_values.value_counts(
                dropna=False
            ).to_string()
        )

    print("\n--- NUMERIC SUMMARY ---")

    if numeric_columns:
        print(
            dataframe[numeric_columns]
            .describe()
            .round(3)
            .to_string()
        )
    else:
        print("No numeric columns.")

    report = {
        "disease": disease,
        "file": str(path.relative_to(PROJECT_ROOT)),
        "rows": int(dataframe.shape[0]),
        "columns": int(dataframe.shape[1]),
        "column_names": dataframe.columns.tolist(),
        "target": target,
        "target_found": target in dataframe.columns,
        "dtypes": {
            column: str(dtype)
            for column, dtype in dataframe.dtypes.items()
        },
        "missing_values": {
            str(column): int(value)
            for column, value in dataframe.isna().sum().items()
            if value > 0
        },
        "suspicious_values": suspicious,
        "duplicate_rows": duplicate_count,
        "numeric_columns": numeric_columns,
        "categorical_columns": categorical_columns,
        "target_distribution": target_distribution,
    }

    return report


def main():

    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    all_reports = {}

    print("\nRESEARCH DATASET AUDIT STARTED")

    for disease, config in DATASETS.items():

        report = audit_dataset(
            disease,
            config
        )

        all_reports[disease] = report

    json_path = RESULTS_DIR / "dataset_audit.json"

    with open(
        json_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            all_reports,
            file,
            indent=2,
            ensure_ascii=False
        )

    markdown_path = RESULTS_DIR / "dataset_audit.md"

    with open(
        markdown_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write("# Multi-Disease Dataset Audit\n\n")
        file.write(
            "Automated structural audit of the four raw datasets "
            "before preprocessing and model training.\n\n"
        )

        for disease, report in all_reports.items():

            file.write(f"## {disease.replace('_', ' ').title()}\n\n")

            file.write(
                f"- Rows: {report['rows']}\n"
            )
            file.write(
                f"- Columns: {report['columns']}\n"
            )
            file.write(
                f"- Target: `{report['target']}`\n"
            )
            file.write(
                f"- Target found: {report['target_found']}\n"
            )
            file.write(
                f"- Duplicate rows: {report['duplicate_rows']}\n\n"
            )

            file.write("### Columns\n\n")

            for column in report["column_names"]:
                file.write(f"- `{column}`\n")

            file.write("\n### Missing Values\n\n")

            if report["missing_values"]:
                for column, count in report["missing_values"].items():
                    file.write(
                        f"- `{column}`: {count}\n"
                    )
            else:
                file.write("- None detected by pandas.\n")

            file.write("\n### Suspicious Values\n\n")

            if report["suspicious_values"]:
                for column, values in report["suspicious_values"].items():
                    file.write(
                        f"- `{column}`: "
                        f"blank={values['blank']}, "
                        f"?={values['question_mark']}\n"
                    )
            else:
                file.write("- None detected.\n")

            file.write("\n### Target Distribution\n\n")

            if report["target_distribution"]:
                for value, count in report["target_distribution"].items():
                    file.write(
                        f"- `{value}`: {count}\n"
                    )
            else:
                file.write("- Target analysis unavailable.\n")

            file.write("\n")

    print("\n" + "=" * 70)
    print("DATASET AUDIT COMPLETE")
    print("=" * 70)

    print(f"\nJSON report : {json_path}")
    print(f"MD report   : {markdown_path}")


if __name__ == "__main__":
    main()
