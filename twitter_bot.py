import tweepy
import schedule
import time
import os
from dotenv import load_dotenv
import datetime
import sys
import locale 

#Set default encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')
locale.getpreferredencoding = lambda: 'UTF-8'

# Load environment variables from .env file
load_dotenv("api_creds.env")

print("Consumer Key:", os.getenv("CONSUMER_KEY"))  # Should not be None
print("Consumer Secret:", os.getenv("CONSUMER_SECRET"))
print("Access Key:", os.getenv("ACCESS_KEY"))
print("Access Secret:", os.getenv("ACCESS_SECRET"))
print("Bearer Token:", os.getenv("BEARER_TOKEN"))


# Twitter API credentials
bearer_token = os.getenv("BEARER_TOKEN")
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_key = os.getenv('ACCESS_KEY')
access_secret = os.getenv('ACCESS_SECRET')

print(consumer_key, consumer_secret, access_key, access_secret)

# Authenticate using Tweepy V2 Client
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_key,
    access_token_secret=access_secret
)


# Define a function to tweet using API V2
def tweet():
    try:
        # get current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tweet_text = f"Hello, world! 🌍👋🕒 {timestamp}"

        response = client.create_tweet(text=tweet_text)
        print(f"✅ Tweet posted successfully! Tweet ID: {response.data['id']}".encode("utf-8").decode("utf-8"))
    except tweepy.TweepyException as e:
        print(f"❌ Error: {e}")

# Schedule the tweet to be sent every 10 seconds
schedule.every(10).seconds.do(tweet)

# Loop to keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)


#The script above uses the `tweepy` library to interact with the Twitter API. The `tweet()` function sends a tweet with the message "Hello, world!". The `schedule` library is used to schedule the tweet to be sent every 10 seconds. The script then enters a loop that runs the scheduled tasks and sleeps for 1 second before checking for new tasks. This allows the script to continuously send tweets at the scheduled intervals.

#To run this script, you will need to replace the placeholder values for the Twitter API credentials with your own. You can obtain these credentials by creating a Twitter Developer account and creating a new app to generate the necessary keys and tokens.

#.errors.TweepyException