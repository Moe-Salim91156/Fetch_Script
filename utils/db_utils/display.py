from tabulate import tabulate

# Step 2: Define the display_resources_table function
def display_resources_table(resources):
    table_data = [
        [
            resource["account"],
            resource["region"],
            resource["resource_type"],
            resource["resource_id"],
            resource["metadata"],
        ]
        for resource in resources
    ]
    headers = ["Account", "Region", "Resource Type", "Resource ID", "Metadata"]
    print(tabulate(table_data, headers, tablefmt="grid"))
