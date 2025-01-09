import boto3
def fetch_ebs_volumes(session, region):
    ec2_client = session.client('ec2', region_name=region)
    response = ec2_client.describe_volumes()
    return response['Volumes']

