
from bs4 import BeautifulSoup

try:
    with open("website.html") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")

soup = BeautifulSoup(content, "html.parser")

# get title text
print(soup.title.string)

all_a = soup.find_all("a")
print(all_a)

heading = soup.find(name="h1", id="name")
print(heading.text)

select03 = soup.select(selector="#name")
print(select03)

select04 = soup.select(selector=".heading")
print(select04)
