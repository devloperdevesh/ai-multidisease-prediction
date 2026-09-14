from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier


def get_models():
    """
    Return all candidate classification models.

    The models are intentionally kept in one place so that
    every disease can be evaluated using the same model set.
    """

    return {
        "logistic_regression": LogisticRegression(
            max_iter=2000,
            random_state=42
        ),

        "decision_tree": DecisionTreeClassifier(
            random_state=42
        ),

        "random_forest": RandomForestClassifier(
            n_estimators=300,
            random_state=42,
            n_jobs=-1
        ),

        "svm": SVC(
            probability=True,
            random_state=42
        ),

        "knn": KNeighborsClassifier(
            n_neighbors=5
        ),

        "xgboost": XGBClassifier(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=5,
            random_state=42,
            eval_metric="logloss"
        ),
    }
