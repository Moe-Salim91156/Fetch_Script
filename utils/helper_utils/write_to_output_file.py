from utils.helper_utils.display_logs import log_message

def format_metadata(metadata):
    """Format metadata into key-value pairs."""

    return "\n".join([f"    {key}: {value}" for key, value in metadata.items()])

def write_resource_details(file, resource):
    """Write details for a single resource."""

    file.write(f"Resource Type: {resource['resource_type']}\n")
    file.write(f"Resource ID: {resource['resource_id']}\n")
    file.write("Metadata:\n")
    file.write(f"{format_metadata(resource['metadata'])}\n")
    file.write("-" * 40 + "\n")

def update_resource_summary(resource_summary, resource_type):
    """Update the resource summary with the count of a specific resource type."""

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

    resource_type = resource_type.lower()
    if resource_type in resource_type_map:
        mapped_type = resource_type_map[resource_type]
        if mapped_type in resource_summary:
            resource_summary[mapped_type] += 1
        else:
            resource_summary[mapped_type] = 1
    else:
        print(f"Unknown resource type: {resource_type}")

def write_resource_summary(file, resource_summary):
    """Write the summary of resource counts."""

    file.write("\n--- Resource Summary ---\n")
    file.write(f"{'Resource Type':<20}{'Count':<10}\n")
    file.write("-" * 40 + "\n")
    for resource_type, count in resource_summary.items():
        file.write(f"{resource_type:<20}{count:<10}\n")
    file.write("-" * 40 + "\n")


def write_to_file(resources, mode):
    "write the whole run to an output file for further use"

    if mode == "w":
        with open("output_files/output.txt", mode):
            pass
    elif mode == "a":
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

        all_resources=[]
        with open("output_files/output.txt", mode) as file:
            current_account = None
            current_region = None

            for resource in resources:
                if resource["account"] != current_account:
                    current_account = resource["account"]
                    file.write(f"\n=== Account: {current_account} ===\n\n")

                if resource["region"] != current_region:
                    current_region = resource["region"]
                    file.write(f"--- Region: {current_region} ---\n\n")

                write_resource_details(file, resource)

                update_resource_summary(resource_summary, resource["resource_type"])

                all_resources.append(resource)

            write_resource_summary(file, resource_summary)

