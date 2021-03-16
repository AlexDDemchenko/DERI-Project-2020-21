#!/usr/bin/env python
# encoding: utf-8

# tdmk2-idbased-distribution.py
# Created on 7 May 2019 at 09:52 AM
# (C) David Coffman 2019
# This code may be used only as authorized by the author.
# Adapted in part from code written by David Yanofsky in 2017 (https://gist.github.com/yanofsky/5436496).

import tweepy  # https://github.com/tweepy/tweepy
import csv
import time

# These are Twitter API keys that MUST be added. Visit developer.twitter.com to obtain these. You may want to
# consider making multiple accounts, as each account is rate-limited.
consumer_key = "UJc1xpDNnVvxjQszKR5VGjxH6"
consumer_secret = "y0ZE4PsnhCwcuSyRVVGVSWcy2S7rl4SKHywMiYK8VFUC9nv1NY"
access_key = "1142057661384581120-cWOpHesXKC8tgPsCWMm7oP7XE5VDVH"
access_secret = "ho3RAWS1l8iTcvVcCLwJFz7FKjDvLplERKrOrQdlSUD8X"





global fails, fail
fail = 0
fails = []

# Retrieves and writes tweets from users listed in the queue.txt file into csv lists.
def get_all_tweets(screen_name):
    global fails, fail
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
   
    api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
    print("Authorized.")
    

    if api.get_user(screen_name).protected == False:
        print("Attempting to access tweets from: " + screen_name)
        alltweets = []
        new_tweets = api.user_timeline(id=screen_name, count=200, tweet_mode='extended')
        alltweets.extend(new_tweets)
        #save the id of the oldest tweet less one
        try:
            oldest = alltweets[-1].id - 1
        
            #keep grabbing tweets until there are no tweets left to grab
            count = 0
            while len(alltweets) < 3200 and count < 20:
                print(count)
                print(f"getting tweets before {oldest}")
        
                #all subsiquent requests use the max_id param to prevent duplicates
                new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest,tweet_mode='extended')
        
                #save most recent tweets
                alltweets.extend(new_tweets)
        
                #update the id of the oldest tweet less one
                oldest = alltweets[-1].id - 1
                print(f"...{len(alltweets)} tweets downloaded so far")
                count+=1
        except:
            print("failed")
        if len(new_tweets) > 0:
            new_tweets = api.user_timeline(screen_name = screen_name,count=200, tweet_mode='extended')#new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)#new_tweets = api.user_timeline(id=screen_name, count=200, since_id=new_tweets[len(new_tweets) - 1].id)
        else:
            print("no new tweets")
            fails.append(screen_name)
            fail += 1
        outtweets = []
        for tweet in alltweets:
            finaltweet = [tweet.id_str, tweet.created_at, tweet.full_text]
            outtweets.append(finaltweet)
        for tweet in alltweets:
            print(tweet.id)
        with open('downloaded/%s.csv' % screen_name, 'w+',encoding="utf_8_sig") as f:
            writer = csv.writer(f)
            writer.writerows(outtweets)
        f.close()

        with open('log.txt', 'w+') as a:
            a.writelines(screen_name)
        a.close()
    else:
        fails.append(screen_name)
        fail += 1


with open('config/queue.txt', newline='\n') as inputfile:
    results = list(csv.reader(inputfile))




end = results[0] #results[len(results) - 1] #last user
print(end)
a=open("log.txt", "r")
temp_name = a.readline()
while __name__ == '__main__' and len(results) != 0: #temp_name != end:
    reqc = 60
    c = 0
    # These are Twitter API keys that MUST be added. Visit developer.twitter.com to obtain these. You may want to
    # consider making multiple accounts, as each account is rate-limited.

    for res in results:
        noFails = fail #for checking if the thing failed
        if reqc == 0:
            consumer_key = "UJc1xpDNnVvxjQszKR5VGjxH6"
            consumer_secret = "y0ZE4PsnhCwcuSyRVVGVSWcy2S7rl4SKHywMiYK8VFUC9nv1NY"
            access_key = "1142057661384581120-cWOpHesXKC8tgPsCWMm7oP7XE5VDVH"
            access_secret = "ho3RAWS1l8iTcvVcCLwJFz7FKjDvLplERKrOrQdlSUD8X"
        if reqc == 1:
            consumer_key = "BmvFr2NipfoCoH0YkhFTMCU4k"
            consumer_secret = "4hChWqJNDwTFWHlRA5i7QXD4cz72rTLPbAudXEoTbTjjDg2yOH"
            access_key = "1153349118300971009-Bgs7tD77D4JdjWEPB2mBhjfcy66c5Z"
            access_secret = "ZCCTZ7lkUoueGkhHuSNaaYzzAs11HCyVxiBT4Egl0whGw"
        if reqc == 2:
            consumer_key = "UJc1xpDNnVvxjQszKR5VGjxH6"
            consumer_secret = "y0ZE4PsnhCwcuSyRVVGVSWcy2S7rl4SKHywMiYK8VFUC9nv1NY"
            access_key = "1142057661384581120-cWOpHesXKC8tgPsCWMm7oP7XE5VDVH"
            access_secret = "ho3RAWS1l8iTcvVcCLwJFz7FKjDvLplERKrOrQdlSUD8X"
        if reqc == 3:
            consumer_key = "BmvFr2NipfoCoH0YkhFTMCU4k"
            consumer_secret = "4hChWqJNDwTFWHlRA5i7QXD4cz72rTLPbAudXEoTbTjjDg2yOH"
            access_key = "1153349118300971009-Bgs7tD77D4JdjWEPB2mBhjfcy66c5Z"
            access_secret = "ZCCTZ7lkUoueGkhHuSNaaYzzAs11HCyVxiBT4Egl0whGw"
        if reqc == 4:
            consumer_key = "UJc1xpDNnVvxjQszKR5VGjxH6"
            consumer_secret = "y0ZE4PsnhCwcuSyRVVGVSWcy2S7rl4SKHywMiYK8VFUC9nv1NY"
            access_key = "1142057661384581120-cWOpHesXKC8tgPsCWMm7oP7XE5VDVH"
            access_secret = "ho3RAWS1l8iTcvVcCLwJFz7FKjDvLplERKrOrQdlSUD8X"
        if reqc == 5:
            consumer_key = "BmvFr2NipfoCoH0YkhFTMCU4k"
            consumer_secret = "4hChWqJNDwTFWHlRA5i7QXD4cz72rTLPbAudXEoTbTjjDg2yOH"
            access_key = "1153349118300971009-Bgs7tD77D4JdjWEPB2mBhjfcy66c5Z"
            access_secret = "ZCCTZ7lkUoueGkhHuSNaaYzzAs11HCyVxiBT4Egl0whGw"
            reqc = 0

        try:
            #print(len(results))
            #print(res)
            get_all_tweets(res[0])
            c += 1
            reqc += 1
            temp_name = res
            print(results)
            if c % 10 == 0:
                print(str(c) + "/" + str(len(results)) + "; " + str(
                round(c / len(results) * 100, 2)) + "% complete. About " + str(
                round(((len(results) - c) / 68), 2)) + " minutes remaining.")
        except tweepy.error.TweepError:
            print("User does not exist.")
 #           fails.append(res)
  #          results.remove(res)
   #         fail += 1
        if fail == noFails:
            with open('log.txt', 'w+') as a:
                a.writelines(res)
            a.close()
            
            
            
a.close()
print("Done, failed users: " + str(fail)) #fails is either they do not exist or have no tweets 
print(fails)
