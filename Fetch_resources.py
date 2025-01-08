import boto3
import json

# Function to create a session for an AWS account using a specific profile
def create_aws_session(profile_name):
    try:
        session = boto3.Session(profile_name=profile_name)
        print(f"Session created for profile: {profile_name}")
        return (session)
    except Exception as e:
        print(f"Error creating session for profile {profile_name}: {str(e)}")
        return None

# Function to read the configuration file containing AWS account details
def read_config_file(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return (config)

# Function to get all available AWS regions
def get_all_regions():
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_regions()
    return [region['RegionName'] for region in response['Regions']]

# Function to fetch security groups for a given region
def fetch_security_groups(session, region):
    try:
        ec2_client = session.client('ec2', region_name=region)
        response = ec2_client.describe_security_groups()
        return response['SecurityGroups']
    except Exception as e:
        print(f"Error fetching security groups in {region}: {str(e)}")
        return []

# Function to display security groups in a formatted manner
def display_security_groups(security_groups, account_name, region):
    print(f"\n{'='*50}")
    print(f"Security Groups for {account_name} in region {region}:")
    if not security_groups:
        print("  No security groups found.")
    else:
        for sg in security_groups:
            print(f"  ID: {sg['GroupId']}, Name: {sg['GroupName']}")
            print(f"    VPC: {sg['VpcId']}")
            print(f"    Description: {sg.get('Description', 'No description')}")
    print(f"{'='*50}\n")

# Function to get user input for regions
def get_user_input_regions():
    user_input = input("Enter the regions to fetch data for (comma-separated), or press Enter to use all regions: ")
    if user_input:
        # User provided regions, split by comma and strip extra spaces
        regions = [region.strip() for region in user_input.split(",")]
    else:
        # Use all available regions if no input is provided
        print("No regions provided, fetching data from all regions...")
        regions = get_all_regions()
    return regions

# Function to fetch resources for the accounts listed in the config file
def fetch_resources_for_accounts(config_file):
    config = read_config_file(config_file)

    # Iterate through each account in the configuration file
    for account in config['accounts']:
        account_name = account['name']
        profile_name = account['profile']
        regions = account.get('regions', [])  # Fetch the regions if provided

        # Create AWS session for the current account
        session = create_aws_session(profile_name)

        if session:
            # If no regions are specified in the config file, ask the user for input
            if not regions:
                print(f"No regions specified for {account_name}. Let's get your input...")
                regions = get_user_input_regions()

            # Fetch resources (e.g., Security Groups) for each region in the current account
            for region in regions:
                print(f"Fetching security groups for {account_name} in region {region}...")
                security_groups = fetch_security_groups(session, region)
                display_security_groups(security_groups, account_name, region)
        else:
            print(f"Skipping {account_name} due to session creation failure.")

# Entry point to execute the script
if __name__ == "__main__":
    config_file = 'config.json'  # Path to the configuration file
    fetch_resources_for_accounts(config_file)

