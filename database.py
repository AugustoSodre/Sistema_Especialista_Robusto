import sqlite3
import json
from datetime import datetime

DB_NAME = "eye_expert_system.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS diagnoses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            symptoms TEXT,
            result TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_diagnosis(symptoms, result):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO diagnoses (timestamp, symptoms, result)
        VALUES (?, ?, ?)
    ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), json.dumps(symptoms), result))
    conn.commit()
    conn.close()