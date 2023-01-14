from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

print(soup.title)

# article_tag = soup.find(name="a", class_="storylink")
# article_text = article_tag.getText()
# print(article_text)

