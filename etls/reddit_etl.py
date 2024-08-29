import sys
import praw
from airflow.utils.log.logging_mixin import LoggingMixin
from markdown_it.parser_block import LOGGER
from praw import Reddit
import pprint

from utils.constants import POST_FIELDS

logger = LoggingMixin().log


# username="armaan675",
# password="c8aZW$ed6AdtnX8",
def connect_reddit(client_id, client_secret, user_agent, username, password) -> Reddit:
    try:
        reddit = praw.Reddit(
                             client_id=client_id,
                             client_secret=client_secret,
                             user_agent=user_agent,
                             username=username,
                             password=password
        )
        logger.info(reddit.user.me())
        return reddit
    except Exception as e:
        print(e)
        sys.exit(1)

def extract_posts(reddit_instance: Reddit, subreddit: str, time_filter: str, limit=None):
    subreddit = reddit_instance.subreddit("UofT")
    posts = subreddit.top(time_filter=time_filter, limit=limit)

    #
    post_list = []

    for post in posts:
        post_dict = vars(post)
        post = {key: post_dict[key] for key in POST_FIELDS}
        post_list.append(post)

    return post_list