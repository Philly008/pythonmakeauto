'''
Created on 2017年1月4日

@author: admin
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
text = urlopen('http://www.python.org/community/jobs').read()
soup = BeautifulSoup(text, "html.parser")

jobs = set()
for header in soup('h3'):
    links = header('a', 'reference')
    if not links: continue
    link = links[0]
    jobs.add('%s (%s)' % (link.string, link['href']))
print('\n'.join(sorted(jobs, key=lambda s: s.lower())))




