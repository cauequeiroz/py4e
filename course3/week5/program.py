import urllib.request
import xml.etree.ElementTree as ET

def download_page(url):
    print('Retrieving', url)

    page = urllib.request.urlopen(url).read().decode()
    page_size = str(len(page))

    print('Retrieved ' + page_size + ' characters')
    return page

def get_comments_info(document):
    xml = ET.fromstring(document)
    counts = [int(count.text) for count in xml.findall('comments/comment/count')]

    print('Count:', len(counts))
    print('Sum:', sum(counts))

def init():
    page_url = input('Enter location: ')
    document = download_page(page_url)

    get_comments_info(document)

init()