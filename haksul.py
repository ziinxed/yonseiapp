import requests
from bs4 import BeautifulSoup

res = requests.get('https://library.yonsei.ac.kr/bbs/list/1')
soup = BeautifulSoup(res.content, 'html.parser')
print(type(soup))

noticeList = soup.select('td a')

noticeLinkList = list()

for link in noticeList:
    if 'href' in link.attrs:
        print(link.attrs['href'], type(link.attrs['href']))
        noticeLinkList.append('library.yonsei.ac.kr' + link.attrs['href'])



print(noticeLinkList)
print (type(noticeList), len(noticeList))
print (noticeList)

