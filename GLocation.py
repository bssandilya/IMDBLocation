'''
Get latitude longitude from address using google API
'''
import requests
import sys
from pprint import pprint

def getlatlong(address):
    '''
    returns lat and long from address
    '''
    apikey = 'AIzaSyD3ojJrvbxvEikhBiLjMAOpPME1piNzCyM'
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    payload = {'key':apikey}
    payload['address'] = address
    try:
        return requests.get(url, params=payload).json()
    except Exception:
        print sys.exc_info()[0]

def test():
    ADD = '175 S San Antonio Rd, Los Altos, CA, USA'
    pprint(getlatlong(ADD))
    return

if __name__ == '__main__':
    test()
