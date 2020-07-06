import urllib.request, urllib.parse
import json

def get_url(location):
    api = 'http://py4e-data.dr-chuck.net/json?'
    
    params = dict()
    params['key'] = 42
    params['address'] = location

    return api + urllib.parse.urlencode(params)

def download_document(url):
    print('Retrieving', url)

    document = urllib.request.urlopen(url).read().decode()
    document_size = str(len(document))

    print('Retrieved ' + document_size + ' characters')
    return json.loads(document)

def get_place_id(document):
    place_id = document['results'][0]['place_id']

    print('Place id', place_id)

def init():
    location = input('Enter location: ')
    url = get_url(location)
    document = download_document(url)

    get_place_id(document)    

init()