import sys
import json
import urllib2

URL = 'https://cdn.rawgit.com/veelenga/santa/master/happy_new_year.json'

language = sys.argv[1] if len(sys.argv) > 1 else None
codes = json.load(urllib2.urlopen(URL))
print codes.get(language, codes['eng'])
