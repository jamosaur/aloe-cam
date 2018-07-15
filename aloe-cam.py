import config
import time
import tweet
import photo

while True:
    start = int(time.time())
    if photo.take_photo():
        tweet.tweet_image("photo.jpg")

    end = int(time.time())

    processing_time = end - start
    sleep_time = int(config.SLEEP_TIME) - processing_time
    print("Sleeping for " + str(sleep_time) + " seconds")
    print("Processing time: " + str(processing_time))
    time.sleep(float(config.SLEEP_TIME))
