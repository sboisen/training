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


def construct_url(bible, reference, apikey=KEY, service='biblia'):
    """Ensure BIBLE, REFERENCE, and APIKEY are properly combined and
    encoded for opening a resource via SERVICE. 

    SERVICE is either 'biblia' or 'cloud'. If biblia, format is assumed
    to be 'txt'. 
    
    Limitation: REFERENCE needs to have '+' rather than spaces, e.g. 'Mark+4:9',
    otherwise you'll get a HTTP Error. 
    """
    if service == 'biblia':
        base_url = 'http://api.biblia.com/v1/bible/content/'
        format = 'txt'
        url = base_url + bible + '.' + format
        # urllib.urlencode() does this more generally 
        return url + '?' + 'passage=' + reference + '&' + 'key=' + apikey
    elif service == 'cloud':
        # doesn't use apikey; no format involved
        base_url = 'http://app.logos.com/books/'
        url = base_url + bible + '/' + reference
    else:
        print 'Unrecognized service:', service        
    
def fetch_url(url):
    req = urllib2.urlopen(url)
    return req.read()


def print_result(reference, str, word_per_line=False):
    if word_per_line:
        for w in str.split():
            print w
    else:
        print 'Content for', reference + ':', str

# Now put it all together (for biblia)

def get_biblia_content(bible, reference, apikey=KEY, word_per_line=False):
    full_url = construct_url(bible, reference, apikey, 'biblia')
    #print 'full_url:', full_url
    result = fetch_url(full_url)
    print_result(reference, result, word_per_line)

