import boto3
def fetch_security_groups(session, region, account_name):
    security_groups = []
    try:
        ec2_client = session.client('ec2', region_name=region)
        response = ec2_client.describe_security_groups()
        
        for sg in response['SecurityGroups']:
            security_groups.append({
                'resource_type': 'security_group',
                'resource_id': sg['GroupId'],
                'region': region,
                'account': account_name,  
                'metadata': {
                    'GroupName': sg['GroupName'],
                    'Description': sg['Description'],
                    'VpcId': sg.get('VpcId', 'N/A'),
                    'Tags': sg.get('Tags', 'N/A')
                }
            })
    except Exception as e:
        print(f"Error fetching security groups: {e}")
    
    return security_groups

