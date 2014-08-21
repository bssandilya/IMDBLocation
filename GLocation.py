'''
Get latitude longitude from address using google API
'''
import requests
import sys
from pprint import pprint
import config

def getlatlong(address):
    '''
    returns lat and long from address
    '''

    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    payload = {'key':config.CONFIG['apikey']}
    payload['address'] = address

    try:
        return requests.get(url, params=payload).json()
    except Exception:
        print sys.exc_info()[0]
        return None

def test():
    '''sample test function'''

    ADD = 'Hatley Castle, Royal Roads, Colwood, British Columbia, Canada'
    pprint(getlatlong(ADD)['results'][0]['geometry']['location'])
    return

if __name__ == '__main__':
    test()
