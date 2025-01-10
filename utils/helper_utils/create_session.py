import boto3
from utils.helper_utils.display_logs import log_message
def create_aws_session(profile): # takes profile as argument and create for each account a seesion
    try:
        session = boto3.Session(profile_name=profile)
        log_message(f"Session for Profile : ({profile}) has been created Sucessfully")
        return (session)
    except:
        log_message(f"Error Creating Session for : {profile}","ERROR")
        return None
# this function is responsible for creating The Session for Each Aws profile provided (account);
