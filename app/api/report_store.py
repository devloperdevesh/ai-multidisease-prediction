from pathlib import Path
import sqlite3
import json
from datetime import datetime, timezone
from uuid import uuid4

DB_PATH = Path(__file__).resolve().parents[2] / "instance" / "medipredict.sqlite3"

def connect():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection

def initialize():
    with connect() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS prediction_reports (
                id TEXT PRIMARY KEY,
                disease TEXT NOT NULL,
                model TEXT NOT NULL,
                prediction INTEGER NOT NULL,
                risk_percentage REAL,
                risk_level TEXT,
                created_at TEXT NOT NULL
            )
        """)

def save_report(payload):
    allowed = {"diabetes", "heart", "ckd", "breast_cancer"}
    disease = payload.get("disease")
    if disease not in allowed:
        raise ValueError("Unsupported disease.")
    if payload.get("prediction") not in (0, 1):
        raise ValueError("Prediction must be 0 or 1.")
    risk = payload.get("risk_percentage")
    if risk is not None:
        risk = float(risk)
        if not 0 <= risk <= 100:
            raise ValueError("Risk percentage must be between 0 and 100.")
    report = {
        "id": str(uuid4()),
        "disease": disease,
        "model": str(payload.get("model", ""))[:100],
        "prediction": int(payload["prediction"]),
        "risk_percentage": risk,
        "risk_level": str(payload.get("risk_level", "unknown"))[:20],
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    if not report["model"]:
        raise ValueError("Model is required.")
    with connect() as db:
        db.execute("""
            INSERT INTO prediction_reports
            (id,disease,model,prediction,risk_percentage,risk_level,created_at)
            VALUES (:id,:disease,:model,:prediction,:risk_percentage,:risk_level,:created_at)
        """, report)
    return report

def list_reports():
    with connect() as db:
        rows = db.execute(
            "SELECT * FROM prediction_reports ORDER BY created_at DESC"
        ).fetchall()
    return [dict(row) for row in rows]

def delete_report(report_id):
    with connect() as db:
        cursor = db.execute("DELETE FROM prediction_reports WHERE id = ?", (report_id,))
        return cursor.rowcount > 0
