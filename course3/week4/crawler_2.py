import urllib.request
from bs4 import BeautifulSoup

def crawler(URL, POSITION, TURN):
    if TURN < 0: return

    print('Retrieving:', URL)

    html = urllib.request.urlopen(URL).read()
    soup = BeautifulSoup(html, 'html.parser')

    links = list()
    for link in soup('a'):
        links.append(link.get('href'))

    crawler(links[POSITION], POSITION, TURN - 1)

def init():
    PAGE_URL = input('Enter URL: ')
    COUNT = input('Enter count: ')
    POSITION = input('Enter position: ')

    COUNT = int(COUNT)
    POSITION = int(POSITION) - 1

    crawler(PAGE_URL, POSITION, COUNT)    

init()
