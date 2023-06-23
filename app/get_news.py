import requests
from bs4 import BeautifulSoup


def get_news():
    rss = requests.get("https://www.20minutos.es/rss/").content
    list_news = BeautifulSoup(rss, "lxml")

    news_header = list_news.find("description").text
    news_link = list_news.find("guid").text

    news_request = requests.get(news_link).content
    news = BeautifulSoup(news_request, "html.parser")

    paragraphs = news.find_all("p", { "class": "paragraph" })

    news_content = "\n\n".join([paragraph.text for paragraph in paragraphs])
    
    return news_header, news_content, news_link


if __name__ == "__main__":
    print(get_news())