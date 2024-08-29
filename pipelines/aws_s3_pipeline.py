from etls.aws_etl import connect_to_s3, create_bucket_if_not_exist, upload_to_s3
from utils.constants import AWS_BUCKET_NAME


def upload_s3_pipeline(ti):
    output_file_name = ti.xcom_pull(task_ids='reddit_extraction', key='return_value')

    s3 = connect_to_s3()
    create_bucket_if_not_exist(s3, AWS_BUCKET_NAME)
    upload_to_s3(s3, output_file_name, AWS_BUCKET_NAME, output_file_name.split('/')[-1])