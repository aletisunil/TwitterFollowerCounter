import tweepy
import logging
from os import environ

logger = logging.getLogger()


def create_api():
    consumer_key = environ['CONSUMER_KEY']
    consumer_secret =  environ['CONSUMER_SECRET']
    access_token =  environ["ACCESS_TOKEN"]
    access_token_secret =environ["ACCESS_TOKEN_SECRET"]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error('Error creating API', exc_info=True)
        raise e
    logger.info('API created')
    return api