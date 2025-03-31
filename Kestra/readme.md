Prerequisite :
Docker / Dokcker-compose installed on VM instance.

To start the docker-compose, use the following commands: 
**docker-compose build**


**docker-compose up**
to start an instance of Kestra which can be accessed on local browser on port 8080
https:localhost:8080

First Flowchart
**gcp_kv** values are set in this workflow to set the Google Credentials , ProjectId , Bucket ID and Dataset .

Second Flowchart
**Spark-gcp.yaml**
In the pyspark job the files fetched from kaggle  are transformed and finally written to GCP
Subsequently, google cloud SDK is authenticated, 
the pyspark script is uploaded and the pyspark job is submitted to the dataproc server.

**GCP-BigQuery.yaml**
Third Task : a partitioned BigQuery table is created from the initial one .

