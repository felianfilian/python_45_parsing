from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

article_texts = []
article_links = []

articles = soup.find_all(name="a")
for article_tag in articles:
    print(article_tag.getText())

# get upvotes
article_upvotes = [score.getText() for score in soup.find(name="span", class_="score")]
print(article_upvotes)
