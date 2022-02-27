import re
import requests
#热歌榜
url='https://music.163.com/discover/toplist?id=3778678'
UserAgent='Mozilla/5.0 (Windows NT 5.1; rv:38.0) Gecko/20100101 Firefox/38.0 SeaMonkey/2.35'
headers={
    'user-agent':UserAgent
}
response=requests.get(url=url,headers=headers)
#print(response.text)
music_html=re.findall('<a href="/song?id=(\d+)">(.*?)</a>',response.text)
print(music_html)
