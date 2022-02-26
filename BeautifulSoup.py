#！ /user/bin.python
# -*- coding:UTF-8 -*-
import os
import requests
from bs4 import BeautifulSoup

# 请求头
headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Referer":"http://www.4399dmw.com/donghua/"
    }
# 使用了一个代理去爬取
proxies = {"HTTP":"http://121.13.252.58:41564"}

# 创建保存路径
def mk_dir(path):
    # os.path.exists(name)判断是否存在路径
    # os.path.join(path, name)连接目录与文件名
    isExist = os.path.exists(os.path.join('C:\pythonProject\python\pachong\dongman',path))
    if not isExist:
        print("mkdir "+path)
        # 创建文件夹
        os.mkdir(os.path.join('C:\pythonProject\python\pachong\dongman',path))
        # 将路径转移到新建文件夹中，这样保存的图片就在这里
        os.chdir(os.path.join('C:\pythonProject\python\pachong\dongman',path))
        return True
    else:
        print(path+" already exists")
        os.chdir(os.path.join('C:\pythonProject\python\pachong\dongman', path))
        return False

# 下载的图片
def save_img(img_src,img_tar):
    try:
        img = requests.get(img_src,headers=headers,proxies=proxies)
        img_name = "img_tar_{}.jpg".format(img_tar+1)
        with open(img_name,'ab') as f:
            f.write(img.content)
            print(img_name)
    except Exception as e:
        print(e)

# 主要爬取代码
def pachong(page):
    url = "http://www.4399dmw.com/search/dh-9-0-0-0-0-{}-0/".format(page)
    # 发送网页请求，返回值用resp存储
    resp = requests.get(url=url,headers=headers,proxies=proxies)
    # 解码后就是网页源代码
    html_doc = resp.content.decode("utf-8")
    # 用BS去处理网页源代码
    soup = BeautifulSoup(html_doc,'lxml')
    # 把所有class值为lst的div标签取出来
    list = soup.find('div',class_='lst').find_all('a',class_='u-card')
    # 创建一个列表用来存放所有图片链接
    pic_urls = []
    for item in list:
        # 提取名字，这一步是用来测试的
        mingzi = item.find('p',class_='u-tt').string
        # 提取图片链接
        pic_url = item.find('img').get('data-src')
        # print(mingzi + "---" + pic_url)
        # 将pic_url存入列表pic_urls中
        pic_urls.append(pic_url)

    for tar,url in enumerate(pic_urls):
        # print(tar,"---",url)
        # 因为url的格式是“//xxx.com/xxxx.img”，前面少了协议，所以要加上
        urln = "http:"+url
        # print(urln)
        save_img(urln,tar)

def main():
    # 从第1页爬到第6页
    for page in range(1,7):
        path = "第"+str(page)+"页"
        try:
            mk_dir(path)
            pachong(page)
        except exception as e:
            print(e)


if __name__ == '__main__':
    main()