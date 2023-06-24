import tweepy
import os
from dotenv import load_dotenv
import logging

load_dotenv()


def send_tweet(message: str):
    client = tweepy.Client(
        consumer_key= os.getenv("TWITTER_API_KEY"),
        consumer_secret=os.getenv("TWITTER_API_KEY_SECRET"),
        access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
        access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    )
    
    try:
        print(message)
        client.create_tweet(text=message)
        print("Tweeted")
    except Exception as e:
        logging.error(f"UNEXPECTED ERROR: {e}")
    
    
if __name__ == "__main__":
    send_tweet("Test API Twitter")