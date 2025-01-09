import boto3

def fetch_subnets(session, region, account_name):
    subnets = []
    try:
        ec2_client = session.client('ec2', region_name=region)
        response = ec2_client.describe_subnets()

        for subnet in response['Subnets']:
            subnets.append({
                'resource_type': 'subnet',
                'resource_id': subnet['SubnetId'],
                'region': region,
                'account': account_name,
                'metadata': {
                    'CidrBlock': subnet['CidrBlock'],
                    'AvailabilityZone': subnet['AvailabilityZone'],
                    'VpcId': subnet['VpcId'],
                    'Tags': subnet.get('Tags', 'N/A')
                }
            })
    except Exception as e:
        print(f"Error fetching subnets: {e}")

    return (subnets)

