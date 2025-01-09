import sqlite3
import os

def initialize_db(db_path="output_files/resources.db"):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Connect to SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resources (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_name TEXT,
        region TEXT,
        resource_type TEXT,
        resource_id TEXT,
        metadata TEXT
    )
    """)
    
    conn.commit()
    conn.close()

