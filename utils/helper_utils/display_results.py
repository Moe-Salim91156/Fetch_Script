import boto3

from collections import Counter
from colorama import Fore, Style, init
from utils.helper_utils.write_to_output_file import update_resource_summary

from colorama import Fore

def write_resource_details_to_terminal(resource):
    """Display details for a single resource in the terminal."""
    print(f"{Fore.LIGHTGREEN_EX}Resource Type: {Fore.RESET}{Style.BRIGHT}{Fore.YELLOW}{resource['resource_type']}")
    print(f"{Fore.LIGHTGREEN_EX}Resource ID: {Fore.RESET}{Fore.WHITE}{resource['resource_id']}")
    print(f"{Fore.LIGHTGREEN_EX}Metadata:{Fore.RESET}")
    for key, value in resource['metadata'].items():
        print(f"    {Fore.CYAN}{key}: {Fore.WHITE}{value}")
    print(f"{Fore.LIGHTWHITE_EX}{'-' * 40}\n")

def write_resource_summary_to_terminal(resource_summary):
    """Display the summary of resource counts in the terminal."""
    print(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}--- Resource Summary ---{Style.RESET_ALL}")
    print(f"{'Resource Type':<20}{'Count':<10}")
    print(f"{Fore.LIGHTWHITE_EX}{'-' * 40}{Style.RESET_ALL}")  # Grey divider
    for resource_type, count in resource_summary.items():
        print(f"{Fore.LIGHTBLUE_EX}{resource_type:<20}{Fore.LIGHTYELLOW_EX}{count:<10}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{'-' * 40}{Style.RESET_ALL}")  # Grey divider

def update_region_summary(region_summary, resource_type):
    """Update resource count summary for the region."""
    resource_type_map = {
        "vpc": "VPC",
        "iam_role": "IAM Roles",
        "security_group": "Security Groups",
        "subnet": "Subnets",
        "network_acl": "Network ACLs",
        "ec2_instance": "EC2 Instances",
        "rds_database": "RDS Databases",
        "s3_bucket": "S3 Buckets",
        "ebs_volume": "EBS Volumes"
    }

    resource_type = resource_type.lower()  # Ensure matching case
    if resource_type in resource_type_map:
        mapped_type = resource_type_map[resource_type]
        if mapped_type in region_summary:
            region_summary[mapped_type] += 1
        else:
            region_summary[mapped_type] = 1
    else:
        print(f"{Fore.RED}Unknown resource type: {resource_type}")

    return region_summary

def write_to_terminal(resources):
    """Display resource details and summaries in the terminal."""
    resource_summary = {
        'VPC': 0,
        'EC2 Instances': 0,
        'RDS Databases': 0,
        'S3 Buckets': 0,
        'Security Groups': 0,
        'IAM Roles': 0,
        'Subnets': 0,
        'EBS Volumes': 0,
        'Network ACLs': 0
    }

    region_summary = {}
    current_account = None
    current_region = None

    for resource in resources:
        if resource["account"] != current_account:
            current_account = resource["account"]
            print(f"\n{Fore.MAGENTA}{Style.BRIGHT}=== Account: {current_account} ===\n")

        if resource["region"] != current_region:
            current_region = resource["region"]
            print(f"{Fore.CYAN}{Style.BRIGHT}--- Region: {current_region} ---\n")

        write_resource_details_to_terminal(resource)
        update_resource_summary(resource_summary, resource["resource_type"])

        if current_region not in region_summary:
            region_summary[current_region] = {key: 0 for key in resource_summary.keys()}
        region_summary[current_region] = update_region_summary(region_summary[current_region], resource["resource_type"])

    write_resource_summary_to_terminal(resource_summary)

