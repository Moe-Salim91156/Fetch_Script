import boto3
import boto3

def fetch_vpcs(session, region, account_name):
    client = session.client('ec2', region_name=region)
    try:
        response = client.describe_vpcs()
        vpcs = []
        for vpc in response.get('Vpcs', []):
            vpcs.append({
                "resource_type": "VPC",
                "resource_id": vpc["VpcId"],
                "region": region,
                "account": account_name,
                "metadata": {
                    "cidr_block": vpc.get("CidrBlock"),
                    "is_default": vpc.get("IsDefault"),
                    "state": vpc.get("State")
                }
            })
        return vpcs
    except Exception as e:
        print(f"Error fetching VPCs for account {account_name} in region {region}: {e}")
        return []
