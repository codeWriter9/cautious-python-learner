from bs4 import BeautifulSoup
from urllib.request import urlopen as ureq





# Wikipedia

url ="https://en.wikipedia.org/wiki/Main_Page"

#sending request to worldometer


client = ureq(url)
page= client.read()
client.close()   #connection closed


#parsing the page
page_soup = BeautifulSoup(page,'html.parser')
print(page_soup);

#getting data present in table celles
container = page_soup.findAll("td")

#geting data from the page
