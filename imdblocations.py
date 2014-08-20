import requests, lxml.html,sys
'''
Extract movie shooting locations from IMDB
'''

'''lambda functions'''
cleandata = lambda x:x.strip('\n').strip()

def processhtml(raw_html):
    '''process raw_html and
       returns locations and corresponding scenes
    '''
    data = lxml.html.fromstring(raw_html)
    if data.xpath('//div[contains(@class,"soda")]'):
        locations = map(cleandata, data.xpath('//div[contains(@class,"soda")]/dt/a/text()'))
        scenes = map(cleandata, data.xpath('//div[contains(@class,"soda")]/dd/text()'))
        return locations, scenes
    else:
        return None,None

def getlocations(url):
    '''returns a dictionary of locations and scenes'''
    headers = {'User-agent':'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25'}
    try:
        raw_html = requests.get(url, headers=headers).text
        l, s = processhtml(raw_html)
        return {'location':l, 'scene':s}
    except:
        print 'Unable to fetch URL: ', url
        sys.exit(1)
    return

def constructUrl(id):
    return 'http://www.imdb.com/title/{0}/locations'.format(id)

def main():
    import pymongo, random, time
    con = pymongo.MongoClient()
    db = con['imdb']
    db2 = con['locationsdb']
    cur = db.top_100k.find().sort('votes',-1)
    for each in cur:
        res = getlocations(constructUrl(each['_id']))
        res['_id'] = each['_id']
        res['title'] = each['title']
        try:
            db2.movielocations.save(res)
        except:
            print 'Already exists'
        time.sleep(random.randrange(0,15))
    return

if __name__ == '__main__':
    main()
