# WJX_Autosubmit

问卷星自动提交，Python3版本，2019年8月仍有效

目前github上的可用版本并不多，同时个人接触较多问卷星的问卷，便萌生了用Python3的爬虫来完成问卷的想法，同时，作为学习的项目。

## 项目需求
以下为项目所需要安装的库（模块），点击文字会跳转到对应的官方文档，请确保安装了对应的最新的版本（在Python3中建议使用pip3 进行安装,也可以按照官方文档的方法）
- [requests](https://2.python-requests.org//zh_CN/latest/")
- [bs4](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id8)
- [fake-useragent](https://pypi.org/project/fake-useragent/)

以下为所需要的Python标准库，不需要另外安装
- re
- random
- time

## 项目思路
参考项目:
- [简书：Python填写问卷星 作者：feifeifeikkk]( https://www.jianshu.com/p/34961ceedcb4)
- [Python笔记（六）--Python3通过post方法实现自动提交问卷星调查问卷](http://www.pianshen.com/article/6056350400/)
- [蜻蜓HTTP](https://www.qingtingip.com/h_210979.html)
- [WJXAutoSubmit](https://github.com/huanxyx/WJXAutoSubmit )


首先对提交后的网页进行分析

![](https://github.com/NormanBB/WJX_Autosubmit/blob/master/1.jpg)
> 问卷星提交数据的url

![](https://github.com/NormanBB/WJX_Autosubmit/blob/master/2.jpg)
> 问卷星提交的参数
