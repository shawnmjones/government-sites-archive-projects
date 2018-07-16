import sys

from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

import requests
import requests_cache

cachefile = "summaries"
requests_cache.install_cache(cachefile)

root_url = sys.argv[1]

nextpageurl = root_url

while nextpageurl is not None:

    r = requests.get(nextpageurl)
    
    soup = BeautifulSoup(r.text, 'html5lib')

    for link in soup.findAll('a'):
        thislink = link.get('href')
        thisurl = urljoin(root_url, thislink)
        print(thisurl)

    nextpageurl = None

    for item in soup.findAll('li', {'class': 'next'}):
    
        for anchor in item.findAll('a'):
            nextpageurl = anchor.get('href')
            nextpageurl = urljoin(root_url, nextpageurl)
            print("NEXT PAGE: {}".format(nextpageurl))
