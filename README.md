# AWS Inventory Script

## Description
This script enumerates AWS resources across multiple accounts and regions. It retrieves information about the following resources:

- VPC
- EC2 Instances
- RDS Databases
- S3 Buckets
- Security Groups
- IAM Roles
- Subnets
- EBS Volumes
- Network ACLs

The results are summarized and displayed in the terminal.

## Prerequisites

### 1. Set Up a Virtual Environment

#### On Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 2. Install Dependencies

Once the virtual environment is activated, install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configure AWS CLI

Make sure your AWS CLI is configured with valid credentials:
```bash
aws configure
```

Make sure your AWS CLI is configured with valid credentials:

aws configure --profile <profile-name>

You will need to provide your AWS Access Key ID, Secret Access Key, default region, and output format.

### 4. Prepare the Config File

Create or update the configuration file config.json inside the config/ folder. The file should have the following structure for multiple accounts:
```json
{
    "accounts": [
        {
            "account_name": "Root_Account",
            "profile_name": "default",
            "regions": ["us-east-1"]
        },
        {
            "account_name": "New_Account",
            "profile_name": "new_account_profile",
            "regions": ["us-west-2", "eu-central-1"] # or u can put [] for all regions
        }
    ]
}

```

- **accounts**: A list of AWS accounts to access.
- **profile_name**: The AWS profile inside account or whole other account.
- **regions**: (Optional) A list of regions to query. If omitted, the script will prompt the user to input regions.

### 5. Run the Script

#### On Linux:
```bash
python3 aws_inventory.py
```

#### On Windows:
```bash
python aws_inventory.py
```

## Assumptions
- The `config.json` file must be located in a `config/` directory relative to the script.
- If no regions are provided in the `config.json` file, the script will prompt the user for input.
- The AWS CLI must be configured with access and secret keys for accessing AWS resources.

## Limitations
- The script only retrieves the following AWS resources:
  - VPC
  - EC2 Instances
  - RDS Databases
  - S3 Buckets
  - Security Groups
  - IAM Roles
  - Subnets
  - EBS Volumes
  - Network ACLs


