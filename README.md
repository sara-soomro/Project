

# Walmart Customer Analysis 🚀  

## 📖 Project Overview  
This is the final project of the Data ZoomCamp 2025 (https://github.com/DataTalksClub/data-engineering-zoomcamp) focuses on building a robust data pipeline to process and visualize Walmart Sales Data. The goal is to extract  dataset from Kaggle ,  store in GCP and transform them using Spark and dbt in BigQuery, and create insightful visualizations using DataStudio Looker.

With a fully automated ETL pipeline orchestrated by Apache Airflow, the project ensures data is collected, processed, and made available for analysis seamlessly. The final output is a set of interactive dashboards that help analyze Walmart sales trends across different dimensions like gender and  purchase Category

 
 

The data pipeline consists of the following major stages:

Extract: Walmart sales data is pulled from an external API using Airflow
Load: The data is stored in GCS 
Transform: First with Apache Spack Raw files are transformed in Parquet and then Using dbt, data is cleaned and structured .
Visualize: Insights are presented using Looker  dashboards
Infrastructure: Terraform is used to provision GCS resources automatically


![Project Overview](https://github.com/sara-soomro/Project/blob/main/project-overview.png?raw=true)


## Prolem Statement 

This dataset is valuable for multiple analytical applications across retail, business, and data science fields. Below are some key insights and use cases:
🛒 1. Customer Segmentation
By analyzing age, gender, purchase amount, and repeat customer behavior, businesses can segment customers into groups. 

📍 Frequent Shoppers – Customers who return often.
📍 High-Value Customers – Those who make large purchases.
📍 Discount-Driven Buyers – Customers who shop mainly during sales.
📍 Impulse Shoppers – Customers who make frequent small purchases.
📍 This segmentation helps in personalized marketing and targeted promotions.

📊 2. Sales Forecasting
Using purchase_date and purchase_amount, businesses can:

Predict future sales trends.
📍 Identify seasonal shopping patterns.
📍 Forecast revenue for inventory planning.

📦 3. Product Performance Analysis
By analyzing product_name, category, rating, and sales amount, businesses can:

Identify top-selling products.
📍 Understand which categories generate the most revenue.
📍 Improve underperforming products.


## 🔹 Tech Stack  
- **Data Extraction:** Python (`pandas`, `requests`), Kaggle API  
- **Data Storage:** Google BigQuery & Google Cloud Storage (GCS)  
- **Data Processing:** Apache Spark (Dataproc Cluster) & DBT  
- **Data Orchestration:** Apachi Airflow(running in Docker) on VM instance in GCS 
- **Data Visualization:** Looker
- **Infrastructure Management:** Terraform (to manage GCS BigQuery , Storage instances (buckets)and cloud resources)

## 🛠 Steps  

### 1️⃣ Data Collection  
- **Source:** Downloading Walmart customer transaction data from [Kaggle](https://www.kaggle.com/).  
- Use **Kaggle API** 
 Unfortunately, I did not find an API to that provides this data on a continuous basis. Therefore, I fetch the data from kaggle as one time operation. However, if an API would be available, the pipeline could be adjusted easily to operate on a schedule on Airflow .It loads data from the website transform it and loads in GCS .
 [(https://www.kaggle.com/datasets/logiccraftbyhimanshi/walmart-customer-purchase-behavior-dataset)]
**setup**
The kaggle data API is used to fetch the data from kaggle. A detailed description and how to authenticate can be found here: https://www.kaggle.com/docs/api. To run the project, it is required to create the environmental variables KAGGLE_USER and KAGGLE_KEY. I stored them in a ".env" file in the airflow folder together with AIRFLOW_UID.
- Store raw data in **Google Cloud Storage (GCS)**.
###  Infrastructure Management :
Terraform is used to create a  bucket for file storage and a  data-set in  BigQuery warehouse .
Step 1.  Therefore, a google cloud project and a service account have to be created.
The project name has to be adjusted in variables.tf. Besides, the key of the service account has to be downloaded as json and needs to be linked in variables.tf as "credentials". 
The service account should have the following roles: **BigQuery Admin, Dataproc Administrator, Editor, Storage Admin and Storage Object Admin**. 
Subsequently, the resources can be created with the terraform commands:
**terraform init**
**terraform plan**
**terraform apply**

### 2️⃣ Data Cleaning & Transformation  
- Process raw data using **Apache Spark** for scalable data transformation.
  raw CSV file is transformed (converting data types)into parquet file and uploaded on GCS Data lake using  Apache Spark .
  Process of Installing and enabling Spark is mentioned in the file Spark.md with all the instructions to run on VM instance .
- Use **DBT** for data modeling and transformations.
   Data models are created - identifying trends and patterns for stakeholders . 


### 3️⃣ Data Storage  
- data is initially stores in Datalate in a bucket in Google Clous Storage .
- Store transformed data in **Google BigQuery** for efficient querying.
 

### 4️⃣ Data Orchestration  
- Use **Kestra (running in Docker)** to schedule and manage data pipeline workflows.
  

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


## 📊 Expected Insights  
✅ Top-selling product categories.  
✅ Customer spending patterns based on gender.  


## 🚀 Future Enhancements  
- Implement **real-time streaming analytics** using Apache Kafka.  
- Build a **predictive model** to forecast sales trends.  

---
**Author:** _Sara Hassan Soomro_  
_Last Updated:_ `March 2025`  


