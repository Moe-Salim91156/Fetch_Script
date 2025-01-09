import boto3


def fetch_acls(session, region, account_name):
    acls = []
    try:
        ec2_client = session.client('ec2', region_name=region)
        response = ec2_client.describe_network_acls()

        for acl in response['NetworkAcls']:
            acls.append({
                'resource_type': 'network_acl',
                'resource_id': acl['NetworkAclId'],
                'region': region,
                'account': account_name,
                'metadata': {
                    'VpcId': acl.get('VpcId', 'N/A'),
                    'Tags': acl.get('Tags', 'N/A')
                }
            })
    except Exception as e:
        print(f"Error fetching network ACLs: {e}")

    return (acls)

