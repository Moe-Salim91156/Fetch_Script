import boto3

def fetch_rds_instances(session,region):
    rds_client = session.client('rds',region_name=region)
    response = rds_client.describe_db_instances()
    return(response['DBInstances'])

