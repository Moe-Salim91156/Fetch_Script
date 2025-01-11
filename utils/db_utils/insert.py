import sqlite3
from utils.helper_utils.display_logs import log_message

def insert_resources_into_db(resources, db_path="output_files/resources.db"):
    """
    Inserts a list of resources into the SQLite database.

    Args:
        resources (list): A list of resource dictionaries to be inserted.
        db_path (str): Path to the SQLite database file.
        logger (function): Optional logger function for status messages.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        for resource in resources:
            metadata_str = "\n".join([f"{key}: {value}" for key, value in resource["metadata"].items()])

            cursor.execute("""
            INSERT INTO resources (account_name, region, resource_type, resource_id, metadata)
            VALUES (?, ?, ?, ?, ?)
            """, (
                resource.get("account"),
                resource.get("region"),
                resource.get("resource_type"),
                resource.get("resource_id"),
                metadata_str
            ))

        conn.commit()

    except sqlite3.Error as e:
        if logger:
            log_message(f"Database error: {e}","ERROR")
    except Exception as e:
            log_message(f"Unexpected error: {e}","ERROR")
    finally:
        conn.close()

