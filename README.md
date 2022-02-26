---
categories:
  - 知识积累
author: JeffreyLove
copyright: true
date: '2022/2/26 11:30:00'
description: 一个简单的爬虫程序
tags:
  - python
  - 爬虫
---

# A crawler program written in python that uses the BeautifulSoup framework  

**使用python的BeautifulSoup框架来编写的爬虫程序**  

程序包含了爬虫代理的使用，网页源代码中标签的提取，图片保存，文件夹的创建等。  

就拿下面这个网站来做实验:smile:  
~~学会了可以去爬一些美女图片网站（bushi~~  
[4399动漫网][http://www.4399dmw.com/search/dh-9-0-0-0-0-1-0/]  

<img src="https://github.com/Jeffrey-love/Crawler/blob/main/picture/3.jpg" width = "500" height = "300" alt="" align=center />

既然我们要爬取图片，那就要利用浏览器自带的*检查*功能，先找到图片在哪个标签内  
如下图：  
<img src="https://github.com/Jeffrey-love/Crawler/blob/main/picture/4.jpg" width = "500" height = "300" alt="" align=center />  

还是比较容易定位到的，这样我们就可以先用`list = soup.find('div',class_='lst').find_all('a',class_='u-card')`把包含img标签的a标签先筛选出来,  
然后用`item.find('img').get('data-src')`将图片链接进行提取，这样一来就有了爬虫的主程序[^3]:smile_cat:
[^3]:完整代码见文件BeautifulSoup.py,含详细注释
  

```python
    url = "http://www.4399dmw.com/search/dh-9-0-0-0-0-{}-0/".format(page)
    resp = requests.get(url=url,headers=headers,proxies=proxies)
    html_doc = resp.content.decode("utf-8")
    soup = BeautifulSoup(html_doc,'lxml')
    # 把所有class值为lst的div标签取出来
    list = soup.find('div',class_='lst').find_all('a',class_='u-card')
    pic_urls = []
    for item in list:
        # 提取图片链接
        pic_url = item.find('img').get('data-src')
        pic_urls.append(pic_url)

    for tar,url in enumerate(pic_urls):
        # 因为url的格式是“//xxx.com/xxxx.img”，前面少了协议，所以要加上
        urln = "http:"+url
        save_img(urln,tar)
```
---

运行程序之后可以见到：  
<img src="https://github.com/Jeffrey-love/Crawler/blob/main/picture/5.jpg" width = "400" height = "300" alt="" align=center />  

运行成功，我们去文件夹里看看效果  
![1](https://github.com/Jeffrey-love/Crawler/blob/main/picture/1.jpg)  
向柯南致敬！！！  :smile:  
<img src="https://github.com/Jeffrey-love/Crawler/blob/main/picture/2.jpg" width = "450" height = "300" alt="" align=center />  
