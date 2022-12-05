import requests
import re
from bs4 import  BeautifulSoup

link = 'https://github.com'
link2 = 'http://www.zongheng.com/'
r = requests.get(link2)
# print(r.status_code)
# print(r.content)
content = r.content
soup = BeautifulSoup(content,'html.parser')
print(soup)
