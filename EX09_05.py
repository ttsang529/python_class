import urllib.request
import urllib.parse
from html.parser import HTMLParser

agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
data = urllib.parse.urlencode({'StartStation':'977abb69-413a-4ccf-a109-0272c24fd490',
                               'EndStation':'f2519629-5973-4d08-913b-479cce78a356',
                               'SearchDate':'2016/08/20',
                               'SearchTime':'08:00',
                               'SearchWay':'DepartureInMandarin',
                               'RestTime':'',
                               'EarlyOrLater':''})
data = data.encode('utf-8')
request = urllib.request.Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult",headers={'User-Agent':agent})
response = urllib.request.urlopen(request,data)
html = response.read().decode('utf_8')
print(html)