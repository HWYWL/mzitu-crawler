# mzitu-crawler
爬取mzitu网站的妹子，注意营养

[![license](https://img.shields.io/github/license/ZYSzys/Mzitu_Spider.svg)](https://github.com/HWYWL/mzitu-crawler/blob/master/LICENSE)

### 环境
python2.7, 3.6
### python库
http请求：requests  
图片提取：bs4  
存储相关: os  


### 下载安装
在终端输入如下命令：
```bash
git clone https://github.com/HWYWL/mzitu-crawler.git
```

### 使用方法
在当前目录下输入：
```bash
cd mzitu-crawler
pip install -r requirements.txt
python main.py
```

### 修改爬取的数量
```python
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
```

运行爬虫，如图所示  
![](https://i.imgur.com/6508MeF.jpg)

稍等几分钟后，当前目录下生成Mzitu文件夹，首页每套图以存储在其中  
![](https://i.imgur.com/6mbzr7u.jpg)

老板再来两瓶营养快线
![](https://i.imgur.com/vvjYCeP.jpg)

### 问题建议

- 联系我的邮箱：ilovey_hwy@163.com
- 我的博客：http://www.hwy.ac.cn
- GitHub：https://github.com/HWYWL