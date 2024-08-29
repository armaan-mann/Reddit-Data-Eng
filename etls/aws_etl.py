import s3fs
from utils.constants import AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY
from airflow.utils.log.logging_mixin import LoggingMixin

logger = LoggingMixin().log


def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(anon=False,
                               key=AWS_ACCESS_KEY_ID,
                               secret=AWS_ACCESS_KEY)
        return s3
    except Exception as e:
        logger.error(e)


def create_bucket_if_not_exist(s3: s3fs.S3FileSystem, bucket_name: str):
    try:
        if not s3.exists(bucket_name):
            s3.mkdir(bucket_name)
            logger.info(f'Created bucket {bucket_name}')
        else:
            logger.info(f'Bucket {bucket_name} already exists')
    except Exception as e:
        logger.error(e)


def upload_to_s3(s3: s3fs.S3FileSystem, file_path: str, bucket_name: str, file_name: str):
    try:
        s3.put(file_path, bucket_name + '/raw/' + file_name)
        logger.info(f'Uploaded {file_name} to {bucket_name}/raw/{file_name}')
    except Exception as e:
        logger.error(e)
