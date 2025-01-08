import boto3

def fetch_vpcs(session, region):
    vpcs = []
    try:
        ec2_client = session.client('ec2', region_name=region)
        response = ec2_client.describe_vpcs()
        for vpc in response['Vpcs']:
            vpcs.append({
                'VpcId': vpc.get('VpcId'),
                'CidrBlock': vpc.get('CidrBlock'),
                'IsDefault': vpc.get('IsDefault')
            })
    except Exception as e:
        print(f"Error fetching VPCs in {region}: {e}")
    return vpcs

