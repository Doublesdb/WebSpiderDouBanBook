from urllib.robotparser import RobotFileParser
import requests
import re
import time
import random

'''
robots协议
'''
UrlRobots = 'https://book.douban.com/robots.txt'

def GetRobotsTxt(url) :
    rp = RobotFileParser()
    rp.set_url(url)
    rp.read()
    print(rp.can_fetch('*', 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'))
    print(rp.can_fetch('*', 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4'))
    print(rp.can_fetch('*', 'https://book.douban.com/tag/%E6%9D%91%E4%B8%8A%E6%98%A5%E6%A0%91?start=40&type=S'))

#GetRobotsTxt(UrlRobots)

'''
爬取标签的5页内容并保存至text.txt
'''
#参数准备
Headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }

def GetOneType(UrlLabel,Headers,Num):
    for i in range(5):
        print('正在抓取' + labels[Num] +'类的第' + str(i) + '页')
        url = UrlLabel + '?start=' + str(i*20) + '&type=S'
        
        rp = requests.get(url, headers = Headers)
        #注意目标文件的编码方式要改成utf-8，而不是Unicode，否则否解码失败
        with open("HtmlCode.txt", 'w', encoding = 'utf-8') as f:
            f.write(rp.text)
        ReEx(Num)
        time.sleep(3 + random.random())

#GetOnepage(Url,Headers)

'''
正则表达式分析
'''
def ReEx(Num):
    FileName = str(labels[Num]) + '.txt'
    with open('HtmlCode.txt', 'r', encoding = 'utf-8') as file_re:
        content = file_re.read()
        STR = r'class="nbg" href="(.*?)".*?src="(.*?)".*?title="(.*?)".*?<div class="pub">\s*(.*?)\/.*?nums">(.*?)</span>.*?<p>(.*?)</p>'
        
        result = re.findall(STR, content, re.S|re.M)
        #print(result)
        
        #追加文本'a'而非覆盖文本'w'
        with open(FileName, 'a', encoding = 'utf-8') as file_result:
            file_result.write(str(result))
            #file_result.write('\n')

'''
抓取多个页面
'''
labels = ['小说', '外国文学', '文学', '随笔', '中国文学', '经典', '日本文学', '散文', '村上春树']

def GetAllPages():
    for i in range(len(labels)):
        UrlLabel = 'https://book.douban.com/tag/' + labels[i]
        GetOneType(UrlLabel,Headers,i)
    print('抓取完成')
    
GetAllPages()
