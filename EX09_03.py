#-*-coding:UTF-8 -*-
#  EX09_03.py
#  
#  統一發票號碼抓取範例
#  

import urllib.request
from html.parser import HTMLParser
data = urllib.request.urlopen('http://invoice.etax.nat.gov.tw') 
content = data.read().decode('utf_8')
data.close()

class myparser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.isNumber = 0 
        self.numbers = []

    def handle_data(self, data):
        if self.isNumber == 1 and self.getpos()[1]<4000:
            #print(data,"pos:",self.getpos())
            #self.numbers.append(data)
            self.numbers.extend(data.split('、'))
            self.isNumber = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'span' and attrs == [('class','t18Red')]:
            self.isNumber = 1

    def handle_endtag(self,tag):
        pass
    
Parser = myparser() 
Parser.feed(content)
print(Parser.numbers)
