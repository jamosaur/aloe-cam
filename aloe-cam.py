import config
import time
import tweet
import photo

while True:
    if photo.take_photo():
        tweet.tweet_image("photo.jpg")

    print("Sleeping for " + config.SLEEP_TIME + " seconds")
    time.sleep(float(config.SLEEP_TIME))
