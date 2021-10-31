import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1388198.xml'
uh = urllib.request.urlopen(url, context=ctx)
data=uh.read()

tree = ET.fromstring(data.decode())
counts = tree.findall('.//count')
sum=0
for x in counts:
    sum=sum+int(x.text)
print(sum)
