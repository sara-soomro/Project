
### 1. Infrastructure Setup (Terraform)
```bash
# Clone repository
git clone https://github.com/sara-soomro/Project.git
cd terraform/

# Initialize Terraform
terraform init

# Plan infrastructure
terraform plan

# Apply configuration
terraform apply
```
**Critical Configurations:**  
Update `main.tf` with:
- GCP bucket name
- BigQuery dataset ID
- Service account credentials path  
Store service account JSON in `/terraform/keys/`


![infrastructure](https://github.com/sara-soomro/Project/blob/main/terraform/busket.jpeg)

