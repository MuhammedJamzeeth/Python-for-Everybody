# Retrieve all the anchor tags
# tags = soup('a')
# for tag in tags:
#    # Look at the parts of a tag
#    print 'TAG:',tag
#    print 'URL:',tag.get('href', None)
#    print 'Contents:',tag.contents[0]
#    print 'Attrs:',tag.attrs

import ssl
import urllib.request

from bs4 import BeautifulSoup

# Ignore SSl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1867520.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags[
tot = 0
tags = soup('span')
for tag in tags:
    n = int(tag.contents[0])
    tot = tot + n

print(tot)
