CREATE OR REPLACE EXTERNAL TABLE `inspiring-code-453522-m5.soomro_zoomcamp_DS.Walmart_customer_purchases`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://buc-inspiring-453522_m5/Walmart_customer_purchases.parquet/part-*.parquet']
);

CREATE OR REPLACE TABLE `inspiring-code-453522-m5.soomro_zoomcamp_DS.Walmart_customer_purchases_partitioned`
PARTITION BY DATE(Purchase_Date)
AS
SELECT * FROM `inspiring-code-453522-m5.soomro_zoomcamp_DS.Walmart_customer_purchases`;
