import configparser
import os

from docutils.io import Input

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

SECRET = parser.get('api_keys', 'reddit_secret_key')
CLIENT_ID = parser.get('api_keys', 'reddit_client_id')
REDDIT_USERNAME = parser.get('api_keys', 'reddit_username')
REDDIT_PASSWORD = parser.get('api_keys', 'reddit_password')

DATABASE_HOST = parser.get('database', 'database_host')
DATABASE_NAME = parser.get('database', 'database_name')
DATABASE_PORT = parser.get('database', 'database_port')
DATABASE_USER = parser.get('database', 'database_username')
DATABASE_PSWD = parser.get('database', 'database_password')

OUTPUT_PATH = parser.get('file_paths', 'output_path')
INPUT_PATH = parser.get('file_paths', 'input_path')

POST_FIELDS = (
    'id',
    'title',
    'selftext',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'upvote_ratio',
    'over_18',
    'edited',
    'spoiler'
)


