import requests

my_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
postdata = {'StartStation':'977abb69-413a-4ccf-a109-0272c24fd490',
                               'EndStation':'f2519629-5973-4d08-913b-479cce78a356',
                               'SearchDate':'2016/08/20',
                               'SearchTime':'08:00',
                               'SearchWay':'DepartureInMandarin',
                               'RestTime':'',
                               'EarlyOrLater':''}
url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"
req = requests.post(url,data=postdata, headers=my_agent)
print(req.text)