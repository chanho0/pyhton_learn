from ast import UAdd
from nturl2path import url2pathname
import requests
query =input('请输入想搜索的关键词')
#url = "https://www.sogou.com/web?query="+query
url = f"https://www.sogou.com/web?query={query}"
#ua用字典
ua ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}
resp = requests.get(url, headers=ua)
print(resp.text)