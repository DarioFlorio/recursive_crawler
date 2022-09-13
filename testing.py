import requests
from bs4 import BeautifulSoup
import re
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
###########################################################################################

url_list=["https://www.styliafoe.com/en/homepage"]
domain = "styliafoe.com"


def writetofile(thelist):
# open file in write mode
    with open(r'urls.txt', 'w') as fp:
        for item in thelist:
        # write each item on a new line
            fp.write("%s\n" % item)
            print('Done') 
 
def crawl(url_list, domain):
    for url in url_list:       
        validate = URLValidator()
        try:
            #print(self._url)
            validate(url)
            #print("String is a valid URL")
            #self.scrape_links(self.urls)
            try:
                reqs = requests.get(url)
                #print("URL is valid and exists on the internet")
                if domain in url:
            #url = 'https://www.geeksforgeeks.org/'
                    soup = BeautifulSoup(reqs.text, 'html.parser')
                    urls = []
                    for link in soup.find_all('a'):
                        print(link.get('href'))
                        url = link.get('href')
                        if url not in url_list:
                            url_list.append(url)
                print(url_list)
                writetofile(url_list)
            except requests.ConnectionError as exception:
                print("URL does not exist on Internet")
        except ValidationError as exception:
            print("String is not valid URL")  
            
        
###########################################################################################
          
    
    
    
    
crawl(url_list, domain)



 
 

