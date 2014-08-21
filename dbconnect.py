from pymongo import MongoClient
import config

def dbconnect():
    '''connect to TCH DB SERVER'''
    try:
        con = MongoClient(config.CONFIG['DBURI'])
        if con[config.CONFIG['DBNAME']].authenticate(config.CONFIG['DBUSER'], config.CONFIG['DBPWD']):
            return con[config.CONFIG['DBNAME']]
        else:
            return None
    except Exception:
        print 'Unable to connect to DB SERVER'
        return None