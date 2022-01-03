import tweepy

# init
consumer_key = open(consumer_key, "r")
consumer_secret = open(consumer_secret, "r")
access_token = open(access_token, "r")
access_token_secret = open(access_token_secret, "r")

# haha oauth go brrr
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter = tweepy.API(auth)

# Ask questions
tweet = input("Enter your tweet: ")
twitter.update_status(status=tweet)