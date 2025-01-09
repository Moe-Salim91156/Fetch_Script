import boto3

def fetch_acls(session,region):
    g_client = session.client('ec2',region_name=region)
    response = g_client.describe_network_acls()
    return (response['NetworkAcls'])

