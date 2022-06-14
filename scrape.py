import requests
from bs4 import BeautifulSoup
import pandas as pd
response = requests.get(url="https://en.wikipedia.org/wiki")
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find(id="firstHeading")
print(title.string)
# Get all the links
allLinks = soup.find(id="bodyContent").find_all("a")
links=[]
for link in allLinks:
	# Use this link to scrape
	linkToScrape = link["href"]
	if linkToScrape.startswith("/wiki/"):
		links.append("https://en.wikipedia.org"+linkToScrape)
print(links)
titles=[]
for link in links:
	response = requests.get(url=link)
	soup = BeautifulSoup(response.content, 'html.parser')

	title = soup.find(id="firstHeading")
	print(title.string)
	titles.append(title.string)

articles={
	"title":titles,"link":links
}
df=pd.DataFrame(articles)
df.to_csv('articles.csv')