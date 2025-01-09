import boto3
def write_to_file(resources, file_name="output.txt"):
    def format_metadata(metadata):
        """Format metadata into key-value pairs."""
        return "\n".join([f"    {key}: {value}" for key, value in metadata.items()])

    with open(file_name, "w") as file:
        current_account = None
        current_region = None

        for resource in resources:
            # Add a header for a new account
            if resource["account"] != current_account:
                current_account = resource["account"]
                file.write(f"\n=== Account: {current_account} ===\n\n")

            # Add a sub-header for a new region
            if resource["region"] != current_region:
                current_region = resource["region"]
                file.write(f"--- Region: {current_region} ---\n\n")

            # Write resource details
            file.write(f"Resource Type: {resource['resource_type']}\n")
            file.write(f"Resource ID: {resource['resource_id']}\n")
            file.write("Metadata:\n")
            file.write(f"{format_metadata(resource['metadata'])}\n")
            file.write("-" * 40 + "\n")

        print(f"Output successfully written to {file_name}")
