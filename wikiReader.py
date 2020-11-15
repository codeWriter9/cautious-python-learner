from bs4 import BeautifulSoup
from urllib.request import urlopen as ureq
import sys


# Wikipedia
url ="https://en.wikipedia.org/wiki/Main_Page"

#sending request to wikipedia


client = ureq(url)
page= client.read()
client.close()   #connection closed


#parsing the page
page_soup = BeautifulSoup(page,'html.parser')
_page_str_ = page_soup.__str__();
print(len(_page_str_));
count = 0;
final_str = '';
for c in _page_str_:
    try :
        print(c);
        final_str = final_str + c;
    except UnicodeEncodeError:
        print(" Cannot Print this  ");
    count = count + 1;
print(final_str);