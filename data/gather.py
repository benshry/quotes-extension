import json
import urllib2
from bs4 import BeautifulSoup
import re

if __name__ == '__main__':
  all_quotes = []

  with open('out.txt', 'w') as out:

    for i in range(1, 24):
      url = 'sample_url'
      page = urllib2.urlopen(url).read()
      soup = BeautifulSoup(page)
      page_quotes = soup.findAll('div', {'id':re.compile('quote_*')})
      all_quotes.extend([q.get_text() for q in page_quotes])

    json.dumps({'archer':all_quotes})
    json.dump({'archer':all_quotes}, out)
