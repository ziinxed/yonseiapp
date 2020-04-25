import requests
from bs4 import BeautifulSoup

res = requests.get('https://library.yonsei.ac.kr/bbs/list/1')
soup = BeautifulSoup(res.content, 'html.parser')
print(type(soup))

noticeList = soup.select('td a')

noticeLinkList = list()
f = open("listFile.txt", 'w')


for link in noticeList:
    if 'href' in link.attrs:
        #print(link.attrs['href'], type(link.attrs['href']))
        listLink = 'library.yonsei.ac.kr' + link.attrs['href']
        noticeLinkList.append(listLink)
        f.write(listLink + "\n")

f.close()

for link in noticeLinkList:
    print(link)



#print(noticeLinkList)
#print (type(noticeList), len(noticeList))
#print (noticeList)

