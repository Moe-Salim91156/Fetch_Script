import boto3

def display_results(resource_name, resources, account_name, region):
    print(f"\n{'='*50}")
    print(f"{resource_name} for {account_name} in {region}:")
    if not resources:
        print(f"  No {resource_name} found.")
    else:
        for resource in resources:
            print(resource)
    print(f"{'='*50}")


