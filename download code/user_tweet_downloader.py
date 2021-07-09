import tweepy #https://github.com/tweepy/tweepy
import csv
import time

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method

	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#initialize a list to hold all the tweepy Tweets
	alltweets = []

	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200, tweet_mode='extended')

	#save most recent tweets
	alltweets.extend(new_tweets)

	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1

	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print ("getting tweets before %s" % (oldest))

		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest,tweet_mode='extended')

		#save most recent tweets
		alltweets.extend(new_tweets)

		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1

		print ("...%s tweets downloaded so far" % (len(alltweets)))

	#transform the tweepy tweets into a 2D array that will populate the csv
	outtweets = [[screen_name, tweet.id_str, tweet.created_at, tweet.full_text] for tweet in alltweets]

	#write the csv
	with open('mega.csv','w') as f:
		writer = csv.writer(f)
		writer.writerow(["name", "id","created_at","text"])
		writer.writerows(outtweets)

	pass


get_all_tweets ("value")
get_all_tweets ("muratpak")
get_all_tweets ("jackbutcher")
get_all_tweets ("naval")
get_all_tweets ("metaprophet")
