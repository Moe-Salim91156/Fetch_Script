import boto3
import json

def fetch_Vpcs():
    client = session.client('ec2',region_name = region)
    response = client.describe_vpcs()
    return response['Vcps']

