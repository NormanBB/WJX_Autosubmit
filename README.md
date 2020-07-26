# WJX_Autosubmit

问卷星自动提交，Python3版本，2020年7月仍有效。采用构建随机答案，不支持验证码。

目前github上的可用版本并不多，同时个人接触较多问卷星的问卷，便萌生了用Python3的爬虫来完成问卷的想法，同时，作为学习的项目。

## 程序运行

1. 安装依赖。
> pip install -r requirements.txt

2. 按照提示输入所需信息

![](./result.png)


## 鸣谢:
- [简书：Python填写问卷星]( https://www.jianshu.com/p/34961ceedcb4)
- [Python笔记（六）--Python3通过post方法实现自动提交问卷星调查问卷](http://www.pianshen.com/article/6056350400/)
- [WJXAutoSubmit](https://github.com/huanxyx/WJXAutoSubmit )
- [ProxyPool 爬虫代理IP池](https://github.com/jhao104/proxy_pool)
- [问卷星项目](https://github.com/tignioj/test_login/tree/master/wjx) 

## Bugs

程序仅支持固定问题的问卷，并不支持问题动态变化的问卷。

欢迎对不同种类问卷进行适配并提交pull request.

在此推荐一个适配多种题型的项目。

- [自动填写问卷并提交,然后自动刷新继续填写](https://github.com/ZainCheung/wenjuanxin)
