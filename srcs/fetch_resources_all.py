import json
import boto3
from fetchers.fetch_vpcs import fetch_vpcs
from fetchers.fetch_Ec2 import fetch_ec2_instances
from fetchers.fetch_security_groups import fetch_security_groups

from utils.create_session import create_aws_session
from utils.display_results import display_results
from utils.get_regions import get_user_input_regions
from utils.get_regions import get_all_regions
from utils.read_config_file import read_config_file

def fetch_resources_for_accounts(config_file):
    config = read_config_file(config_file)
    for account in config['accounts']:
        account_name = account['name']
        profile_name = account['profile']
        regions = account.get('regions')

        session = create_aws_session(profile_name)
        if not session:
            print(f"Failed to create session for {account_name}. Skipping account.")
            continue

        # Prompt user if regions are not specified in config
        if not regions:
            regions = get_user_input_regions(account_name)

        for region in regions:
            print(f"\nFetching resources for {account_name} in {region}...")

            # Fetch and display VPCs
            vpcs = fetch_vpcs(session, region)
            display_results("VPCs", vpcs, account_name, region)
            
            # Fetch and display EC2 instances
            ec2_instances = fetch_ec2_instances(session, region)
            display_results("EC2 Instances", ec2_instances, account_name, region)

            sgs = fetch_security_groups(session,region)
            display_results("security groups", sgs,account_name,region)
            # Add other resource fetching here

if __name__ == "__main__":
    fetch_resources_for_accounts('config.json')
