import boto3

def fetch_iam_roles(session, region, account_name):
    iam_roles = []
    try:
        iam_client = session.client('iam')
        response = iam_client.list_roles()
        
        for role in response['Roles']:
            iam_roles.append({
                'resource_type': 'iam_role',
                'resource_id': role['RoleName'],
                'region': region,
                'account': account_name,
                'metadata': {
                    'RoleId': role['RoleId'],
                    'Arn': role['Arn'],
                    'CreateDate': str(role['CreateDate']),
                    'Tags': 'N/A'  
                    }
            })
    except Exception as e:
        print(f"Error fetching IAM roles: {e}")
    
    return iam_roles

