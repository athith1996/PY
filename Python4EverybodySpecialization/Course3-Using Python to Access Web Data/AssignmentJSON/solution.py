import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import ssl
import xml.etree.ElementTree as ET
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1388199.json'
uh = urllib.request.urlopen(url, context=ctx)
data=uh.read().decode()

info = json.loads(data)
sum=0
for counts in info['comments']:
    sum=sum+int(counts['count'])
print(sum)
