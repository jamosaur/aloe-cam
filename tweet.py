import config
import tweepy
import datetime


def tweet_image(image_path=None):
    if config.TWITTER_ENABLED:
        if image_path:
            try:
                auth = tweepy.OAuthHandler(config.CONSUMER_TOKEN, config.CONSUMER_SECRET)
                auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
                api = tweepy.API(auth)
                current_time = datetime.datetime.now()
                status = current_time.strftime("%c") + " #aloe #aloevera #timelapse #grow #growcam"
                api.update_with_media(image_path, status)
                print("Tweeted!")
            except:
                print('Failed to tweet...')
                pass