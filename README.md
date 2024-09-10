# Reddit Data Pipeline with Airflow, Celery, PostgreSQL, S3, AWS Glue, Athena, and Redshift

This project implements a robust data pipeline to extract, transform, and load (ETL) Reddit data into an Amazon Redshift data warehouse. The pipeline leverages a range of services, including Apache Airflow, Celery, PostgreSQL, Amazon S3, AWS Glue, Amazon Athena, and Amazon Redshift.

## Key Features

- **Data Extraction**: Retrieves Reddit data using its API.
- **Raw Data Storage**: Uses Apache Airflow to store raw data in Amazon S3.
- **Data Transformation**: AWS Glue and Amazon Athena perform the necessary transformations.
- **Data Loading**: Loads the processed data into Amazon Redshift for querying and analytics.

## Pipeline Components

- **Reddit API**: The source from which Reddit data is collected.
- **Apache Airflow & Celery**: Handle the orchestration of ETL tasks, managing workflow automation and task distribution.
- **PostgreSQL**: Used for temporary data storage and metadata management during the pipeline process.
- **Amazon S3**: Serves as the storage location for raw Reddit data before processing.
- **AWS Glue**: Catalogs the data and manages the transformation via ETL jobs.
- **Amazon Athena**: Enables SQL-based querying and transformation of data.
- **Amazon Redshift**: The destination for transformed data, where it can be used for analytics and advanced querying.
