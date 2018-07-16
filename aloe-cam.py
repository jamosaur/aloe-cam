import config
import time
import tweet
import photo
import filesystem
import suncheck

while True:
    suncheck.check_sun()
    start = int(time.time())
    photo.take_photo()
    if filesystem.get_latest_file_number() % 36 == 0:
        photo.create_gif(filesystem.get_latest_file_number())
        tweet.tweet_image("timelapse.gif")

    end = int(time.time())

    processing_time = end - start
    sleep_time = int(config.SLEEP_TIME) - processing_time
    print("Sleeping for " + str(sleep_time) + " seconds")
    print("Processing time: " + str(processing_time))
    time.sleep(float(config.SLEEP_TIME))
