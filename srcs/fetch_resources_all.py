import os
import json
import boto3
from colorama import Fore, Style, init

from fetchers.fetch_vpcs import fetch_vpcs
from fetchers.fetch_Ec2 import fetch_ec2_instances
from fetchers.fetch_security_groups import fetch_security_groups
from fetchers.fetch_EBS_Volumes import fetch_ebs
from fetchers.fetch_subnets import fetch_subnets
from fetchers.fetch_acls import fetch_acls
from fetchers.fetch_rds import fetch_rds_instances
from fetchers.fetch_S3_Buckets import fetch_S3_Buckets
from fetchers.fetch_iam_roles import fetch_iam_roles

from utils.helper_utils.create_session import create_aws_session
#from utils.helper_utils.display_results import display_resources,calculate_resource_summary,display_account_summary
from utils.helper_utils.display_results import write_to_terminal
from utils.helper_utils.get_regions import get_user_input_regions
from utils.helper_utils.get_regions import get_all_regions
from utils.helper_utils.read_config_file import read_config_file
from utils.helper_utils.display_logs import log_message
from utils.helper_utils.write_to_output_file import write_to_file

from utils.db_utils.init import initialize_db
from utils.db_utils.insert import insert_resources_into_db
from utils.db_utils.display import display_resources_table

def fetch_resources_for_accounts(config, db_path="output_files/resources.db"):
    "fetch all resources form accounts and displays them, also cheks for erros"

    write_to_file([], "w")
    with open("output_files/log.txt", "w") as log_file_handle:
        log_file_handle.truncate(0)

    all_resources = []
    overall_success = True  # flag to Track overall success

    for account in config.get('accounts', []):
        profile_name = account.get('profile_name')
        if not profile_name:
            log_message(f"Skipping account: Missing 'profile_name'", "WARNING")
            overall_success = False
            continue

        session = create_aws_session(profile_name)
        if not session:
            log_message(f"Failed to create session for profile: {profile_name}", "ERROR")
            overall_success = False
            continue

        account_name = account.get('account_name')
        if not account_name:
            log_message(f"Skipping account: Missing 'account_name'", "WARNING")
            overall_success = False
            continue

        regions = account.get('regions') or get_user_input_regions(account_name)

        for region in regions:
            try:
                log_message(f"Fetching resources for account {Style.BRIGHT}({account_name}) in region ({region})")
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
                log_message(f"Completed fetching resources for account {Style.BRIGHT}({account_name}){Style.RESET_ALL} in region ({region})")
                write_to_file(resources, "a")
                write_to_terminal(resources)
                all_resources.extend(resources)
            except Exception as e:
                log_message(f"Error fetching resources for account {account_name} in region {region}. Details: {e}", "ERROR")
                overall_success = False

    if all_resources:
        insert_resources_into_db(all_resources, db_path)
    else:
        log_message("No resources fetched to insert into the database.", "WARNING")

    return overall_success

