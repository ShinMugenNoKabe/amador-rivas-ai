import requests
from bs4 import BeautifulSoup


def get_news():
    with open("./app/links_cache.txt", "r+") as links_cache:
        rss = requests.get("https://www.20minutos.es/rss/").content
        list_news = BeautifulSoup(rss, "lxml").find_all("item")
        
        already_tweeted_links = links_cache.readlines()
        
        for news in list_news:
            if not f"{news.find('guid').text}\n" in already_tweeted_links:
                item = news
                break

        news_link = item.find("guid").text
        news_header = item.find("description").text
        
        # Save the link in a txt file so it doesn't get tweeted again
        links_cache.write(f"{news_link}\n")

        news_request = requests.get(news_link).content
        news = BeautifulSoup(news_request, "html.parser")

        paragraphs = news.find_all("p", { "class": "paragraph" })

        news_content = "\n\n".join([paragraph.text for paragraph in paragraphs])
    
    return news_header, news_content, news_link


if __name__ == "__main__":
    print(get_news()[2])