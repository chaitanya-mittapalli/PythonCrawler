import requests
from bs4 import BeautifulSoup

class cricket():
    def scoreFinder(self,url):
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text)
        for link in soup.findAll('div',{'class':'match-information-strip'}):
            title=link.string
            print(title)
        for link in soup.findAll('div',{'class':'team-1-name'}):
            title=link.string
            print(title)
        for link in soup.findAll('span',{'class':'innings-1-score '}):
            title=link.string
            print(title)



