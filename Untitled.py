#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import pyspark
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.context import SparkContext
from pyspark.sql import types
from pyspark.sql.functions import col


# In[2]:


credentials_location = '/home/sara/terraform/mycreds.json'

conf = SparkConf() \
    .setMaster('local[*]') \
    .setAppName('test') \
    .set("spark.jars", "/home/sara/data-engineering-zoomcamp/05-batch/code/data/lib/gcs-connector-hadoop3.2.2.5.jar") \
    .set("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
    .set("spark.hadoop.google.cloud.auth.service.account.json.keyfile", credentials_location)


# In[3]:


sc = SparkContext(conf=conf)

hadoop_conf = sc._jsc.hadoopConfiguration()

hadoop_conf.set("fs.AbstractFileSystem.gs.impl",  "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")
hadoop_conf.set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
hadoop_conf.set("fs.gs.auth.service.account.json.keyfile", credentials_location)
hadoop_conf.set("fs.gs.auth.service.account.enable", "true")


# In[4]:


spark = SparkSession.builder \
    .config(conf=sc.getConf()) \
    .getOrCreate()


# In[33]:


df = spark.read \
    .option("header", "true") \
    .csv('Walmart_customer_purchases.csv')



# In[34]:


df.dtypes


# In[37]:


ischema = types.StructType([
    types.StructField('Customer_ID', types.StringType(), True),
    types.StructField('Age', types.IntegerType(), True),
    types.StructField('Gender', types.StringType(), True),
    types.StructField('City', types.StringType(), True),
    types.StructField('Category', types.StringType(), True),
    types.StructField('Product_Name', types.StringType(), True),
    types.StructField('Purchase_Date', types.TimestampType(), True),
    types.StructField('Purchase_Amount', types.FloatType(), True),
    types.StructField('Payment_Method',types.StringType(), True),
    types.StructField('Discount_Applied', types.StringType(), True),
    types.StructField('Rating', types.IntegerType(), True),
    types.StructField('Repeat_Customer', types.StringType(), True)
])


# In[38]:


df = spark.read.csv("Walmart_customer_purchases.csv", schema=ischema, header=True)


# In[40]:


df.printSchema()


# In[32]:


from pyspark.sql.functions import count, when
df.select(
    count(when(col("Purchase_Amount").isNull(), 1)).alias("null_count"),
    count(when(col("Purchase_Amount").isNotNull(), 1)).alias("non_null_count")
).show()


# In[41]:


gcs_output_path = "gs://buc-inspiring-453522_m5/Walmart_customer_purchases.parquet"


# In[42]:


# Writing DataFrame to GCS in Parquet format with overwrite mode
df.write \
    .mode("overwrite") \
    .format("parquet") \
    .save(gcs_output_path)


# In[ ]:




