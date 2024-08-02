import tweepy
import time

auth = tweepy.OAuthHandler('z0tge5ykULTu5WXS6kg0f8rg8', 'a5SWYBwYA8bGvcC2mrtN8mySlKwRyWd40TaSoOeYbdxbs6X7RG')
auth.set_access_token('1772122381919584256-bxvrCBQTgAEqmFk1Tn1HUMG1hPL67h', 'wd990W1KbLGe6uL0q2XUOFJo9gWVWRv09MHtDoBYMm1VY')

api = tweepy.API(auth)
user = api.verify_credentials()

def limit_handle(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(300)

search_string = 'Cheta Ike-Obasi'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
	try:
		tweet.favorite()
		print('i liked that tweet')
	except tweepy.TweepyError as e:
		print(e.reason)
	except StopIteration:
		break



#Generous Bot
#for follower in limit_handler(tweepy.cursor(api.get_followers).items()):
	#if follower.name == 'Ajeasmith':
		#follower.follow()
		#break 
