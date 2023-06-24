from schedule import every, repeat
from get_news import get_news
from write_tweet import write_tweet
from send_tweet import send_tweet


def schedule_twit_every_hour():
    news_header, news_content, news_link = get_news()
    twit = write_tweet(news_header, news_content, news_link)[0]
    
    send_tweet(twit)
    
    
if __name__ == "__main__":
    schedule_twit_every_hour()