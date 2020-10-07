import requests
from bs4 import BeautifulSoup
url = input("Enter the website which you want to scrape: ")

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

print(soup.prettify())	# to print html in tree structure
