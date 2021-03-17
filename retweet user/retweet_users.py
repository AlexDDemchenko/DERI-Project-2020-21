import tweepy
from tweepy import OAuthHandler
import numpy as np
import secrets
import tweepy
import pandas as pd
import os
import cv2
import io
import requests
with open(r'C:\Users\Administrator\Desktop\DERI\retweet user\input.txt', 'r') as f:
    ID = f.read()
    f.close()
CONSUMER_KEY = ""
CONSUMER_SECRET =""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
# the ID of the tweet 
IDS = ID.split()

for ID in IDS:
    try:
        # getting the retweeters
        retweets_list = api.retweets(ID, 100) 
        # printing the screen names of the retweeters 
        for retweet in retweets_list:
            print(retweet.user.screen_name)
    except tweepy.RateLimitError:
            print("Rate limit reached: waiting 15 min")
            time.sleep(15 * 60)
    except:
        print("Tweet does not exist")
        pass
