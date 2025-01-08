from srcs.fetch_resources_all import fetch_resources_for_accounts


def main():
    config_file = "config/config.json"  # Path to your configuration file
    fetch_resources_for_accounts(config_file)

if __name__ == "__main__":
    main()

