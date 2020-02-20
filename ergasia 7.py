#Για να τρέξει πράγραμμα πρέπει να κατεβάσετε την βηβλιοθήκη tweepy
import tweepy



def count_words_in_50_last_tweets(username):
	consumer_key = 'lVRVgyDcySzumCjFZd9lBalfz'
	consumer_secret = 'vfxRlMMuieQNtgf0G8ECsyuMWt1a3XqYCVSwkX5mejjzm6CvdH'
	access_token = '1015577769168769024-XTFzEXXgVHSMfNHCeyl9g5OfmPcrW6'
	access_secret = 'gVR9bOWNfOAaBtR4Xgvj6LLhZ81V1gQAEYKngGwAOGoDg'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)

	# count tweet
	tweets_words_num = 0
	try: 
		# Pulling individual tweets from query
		for tweet in api.user_timeline(username, count=50):
			# Adding number of words per tweet
			tweets_words_num += len(tweet.text.split())
  		
	except BaseException as e:
		print('failed on_status,',str(e))
		return -1

	return tweets_words_num

  '''Example usernames  kvlly  EmmaBostian'''
while 1:
	first_username = input("Please enter a tweeter Username:\n")
	first_tweet_words_num = count_words_in_50_last_tweets(first_username)
	if first_tweet_words_num != -1:
		second_username = input("Please enter another tweeter User name:\n")
		second_tweet_words_num = count_words_in_50_last_tweets(second_username)
		if second_tweet_words_num != -1:
			if first_tweet_words_num > second_tweet_words_num:
				print("User",first_username,"has more tweet words (",first_tweet_words_num,") than User",second_username,"! (",second_tweet_words_num,")\n\n")
			elif first_tweet_words_num < second_tweet_words_num:
				print("User",second_username,"has more tweet words (",second_tweet_words_num,") than User",first_username,"! (",first_tweet_words_num,")\n\n")
			else:
				print("Both Users have the same tweet words! (",first_tweet_words_num,")")

		else:
			print("An Error has Occured. Please enter the tweeter usernames again...\n\n")

	else:
		print("An Error has Occured. Please enter the tweeter usernames again...\n\n")



 