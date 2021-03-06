import os
from dotenv import load_dotenv

load_dotenv(verbose=True, dotenv_path=".env")

TWITTER_ENABLED = os.getenv('TWITTER_ENABLED')
S3_ENABLED = os.getenv('S3_UPLOAD_ENABLED')
LOCAL_STORE_ENABLED = os.getenv('LOCAL_STORE_ENABLED')

LAT = os.getenv('LAT')
LNG = os.getenv('LNG')

WIDTH = os.getenv('PHOTO_WIDTH')
HEIGHT = os.getenv('PHOTO_HEIGHT')
SLEEP_TIME = os.getenv('TIME_BETWEEN_PHOTOS')

CONSUMER_TOKEN = os.getenv('TWITTER_CONSUMER_TOKEN')
CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET')

LOCAL_STORAGE_LOCATION = os.getenv('LOCAL_STORAGE_LOCATION')

if __name__ == '__main__':
    print(LOCAL_STORAGE_LOCATION)
