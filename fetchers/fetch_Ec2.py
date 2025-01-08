import boto3

def fetch_ec2_instances(session, region):
    ec2_client = session.client('ec2', region_name=region)
    
    try:
        response_json = ec2_client.describe_instances()
        
        if 'Reservations' in response_json: #if there is instances(respone_json)
            instances = []
            for json_filter in response_json['Reservations']:
                for instance in json_filter['Instances']:
                    instances.append(instance)
            return instances
        else:
            print("No reservations found in response")
            return []

    except Exception as e:
        print(f"Error fetching EC2 instances: {e}")
        return []

