#!/usr/bin/env python3

import configparser

global AT
global ATS
global CAK
global CASK

config = configparser.ConfigParser()
config.read("config.ini")
config.sections()
config.get("DEFAULTS", "", fallback=False)

tweet = config.get("DEFAULTS", "tweet", fallback=False)
print(tweet)

if tweet:
    twitter_api = configparser.ConfigParser()
    twitter_api.read("twitter.ini")
    twitter_api.sections()
    twitter_api.get("twitter", "", fallback=0)
    AT = twitter_api.get("twitter", "access_token")
    ATS = twitter_api.get("twitter", "access_token_secret")
    CAK = twitter_api.get("twitter", "consumer_api_key")
    CASK = twitter_api.get("twitter", "consumer_api_secret_key")
else:
    config = configparser.ConfigParser()
    config.read("config.ini")
    config.sections()
    config.get("DEFAULTS", "", fallback=False)

    AT = config.get("DEFAULTS", "tweet", fallback=False)
    ATS = config.get("DEFAULTS", "tweet", fallback=False)
    CAK = config.get("DEFAULTS", "tweet", fallback=False)
    CASK = config.get("DEFAULTS", "tweet", fallback=False)
