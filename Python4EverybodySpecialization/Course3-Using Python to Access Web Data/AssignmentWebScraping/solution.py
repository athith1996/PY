from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Kimmie.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count=7
position=18
x=0
names=list()

while x<count:
    tags=soup('a')
    name=tags[position-1].contents[0]
    names.append(name)
    url=tags[position-1].get('href')
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    x=x+1
print(names[count-1])
