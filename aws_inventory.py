import json
from srcs.fetch_resources_all import fetch_resources_for_accounts
from utils.helper_utils.display_logs import log_message

def main():
    config_file = 'config/config.json'
    try:
        with open(config_file, "r") as file:
            config = json.load(file)
    except FileNotFoundError:
        log_message(f"Error: '{config_file}' not found. Please provide a valid configuration file.")
        return
    except json.JSONDecodeError:
        log_message(f"Error: '{config_file}' contains invalid JSON. Please fix the file and try again.")
        return

    log_message("Starting resource fetching process...")
    fetch_resources_for_accounts(config)
    log_message("Resource fetching process completed successfully.")

if __name__ == "__main__":
    main()

