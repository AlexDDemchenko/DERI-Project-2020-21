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
CONSUMER_KEY = "UJc1xpDNnVvxjQszKR5VGjxH6"
CONSUMER_SECRET ="y0ZE4PsnhCwcuSyRVVGVSWcy2S7rl4SKHywMiYK8VFUC9nv1NY"
ACCESS_TOKEN = "1142057661384581120-cWOpHesXKC8tgPsCWMm7oP7XE5VDVH"
ACCESS_TOKEN_SECRET = "ho3RAWS1l8iTcvVcCLwJFz7FKjDvLplERKrOrQdlSUD8X"
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
