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
You will need to provide your AWS Access Key ID, Secret Access Key, default region, and output format.

### 4. Prepare the Config File

Create a configuration file named `config.json` inside a `config/` folder. The file should have the following structure:

```json
{
    "accounts": [
        {
            "account_id": "123456789012",
            "role_name": "RoleToAssume",
            "regions": ["us-east-1", "us-west-1"]
        }
    ]
}
```

- **accounts**: A list of AWS accounts to access.
- **account_id**: The AWS account ID.
- **role_name**: The IAM role name to assume for cross-account access.
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


