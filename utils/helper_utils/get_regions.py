import boto3

def get_all_regions():
    ec2_client = boto3.client('ec2')
    try:
        response = ec2_client.describe_regions()
        return [region['RegionName'] for region in response['Regions']]
    except Exception as e:
        print(f"Error fetching regions: {e}")
        return []

def get_user_input_regions(account_name):
    """
    Prompt the user to specify regions for an account.
    If the user presses Enter, return all available regions.
    """

    user_input = input(f"\nSpecify regions for account '{account_name}' (comma-separated), or press Enter for all regions: ").strip()
    if not user_input:
        print("Fetching all available regions...")
        return get_all_regions()
    else:
        return [region.strip() for region in user_input.split(",")]
# test
#regions = get_all_regions()
#if regions:  # If regions are available
 #   print("Available Regions:")
  #  for region_name, region_info in regions.items():
  #      print(f"Region: {region_info['region_name']}")
#else:
 #   print("No regions found or error occurred.")
