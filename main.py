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
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_upvotes)
max_score = max(article_upvotes)
max_index = article_upvotes.index(max_score)
print(max_index)
print(article_texts[max_index])
print(article_links[max_index])

print(article_upvotes)
