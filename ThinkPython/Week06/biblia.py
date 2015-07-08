"""Client for Biblia API

You need an API key to use this code. 

>>> import biblia
# note you need to replace spaces with '+' in the passage reference for this version
>>> biblia.get_biblia_content('LEB', 'txt', 'Mark+4:9')
Content for Mark 4:9: And he said, "Whoever has ears to hear, let him hear!"
"""

# standard Python module for opening URLs
import urllib2

# my key is in key.py as
# KEY = 'abcdefghi'
from key import KEY

def construct_base_url(bible, format):
    """Return the base URL for BIBLE and FORMAT. 
    BIBLE is 'KJV' or 'LEB'
    FORMAT is 'xml' or 'json' or 'txt'
    """
    base_url = 'http://api.biblia.com/v1/bible/content/'
    url = base_url + bible + '.' + format
    return url

def construct_url(base_url, passage, apikey=KEY):
    """Ensure URL, PASSAGE, and APIKEY are properly combined and
    encoded for opening a resource. Assumes the Bible version and
    return type are already in URL.
    
    Limitation: PASSAGE needs to have '+' rather than spaces, e.g. 'Mark+4:9',
    otherwise you'll get a HTTP Error. 
    """
    # urllib.urlencode() does this more generally 
    return base_url + '?' + 'passage=' + passage + '&' + 'key=' + apikey
    
def fetch_url(url):
    req = urllib2.urlopen(url)
    return req.read()

def print_result(passage, str):
    print 'Content for', passage + ':', str

# Now put it all together

def get_biblia_content(bible, format, passage, apikey=KEY):
    base = construct_base_url(bible, format)
    full_url = construct_url(base, passage, apikey)
    #print 'full_url:', full_url
    result = fetch_url(full_url)
    print_result(passage, result)
