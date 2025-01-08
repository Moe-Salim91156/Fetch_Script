import boto3
import json
def read_config_file(config_file):
    with open(config_file, 'r') as file:
        return json.load(file)


