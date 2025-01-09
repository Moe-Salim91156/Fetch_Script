import boto3

def fetch_S3_Buckets(session, region, account_name):
    s3_buckets = []
    try:
        s3_client = session.client('s3', region_name=region)
        response = s3_client.list_buckets()

        for bucket in response['Buckets']:
            s3_buckets.append({
                'resource_type': 's3_bucket',
                'resource_id': bucket['Name'],
                'region': region,
                'account': account_name,
                'metadata': {
                    'CreationDate': str(bucket['CreationDate']),
                    'Tags': 'N/A' 
                    }
            })
    except Exception as e:
        print(f"Error fetching S3 buckets: {e}")

    return s3_buckets

