#!/usr/bin/env python3
from configs import DATA_LOGGER
import os
from logger import logger

# twitter api
global TWEET
TWEET = False
global TWITTER_CONFIG
TWITTER_CONFIG = str('twitter_access_tokens')
global ACCESS_TOKEN_SECRET
global ATS
ACCESS_TOKEN_SECRET = os.path.expanduser(
    os.getcwd() + '/' + TWITTER_CONFIG + '/access_token_secret.txt')
global ACCESS_TOKEN
global AT
ACCESS_TOKEN = os.path.expanduser(
    os.getcwd() + '/' + TWITTER_CONFIG + '/access_token.txt')
global CONSUMER_API_KEY
global CAK
CONSUMER_API_KEY = os.path.expanduser(
    os.getcwd() + '/' + TWITTER_CONFIG + '/consumer_api_key.txt')
global CONSUMER_API_SECRET_KEY
global CASK
CONSUMER_API_SECRET_KEY = os.path.expanduser(
    os.getcwd() + '/' + TWITTER_CONFIG + '/consumer_api_secret_key.txt')


def get_data(filename):
    f = open(filename, "r")
    DATA = str(f.read())
    f.close()
    if (DATA_LOGGER):
        logger.info(DATA)  # unsecure
    return DATA


CAK = get_data(CONSUMER_API_KEY)
CASK = get_data(CONSUMER_API_SECRET_KEY)
AT = get_data(ACCESS_TOKEN)
ATS = get_data(ACCESS_TOKEN_SECRET)
