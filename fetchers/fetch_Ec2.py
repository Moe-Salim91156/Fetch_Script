import boto3
from utils.helper_utils.display_logs import log_message

def fetch_ec2_instances(session, region,account_name):
    ec2_instance = []

    try:
        ec2_client = session.client('ec2',region_name= region)
        response = ec2_client.describe_instances()

        for reservation in response['Reservations']:
            for instance in reservations['Instances']:
                ec2_instance.append({
                    'ResourceId': 'Ec2',
                    'InstanceId': instance.get('instanceId'),
                    'state': instance.get('State',{}).get('Name'),
                    'Region': region,
                    'Account_name': account_name,
                    })
    except Exception as e:
        log_message(f"erorr fetching EC2 instance for {account_name} in {region}, {e}")
    return (ec2_instance)
