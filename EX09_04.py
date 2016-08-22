#-*-coding:UTF-8 -*-
#  EX09_04.py
#  
#  捷運站查詢範例
#  
import urllib.request
import urllib.parse
from html.parser import HTMLParser

agent ='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'

data = urllib.parse.urlencode({'StartStation':'977abb69-413a-4ccf-a109-0272c24fd490', 
                                'EndStation':'9c5ac6ca-ec89-48f8-aab0-41b738cb1814',
                                'SearchDate':'2016/08/19',
                                'SearchTime':'21:00',
                                'SearchWay':'DepartureInMandarin',
                                'RestTime':'',
                                'EarlyOrLater':''})
data = data.encode('utf-8')
request =urllib.request.Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult",headers={"User-Agent":agent})
response = urllib.request.urlopen(request,data)

html = response.read().decode('utf_8')

#print(html)
class myparser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        #self.isNumber = 0
        self.numbers = []
    def handle_data(self, data):
        #if self.isNumber == 1:
            print(data)
    def handle_starttag(self, tag, attrs):
        #if tag == 'font' and attrs == [('size','-1')]:
            self.isNumber = 1
    def handle_endtag(self, tag):
        #if tag == 'font' and self.isNumber == 1:
            self.isNumber = 0

Parser = myparser()
Parser.feed(html)
