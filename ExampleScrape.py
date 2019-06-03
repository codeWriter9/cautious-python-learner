'''
Created on 15-Jul-2018

@author: Sanjay Ghosh
'''
import sys;
import urllib.request;
from bs4 import BeautifulSoup;



def scrape_wiki(keyword):
    url = 'https://en.wikipedia.org/wiki/Anurag_Basu';
    req = urllib.request.Request(url);
    req.add_header('Accept', 'application/json, text/javascript, */*; q=0.01');
    req.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
    req.add_header('X-Requested-With', 'XMLHttpRequest');
    s = urllib.request.urlopen(req);


    soup = BeautifulSoup(s, 'html.parser');
    #print(s.read());
    #print(soup);
    print(soup.title);
    print(soup.title.name);
    print(soup.title.string);
    print(soup.title.parent.name);
    #for link in soup.find_all('a'):
    #print(link.get('href'));
    print("End of Program");




if __name__ == "__main__":

    # you can pass in a keyword to search for when you run the script
    # be default, we'll search for the "web scraping" keyword
    try:
        keyword = sys.argv[1];
    except IndexError:
        keyword = "web scraping";

    scrape_wiki(keyword);
