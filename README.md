

# Walmart Customer Analysis 🚀  

## 📖 Project Overview  
This is the final project of the data engineering zoomcamp (https://github.com/DataTalksClub/data-engineering-zoomcamp)l
As part of the project, I created a datapipeline that loads and processes data from kaggle to analyze Walmart customer purchasing behavior using transactional data. The data can be found here: [(https://www.kaggle.com/datasets/logiccraftbyhimanshi/walmart-customer-purchase-behavior-dataset)]
Its an **end-to-end data pipeline** to extract, clean, store, and analyze data to derive insights about shopping trends.  

## 🔹 Tech Stack  
- **Data Extraction:** Python (`pandas`, `requests`), Kaggle API  
- **Data Storage:** Google BigQuery & Google Cloud Storage (GCS)  
- **Data Processing:** Apache Spark (Dataproc Cluster) & DBT  
- **Data Orchestration:** Kestra (running in Docker) on VM instance in GCS 
- **Data Visualization:** Looker
- **Infrastructure Management:** Terraform (to manage GCS BigQuery , Storage instances (buckets)and cloud resources)

## 🛠 Steps  

### 1️⃣ Data Collection  
- **Source:** Downloading Walmart customer transaction data from [Kaggle](https://www.kaggle.com/).  
- Use **Kaggle API** 
 Unfortunately, I did not find an API to that provides this data on a continuous basis. Therefore, I fetch the data from kaggle as one time operation. However, if an API would be available, the pipeline could be adjusted easily to operate on a schedule on Kestra .It loads data from the website transform it and loads in GCS .
**setup**
The kaggle data API is used to fetch the data from kaggle. A detailed description and how to authenticate can be found here: https://www.kaggle.com/docs/api. To run the project, it is required to create the environmental variables KAGGLE_USER and KAGGLE_KEY. I stored them in a ".env" file in the airflow folder together with AIRFLOW_UID.
- Store raw data in **Google Cloud Storage (GCS)**.
###  Infrastructure Management :
Terraform is used to create two buckets, a dataproc cluster and a bigquery data warehouse in the google cloud. Therefore, a google cloud project and a service account have to be created. The project name has to be adjusted in variables.tf. Besides, the key of the service account has to be downloaded as json and needs to be linked in variables.tf as "credentials". The service account should have the following roles: BigQuery Admin, Dataproc Administrator, Editor, Storage Admin and Storage Object Admin. Subsequently, the resources can be created with the terraform commands: terraform init terraform plan terraform apply

### 2️⃣ Data Cleaning & Transformation  
- Process raw data using **Apache Spark** for scalable data transformation.
  Process of Installing and enabling Spark is mentioned in the file Spark.md with all the instructions to run on VM instance .
- Use **DBT** for data modeling and transformations.  

### 3️⃣ Data Storage  
- data is initially stores in Datalate in a bucket in Google Clous Storage .
- Store transformed data in **Google BigQuery** for efficient querying.
 

### 4️⃣ Data Orchestration  
- Use **Kestra (running in Docker)** to schedule and manage data pipeline workflows.
  

### 5️⃣ Data Analysis & Insights  
- **Customer Segmentation:** Group customers by purchase behavior.  
- **Product Trends:** Identify best-selling and underperforming items.  
- **Seasonality Analysis:** Find peak shopping times and trends.  

### 6️⃣ Data Visualization  
- Create **interactive dashboards** using **Looker**.  
- Generate **monthly sales and customer retention reports**.  

## 📊 Expected Insights  
✅ Top-selling product categories.  
✅ Customer spending patterns based on demographics.  
✅ Impact of discounts and promotions on sales.  

## 🚀 Future Enhancements  
- Implement **real-time streaming analytics** using Apache Kafka.  
- Build a **predictive model** to forecast sales trends.  

---
**Author:** _Sara Hassan Soomro_  
_Last Updated:_ `March 2025`  


