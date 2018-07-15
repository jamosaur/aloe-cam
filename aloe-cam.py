import config
import time
import tweet
import photo

while True:
    if photo.take_photo():
        #tweet.tweet_image('photo.jpg')

    time.sleep(float(config.SLEEP_TIME))
