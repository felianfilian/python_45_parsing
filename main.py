from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

article_texts = []
article_links = []

articles = soup.find_all(name="a")
for article_tag in articles:
    pass
    # print(article_tag.getText())

# get upvotes
article_upvotes = [score.getText().split()[0] for score in soup.find(name="span", class_="score")]
max_score = max(article_upvotes)
print(max_score)

print(article_upvotes)
