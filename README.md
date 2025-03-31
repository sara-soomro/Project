

# Walmart Customer Analysis 🚀  

## 📖 Problem Statement 
This is the final project of the Data ZoomCamp 2025 (https://github.com/DataTalksClub/data-engineering-zoomcamp) focuses on building a robust data pipeline to process and visualize Walmart Sales Data. The goal is to extract  dataset from Kaggle ,  store in GCP and transform them using Spark and dbt in BigQuery, and create insightful visualizations using DataStudio Looker.

With a fully automated ETL pipeline orchestrated by Kestra, the project ensures data is collected, processed, and made available for analysis seamlessly. The final output is a set of interactive dashboards that help analyze Walmart sales trends across different dimensions like gender and  purchase Category . Identifying  **Top-selling product categories** and **Customer spending patterns based on gender**

 
 
## 📖 Project Overview
The data pipeline consists of the following major stages:

Extract: Walmart sales data is pulled from an external API Kaggle using pythonScript running through Apache Spark (DataProc) in a Cloud VM instance .
Load: The data is stored in GCS 
Transform: First with Apache Spack Raw files are transformed in Parquet and then Using dbt, data is cleaned and structured .
Visualize: Insights are presented using Looker  dashboards
Infrastructure: Terraform is used to provision GCS resources automatically


![Project Overview](https://github.com/sara-soomro/Project/blob/main/final-Project.png?raw=true)


## 🔹 Tech Stack  
- **Data Extraction:** Python (`pandas`, `requests`), Kaggle API  
- **Data Storage:** Google BigQuery & Google Cloud Storage (GCS)  
- **Data Processing:** Apache Spark (Dataproc Cluster) & DBT  
- **Data Orchestration:** Kestra(running in Docker) on VM instance in GCS 
- **Data Visualization:** Looker
- **Infrastructure Management:** Terraform (to manage GCS BigQuery , Storage instances (buckets)and cloud resources)

## 🛠 Steps  

### 1️⃣ Data Collection  
- **Source:** Downloading Walmart customer transaction data from [Kaggle](https://www.kaggle.com/).  
- Use **Kaggle API** 
 Unfortunately, I did not find an API to that provides this data on a continuous basis. Therefore, I fetch the data from kaggle as one time operation. However, if an API would be available, the pipeline could be adjusted easily to operate on a schedule on Kestra .It loads data from the website transform it and loads in GCS .
 [(https://www.kaggle.com/datasets/logiccraftbyhimanshi/walmart-customer-purchase-behavior-dataset)]

Currently Python script using **Apacke Spark** running on **DataProc Cluster** is collecting data from Kaggle API

![VM](https://github.com/sara-soomro/Project/blob/main/VM_cluster.png)
- Store raw data on **VM instance** 

###  Infrastructure Management :
Terraform is used to create a  bucket for file storage and a  data-set in  BigQuery warehouse .
Therefore, a google cloud project and a service account have to be created.
Besides, the key of the service account has to be downloaded as json and needs to be linked in main.tf file along with project ID
The service account should have the following roles: **BigQuery Admin, Dataproc Administrator, Editor, Storage Admin and Storage Object Admin**. 
Subsequently, the resources can be created with the terraform commands:
**terraform init**
**terraform plan**
**terraform apply**

### 2️⃣ Data Cleaning & Transformation  

Raw CSV file is transformed (converting data types)into parquet file and uploaded on GCS Data lake using  Apache Spark .


CSV Files are downloaded from Kaggle on VM instance . Using Apache Spark raw CSV files are transformed (Data types) and converted to parquet files .
Finaly the transformed parquet files are stored on GCP Bucket .


![Parquet-GCP](https://github.com/sara-soomro/Project/blob/main/spark/CSV-Parquet.png)
![Project Overview](https://github.com/sara-soomro/Project/blob/main/spark/cluster.png)

- Use **DBT** for data modeling and transformations.
   Data models are created - identifying trends and patterns for stakeholders . 


### 3️⃣ Data Storage  

- Data is initially stores in Data lake in a bucket in Google Cloud Storage .
- Store transformed data in **Google BigQuery** for efficient querying. Data set is created by partitioning on the purchare_date column 
![DS](https://github.com/sara-soomro/Project/blob/main/BigQuery/Dataset.jpeg)


 

### 4️⃣ Data Orchestration  
- Use **Kestra (running in Docker)** to schedule and manage data pipeline workflows.In this project the Dataset was a one off data so it has not been scheduled to take on more data .Attached Kestra files can we modified with  schedules incase more data needs to be ingested . 
  

### 5️⃣ Data Analysis & Insights  
- **Customer Segmentation:** Group customers by purchase behavior.  
- **Product Trends:** Identify best-selling and underperforming items.  

### 6️⃣ Data Visualization  
- Create **interactive dashboards** using **Looker**. to analize customer behaviour .
  ## Looker Studio Report

You can view the detailed interactive report on Looker Studio 
[here](https://lookerstudio.google.com/u/0/reporting/34f3a837-48ab-413a-9c2e-07ab445dbd1e/page/agjDF).

![Data Looker](https://github.com/sara-soomro/Project/blob/main/looker1.png?raw=true)
![Data Looker](https://github.com/sara-soomro/Project/blob/main/looker.png?raw=true)

# Running this project
### Prerequisites
* A Google Cloud Platform project named 
* A service account with permission to create buckets and BigQuery datasets. For reference, the following roles where set:
    * BigQuery Data Editor
    * BigQuery User
    * Storage Admin
* A service account JSON key. This needs to be placed in terraform/keys/ with the name my-creds.json

### Steps
#### 1. Clone the repository and access the project directory: 

```bash
 git clone https://github.com/Project.git
 cd Project
```

#### 2. Deploy the infrastructure with Terraform:

refer to terraform 



#### 3. Data Transformationn

 Refer to spark folder 
 
#### 3. Big Query 

Run the sql query in the BigQuery foler to create Data-Set .

### 4. dbt 

Details on how to run DBT Models are in Walmart-Project folder .

### 5. Looker 

After creating DBT Model the data can ve visualized in Google Data Looker 

 
## 📊 Expected Insights  
✅ Top-selling product categories.  
✅ Customer spending patterns based on gender.  


## 🚀 Future Enhancements  
- Implement **real-time streaming analytics** using Apache Kafka.  
- Build a **predictive model** to forecast sales trends.  

---
**Author:** _Sara Hassan Soomro_  
_Last Updated:_ `March 2025`  


