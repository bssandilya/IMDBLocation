from pymongo import MongoClient
import GLocation
import config
from dbconnect import dbconnect

def fetchLatLong():
    db = dbconnect()
    for each in db.movielocations.find():
        if each['location']:
            for eachlocation in each['location']:
                res = GLocation.getlatlong(eachlocation)
                lat_lon = dict(res['results'][0]['geometry']['location'])
                record = {'mid':each['_id'], 'title':each['title']}
                record.update(lat_lon)
                print record
                raw_input()
    return

if __name__ == '__main__':
    fetchLatLong()