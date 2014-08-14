import json
import urllib2
from bs4 import BeautifulSoup
import re

def get_quotes(name, last_page):
  show_quotes = []
  for i in range(1, last_page + 1):
    url = 'sample'
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page)
    page_quotes = soup.findAll('div', {'id':re.compile('quote_*')})
    show_quotes.extend([q.get_text() for q in page_quotes])
  return show_quotes

if __name__ == '__main__':
  all_quotes = {}
  with open('out.txt', 'w') as out:
    all_quotes['archer'] = get_quotes('archer', 23)
    json.dump(all_quotes, out)
