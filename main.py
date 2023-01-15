from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

print(soup.title)

article_upvote = soup.find(name="span", class_="score").getText()
print(article_upvote)

