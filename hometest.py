import urllib.request as request
from bs4 import BeautifulSoup as bs
from pyquery import PyQuery as pq
import asyncio
import aiohttp

@asyncio.coroutine
async def getPage(url,res_list):
    print(url)
    headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'}
    #conn = aiohttp.ProxyConnector(proxy="http://127.0.0.1:8087")
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as resp:
            assert resp.status==200
            res_list.append(await resp.text())


class parseListPage():
    def __init__(self,page_str):
        self.page_str = page_str
    def __enter__(self):
        page_str = self.page_str
        page = pq(page_str)
        # 获取标题链接
        articles = doc('.article_list ul li').items()
        art_urls = []
        for a in articles:
            x = a.find('a')['href']
            art_urls.append(x)
        return art_urls
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


page_num = 10
page_urls = 'http://news.ncu.edu.cn/html/mtjj/index.html'
loop = asyncio.get_event_loop()
ret_list = []
tasks = [getPage(host,ret_list) for host in page_urls]
loop.run_until_complete(asyncio.wait(tasks))

articles_url = []
for ret in ret_list:
    with parseListPage(ret) as tmp:
        articles_url += tmp
ret_list = []

tasks = [getPage(url, ret_list) for url in articles_url]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
