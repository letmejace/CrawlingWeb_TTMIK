from bs4 import BeautifulSoup
from urllib.request import urlopen

# 네이버 실시간 검색어 ( 분야별 : 도서 )
response = urlopen('https://datalab.naver.com/')
soup = BeautifulSoup(response, 'html.parser')

i = 1
for anchor in soup.select('span.title'):
    print(str(i) + "위 : " + anchor.get_text())
    i = i + 1
