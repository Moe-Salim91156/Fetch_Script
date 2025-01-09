import boto3

def fetch_S3_Buckets(session,region):
    s3_client = session.client('s3')
    response = s3_client.list_buckets()
    return (response['Buckets'])
