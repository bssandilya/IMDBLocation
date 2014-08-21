'''
Get latitude longitude from address using google API
'''

from pprint import pprint
import requests
import sys
import config

def getlatlong(address):
    '''returns lat and long from address
    '''

    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    payload = {'key':config.CONFIG['apikey']}
    payload['address'] = address

    try:
        r = requests.get(url, params=payload)
        if r.status_code == 200 and r.json().get('results'):
            return r.json()['results'][0]['geometry']['location']
        else:
            return None

    except Exception:
        print sys.exc_info()[0]
        return None
