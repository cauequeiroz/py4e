import urllib.request
import json

def download_document(url):
    print('Retrieving', url)

    document = urllib.request.urlopen(url).read().decode()
    document_size = str(len(document))

    print('Retrieved ' + document_size + ' characters')
    return document

def get_comments_info(document):
    comments = json.loads(document)['comments']    
    counts = [ int(comment['count']) for comment in comments ]
    
    print('Count:', len(counts))
    print('Sum:', sum(counts))

def init():
    page_url = input('Enter location: ')
    document = download_document(page_url)

    get_comments_info(document)

init()