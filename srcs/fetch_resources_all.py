import os
import json
import boto3

from fetchers.fetch_vpcs import fetch_vpcs
from fetchers.fetch_Ec2 import fetch_ec2_instances
from fetchers.fetch_security_groups import fetch_security_groups
from fetchers.fetch_EBS_Volumes import fetch_ebs
from fetchers.fetch_subnets import fetch_subnets
from fetchers.fetch_acls import fetch_acls
from fetchers.fetch_rds import fetch_rds_instances
from fetchers.fetch_S3_Buckets import fetch_S3_Buckets
from fetchers.fetch_iam_roles import fetch_iam_roles

from utils.create_session import create_aws_session
from utils.display_results import display_resources
from utils.get_regions import get_user_input_regions
from utils.get_regions import get_all_regions
from utils.read_config_file import read_config_file
from utils.logging import log_message
from utils.write_to_output_file import write_to_file

def fetch_resources_for_accounts(config):
    all_resources = []
    for account in config.get('accounts', []):
        profile_name = account.get('profile_name')
        if not profile_name:
            log_message(f"Skipping account: Missing 'profile_name'")
            continue

        session = create_aws_session(profile_name)
        if not session:
            log_message(f"Failed to create session for profile: {profile_name}")
            continue

        account_name = account.get('account_name')
        if not account_name:
            log_message(f"Skipping account: Missing 'account_name'")
            continue

        regions = account.get('regions') or get_user_input_regions(account_name)

        for region in regions:
            log_message(f"Fetching resources for account '{account_name}' in region '{region}'")
            resources = []
            resources.extend(fetch_vpcs(session, region, account_name))
            resources.extend(fetch_ec2_instances(session, region, account_name))
            resources.extend(fetch_rds_instances(session, region, account_name))
            resources.extend(fetch_S3_Buckets(session, region, account_name))
            resources.extend(fetch_iam_roles(session, region, account_name))
            resources.extend(fetch_security_groups(session, region, account_name))
            resources.extend(fetch_ebs(session, region, account_name))
            resources.extend(fetch_subnets(session, region, account_name))
            resources.extend(fetch_acls(session, region, account_name))
            all_resources.extend(resources)
            log_message(f"Completed fetching resources for account '{account_name}' in region '{region}'")

    output_file = os.path.join(os.getcwd(), "output.txt")
    write_to_file(all_resources, output_file)
    log_message(f"All resources written to {output_file}")
    print("logs has been saved in log.txt")

