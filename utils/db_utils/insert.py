import sqlite3

def insert_resources_into_db(resources, db_path="output_files/resources.db"):
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
    conn.close()

    print(f"Resources successfully inserted into {db_path}")

