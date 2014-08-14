from bs4 import BeautifulSoup
import json
import os
import re
import urllib2

IN_PATH = 'tmp/quotes.txt'
OUT_PATH = 'tmp/quotes_out.txt'

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
  with open(IN_PATH, 'r') as input, open(OUT_PATH, 'w') as out:
    all_quotes = {}
    dict = json.load(input)
    shows = [
        ('archer', 23),
        ('arrested-development', 12),
        ('30-rock', 18)]
    for show in shows:
      if show[0] in dict.keys():
        all_quotes[show[0]] = dict[show[0]]
      else:
        all_quotes[show[0]] = get_quotes(show[0], show[1])

    json.dump(all_quotes, out)
  os.rename(OUT_PATH, IN_PATH)
