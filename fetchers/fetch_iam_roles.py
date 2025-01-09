import boto3

def fetch_iam_roles(session,region):
    iam_client = session.client('iam')
    response = iam_client.list_roles()
    return (response['Roles'])
