from airflow.operators.python import PythonOperator
from airflow.utils.log.logging_mixin import LoggingMixin
from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv
from utils.constants import CLIENT_ID, SECRET, REDDIT_USERNAME, REDDIT_PASSWORD, OUTPUT_PATH
import pandas as pd

logger = LoggingMixin().log


def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    """
    Connects to a reddit instance -> extracts information -> transforms the information -> loads to a csv

    :param file_name: where the extracted data will be saved
    :param subreddit: the name of the subreddit to be extracted from
    :param time_filter: time range to extract data from. Day means all posts from past day
    :param limit: The maximum number of posts to extract.
    :return: Instance of reddit
    """
    instance = connect_reddit(CLIENT_ID, SECRET, username=REDDIT_USERNAME, password=REDDIT_PASSWORD,
                              user_agent='test script by u/armaan675')
    posts = extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)
    post_df = transform_data(post_df)
    load_data_to_csv(post_df, f'{OUTPUT_PATH}/{file_name}.csv')

    return f'{OUTPUT_PATH}/{file_name}.csv'

    #upload of s3 bucket
    # upload_s3 = PythonOperator(
    #     task_id='upload_data',
    #     python_callable=upload_s3_pipeline,
    #     dag = dag
    # )
