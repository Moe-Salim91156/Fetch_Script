import sqlite3

def initialize_db(db_name="resources.db"):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Create tables for each resource type
        cursor.execute('''CREATE TABLE IF NOT EXISTS ec2_instance (
                            resource_id TEXT PRIMARY KEY,
                            account TEXT,
                            region TEXT,
                            instance_type TEXT,
                            state TEXT,
                            public_ip TEXT,
                            tags TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS rds_instance (
                            resource_id TEXT PRIMARY KEY,
                            account TEXT,
                            region TEXT,
                            engine TEXT,
                            status TEXT,
                            endpoint TEXT,
                            tags TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS s3_bucket (
                            resource_id TEXT PRIMARY KEY,
                            account TEXT,
                            region TEXT,
                            creation_date TEXT,
                            tags TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS iam_role (
                            resource_id TEXT PRIMARY KEY,
                            account TEXT,
                            role_id TEXT,
                            arn TEXT,
                            create_date TEXT,
                            tags TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS subnet (
                            resource_id TEXT PRIMARY KEY,
                            account TEXT,
                            region TEXT,
                            cidr_block TEXT,
                            availability_zone TEXT,
                            vpc_id TEXT,
                            tags TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS ebs_volume (
                            resource_id TEXT PRIMARY KEY,
                            account TEXT,
                            region TEXT,
                            size INTEGER,
                            state TEXT,
                            volume_type TEXT,
                            tags TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS network_acl (
                            resource_id TEXT PRIMARY KEY,
                            account TEXT,
                            region TEXT,
                            vpc_id TEXT,
                            tags TEXT)''')

        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")

