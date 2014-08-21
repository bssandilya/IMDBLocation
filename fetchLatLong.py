from pymongo import MongoClient
import GLocation
import config
from dbconnect import dbconnect

def fetchLatLong():
    db = dbconnect()
    for l in db.movielocations.aggregate([{"$unwind":"$location"}])["result"]:
        print l['_id'], l['title'], l['location'], GLocation.getlatlong(l['location'])
        raw_input()

if __name__ == '__main__':
    fetchLatLong()