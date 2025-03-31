### 3. Data Transformation (Dataproc)

To getup spark on your local machine or VM instance in GCP refer to the linux.md file and pyspark.md file 

CSV Files are downloaded from Kaggle on VM instance . Using Apache Spark raw CSV files are transformed (Data types)
The Schema is infered using Pandas and converted to parquet files .
Finaly the transformed parquet files are stored on GCP Bucket .


```bash
# Create Dataproc cluster
gcloud dataproc clusters create cluster-bfdd-m \
    --region=us-west2-c \
    --single-node \
    --service-account=<YOUR_SERVICE_ACCOUNT>

# Submit Spark job
gcloud dataproc jobs submit pyspark \
    --cluster=cluster \
    --region=us-central1 \
    --jars=gs://spark-lib/bigquery/spark-3.5-bigquery-0.41.1.jar \
    gs://<YOUR_BUCKET>/code/06_spark.py \

```
Before you run the spark job. Make sure :

- once it is created, in the GCS Bucket section, you will see other buckets apart from the one you created, replace the dataproc temp bucket in the 06_spark.py file with your temp dataproc bucket id.

- put the 06_spark.py file in your original gcs bucket in an other folder called "code".
```bash
gsutil cp 06_spark.py gs://<BUCKET>/code/



![Parquet-GCP](https://github.com/sara-soomro/Project/blob/main/spark/CSV-Parquet.png)
![Project Overview](https://github.com/sara-soomro/Project/blob/main/spark/cluster.png)

```
