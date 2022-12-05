import re
from bs4 import BeautifulSoup
import requests
#复杂一点
url=''
response = requests.get(url)
soup = BeautifulSoup(response,'html.parser')
# negex = re.compile()
soup.find(negex)
soup.find_all(negex)

#exercise
下载徐文兵梁冬音频 url在收藏夹里
