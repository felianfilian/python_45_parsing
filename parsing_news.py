from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

article_texts = []
article_links = []

articles = soup.find_all(name="a")
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

# get upvotes
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

max_score = max(article_upvotes)
max_index = article_upvotes.index(max_score)

print(article_texts[max_index])
print(article_links[max_index])

