import tweepy
import config

auth = tweepy.OAuthHandler(config.CONSUMER_TOKEN, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
api = tweepy.API(auth)

imagePath = 'cam.jpg'
status = 'Hello',

api.update_with_media(imagePath)
