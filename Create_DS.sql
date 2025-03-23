CREATE OR REPLACE EXTERNAL TABLE `inspiring-code-453522-m5.soomro_zoomcamp_DS.Walmart_customer_purchases`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://buc-inspiring-453522_m5/Walmart_customer_purchases.parquet/part-*.parquet']
);


/* 
  External table is created in BIG QUERY via Parquet files stored on GCS .  
  Partitioned table is made partitioning data based on Purchase Date column 
*/

  
CREATE OR REPLACE TABLE `inspiring-code-453522-m5.soomro_zoomcamp_DS.Walmart_customer_purchases_partitioned`
PARTITION BY DATE(Purchase_Date)
AS
SELECT * FROM `inspiring-code-453522-m5.soomro_zoomcamp_DS.Walmart_customer_purchases`;
