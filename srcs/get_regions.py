import boto3

def get_all_regions():
    general_client = boto3.client('ec2') # why (Ec2) here ? / 

    try:
        response_json = general_client.describe_regions()
        regions = {}
        for region in response_json['Regions']:
            region_name = region['RegionName']
            regions[region_name] = {'region_name' : region_name}
    except:
        print(f"error fetching regions")
        return {}
    return regions

# test
#regions = get_all_regions()
#if regions:  # If regions are available
 #   print("Available Regions:")
  #  for region_name, region_info in regions.items():
  #      print(f"Region: {region_info['region_name']}")
#else:
 #   print("No regions found or error occurred.")
