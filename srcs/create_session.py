import boto3

def create_aws_session(profile): # takes profile as argument and create for each account a seesion
    try:
        session = boto3.Session(profile_name=profile)
        print(f"Session for Profile : ({profile}) has been created Sucessfully")
        return (session)
    except:
        print(f"Error Creating Session for : {profile}")
        return None
# this function is responsible for creating The Session for Each Aws profile provided (account);
