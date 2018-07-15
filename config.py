import os
from dotenv import load_dotenv;

load_dotenv()

CONSUMER_TOKEN = os.getenv('TWITTER_CONSUMER_TOKEN')
CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET')
