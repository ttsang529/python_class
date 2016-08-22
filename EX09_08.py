import requests
from bs4 import BeautifulSoup
req = requests.get('http://invoice.etax.nat.gov.tw')
bs = BeautifulSoup(req.text,"html.parser")
for i in bs.find_all('span',{'class':'t18Red'}):
    print(i.string)