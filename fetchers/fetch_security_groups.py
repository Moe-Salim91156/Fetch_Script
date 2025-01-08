import boto3

def fetch_security_groups(session, region):
    """
    Fetch security groups for the specified AWS region.

    Args:
        session: Boto3 session object.
        region: The AWS region.

    Returns:
        A list of security groups.
    """
    security_groups = []
    try:
        ec2_client = session.client('ec2', region_name=region)
        response = ec2_client.describe_security_groups()
        
        for sg in response['SecurityGroups']:
            security_groups.append({
                'GroupId': sg.get('GroupId'),
                'GroupName': sg.get('GroupName'),
                'Description': sg.get('Description'),
                'VpcId': sg.get('VpcId')
            })
    except Exception as e:
        print(f"Error fetching security groups in {region}: {e}")
    return security_groups

