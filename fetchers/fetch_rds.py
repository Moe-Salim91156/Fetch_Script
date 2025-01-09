import boto3

def fetch_rds_instances(session, region, account_name):
    rds_instances = []
    try:
        rds_client = session.client('rds', region_name=region)
        response = rds_client.describe_db_instances()
        
        for db_instance in response['DBInstances']:
            rds_instances.append({
                'resource_type': 'rds_instance',
                'resource_id': db_instance['DBInstanceIdentifier'],
                'region': region,
                'account': account_name,
                'metadata': {
                    'Engine': db_instance['Engine'],
                    'Status': db_instance['DBInstanceStatus'],
                    'Endpoint': db_instance.get('Endpoint', {}).get('Address', 'N/A'),
                    'Tags': db_instance.get('TagList', 'N/A')
                }
            })
    except Exception as e:
        print(f"Error fetching RDS instances: {e}")
    
    return rds_instances

