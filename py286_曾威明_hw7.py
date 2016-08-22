import requests
import sys
from bs4 import BeautifulSoup


def paser_yahoo_movie_info(url):
    filename='5852.txt'
    orig_stdout = sys.stdout
    f = open(filename, 'w')
    sys.stdout = f

    req = requests.get(url)
    bs = BeautifulSoup(req.text,"html.parser")
    for i in bs.find_all('span',{'class':['tit','dta']}):
        if (str(type(i.string)).find('NoneType')==-1):
            print (i.string)
        else:
            for a in i.findAll('a', href=True):
                print(a.string)

    sys.stdout = orig_stdout
    f.close()

if __name__ == '__main__':
    url='https://tw.movies.yahoo.com/movieinfo_main.html/id=5852'
    paser_yahoo_movie_info(url)