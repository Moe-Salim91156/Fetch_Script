import json
import os
from srcs.fetch_resources_all import fetch_resources_for_accounts
from utils.helper_utils.display_logs import log_message
from utils.db_utils.init import initialize_db
from utils.db_utils.insert import insert_resources_into_db

def main():
    config_file = 'config/config.json'
    try:
        # Load the configuration file
        with open(config_file, "r") as file:
            config = json.load(file)
    except FileNotFoundError:
        log_message(f"Error: ({config_file}) not found. Please provide a valid configuration file.", "ERROR")
        return
    except json.JSONDecodeError:
        log_message(f"Error: ({config_file}) contains invalid JSON. Please fix the file and try again.", "ERROR")
        return

    try:
        log_message("Starting resource fetching process...")
        initialize_db()

        # Attempt to fetch resources
        success = fetch_resources_for_accounts(config)
        if not success:
            log_message("Error: Resource fetching failed. Exiting the script.", "ERROR")
            return
        log_message("Resource fetching process completed successfully.")
        log_message(f"Output has been inserted in output_files/output.txt", "HINTS")
        log_message(f"Resources successfully inserted into output_files/resources.db")
    except Exception as e:
        log_message(f"Error: An unexpected error occurred during the resource fetching process. Details: {e}", "ERROR")

if __name__ == "__main__":
    main()

