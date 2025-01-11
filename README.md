# AWS Inventory Script

## Description
This Python script enumerates AWS resources from multiple accounts and regions. It fetches key resources like:

- VPC
- EC2 Instances
- RDS Databases
- S3 Buckets
- Security Groups
- IAM Roles
- Subnets
- EBS Volumes
- Network ACLs

The script collects resource details from the specified AWS regions and displays a summary in the terminal.

## Prerequisites

### Dependencies
All required dependencies are listed in the `requirements.txt` file.

### Setting up the environment

Ensure you have configured your AWS CLI with valid AWS access and secret keys. You can configure it using:

aws configure

-> Put Your access key and secret key

#### 1. Create a Virtual Environment:

On **Linux**:
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

on **Windows**
python -m venv env
pip install -r requirements.txt

#### 1. modify the config/config.json file for your need:
example : 
{
    "accounts": [
        {
            "account_name": "Root_Account",
            "profile_name": "default",
            "regions": []
        },
        {
            "account_name": "IAM_Account",
            "profile_name": "iam_user_profile",
            "regions": ["us-east-1"]
        }
    ]
}


