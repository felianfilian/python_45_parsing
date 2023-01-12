
from bs4 import BeautifulSoup

try:
    with open("website.html") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")

soup = BeautifulSoup()




