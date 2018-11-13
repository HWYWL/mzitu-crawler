#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'YI'

import requests
from bs4 import BeautifulSoup
import os


class MeiZe:
    def __init__(self, url, page):
        self.url = url + str(page)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/60.0.3112.113 Safari/537.36',
            'Referer': 'http://www.mzitu.com/'
        }
        self.req = requests.session()
        self.all_a = []
        self.all_a_title = []
        self.all_a_max = []
        os.makedirs(os.path.join(os.getcwd(), 'mzitu'))
        os.chdir(os.path.join(os.getcwd(), 'mzitu'))
        self.initpwd = os.getcwd()

    # 解析网页
    def domainHtml(self):
        html = self.req.get(self.url, headers=self.headers)
        lis = BeautifulSoup(html.text, 'lxml').find('div', class_='postlist').find_all('li')
        for a in lis:
            imgurl = a.find('a')['href']
            self.all_a.append(imgurl)

    # 获取页面信息
    def getMaxPage(self):
        for a in self.all_a:
            imghtml = self.req.get(a, headers=self.headers)
            title = BeautifulSoup(imghtml.text, 'lxml').find('h2', class_='main-title').string
            # 获取标题
            last = BeautifulSoup(imghtml.text, 'lxml').find('div', class_='pagenavi').find_all('span')
            last = int(last[-2].string)
            self.all_a_title.append(title)
            self.all_a_max.append(last)

    # 下载妹子
    def downloading(self):
        cnt = 0
        print('当前页总个数: %s' % len(self.all_a))
        for a in self.all_a:
            print('正在下载第 %s 个妹子...' % (cnt + 1))
            os.makedirs(os.path.join(os.getcwd(), self.all_a_title[cnt]))
            os.chdir(os.path.join(os.getcwd(), self.all_a_title[cnt]))

            for i in range(1, self.all_a_max[cnt] + 1):
                nurl = a + '/' + str(i)
                imghtml = self.req.get(nurl, headers=self.headers)
                aaa = BeautifulSoup(imghtml.text, 'lxml').find('div', class_='main-image').find('img')['src']
                img = self.req.get(aaa, headers=self.headers)
                f = open(str(i) + '.jpg', 'ab')
                f.write(img.content)
                f.close()

            cnt += 1
            os.chdir(self.initpwd)

        print('本页下载完成，进入下一页下载!')


if __name__ == '__main__':
    # 当前页
    current = 1
    # 总页数
    total = 100

    while current < total:
        mz = MeiZe("http://www.mzitu.com/page/", current)
        mz.domainHtml()
        mz.getMaxPage()
        mz.downloading()
        current += 1
