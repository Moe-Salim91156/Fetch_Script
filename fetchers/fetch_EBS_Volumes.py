import boto3

def fetch_ebs(session, region, account_name):
    ebs_volumes = []
    try:
        ec2_client = session.client('ec2', region_name=region)
        response = ec2_client.describe_volumes()

        for volume in response['Volumes']:
            ebs_volumes.append({
                'resource_type': 'ebs_volume',
                'resource_id': volume['VolumeId'],
                'region': region,
                'account': account_name,
                'metadata': {
                    'Size': volume['Size'],
                    'State': volume['State'],
                    'VolumeType': volume['VolumeType'],
                    'Tags': volume.get('Tags', 'N/A')
                }
            })
    except Exception as e:
        print(f"Error fetching EBS volumes: {e}")

    return (ebs_volumes)

