
from bs4 import BeautifulSoup

try:
    with open("website.html") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")

soup = BeautifulSoup(content, "html.parser")

# get title text
print(soup.title.string)




