import requests
from bs4 import BeautifulSoup
import re
import random
import time
import collections 
import urllib.request
from fake_useragent import UserAgent



def Get_IP():
    headers = {     #构建简易的请求头，用于访问西刺代理网站
        'User-Agent': UserAgent().random
    }
    html = urllib.request.Request(url='https://www.xicidaili.com/nn/', headers=headers)
    html = urllib.request.urlopen(html).read().decode('utf-8')
    reg = r'<td>(.+?)</td>'#通过浏览器的F12查看页面元素，发现所有元素都放在td标签中，并按IP地址，端口，协议，地址，时间的顺序排列
    reg = re.compile(reg)
    #经正侧表达式匹配后将所有元素按顺序存放在列表中，但这并不是最终的结果
    pools = re.findall(reg, html)[0:499:5]#提取出其中所有的IP地址，并存放到列表中，形成地址池
    Random_IP = random.choice(pools)#随机在地址池中选出一个IP地址
    return Random_IP
构建请求头header（这里需要自己抓包收集数据（Cookie）来构建自己的请求头）
如果一直不成功可以重新抓包更换一下coookie
def Get_Headers():
    headers = {  
        'Host':'www.wjx.cn',
        'User-Agent': UserAgent().random,#随机User-Agent，需要从fake_useragent 库中 UserAgent包
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',#以表格形式提交数据
        'Referer':'https://www.wjx.cn/m/XXXXX.aspx',#你的调查问卷链接
        'Cookie':'XXXXX',#抓包
        'X-Forwarded-For':Get_IP()#调用函数获取代理IP地址
    }
    return headers
构建传参函数用来提交参数
def Auto_WjX():
    url = '目的url'
    #data是提交的参数（填写的问卷数据需要自己按实际情况编写）
    #若包含中文参数则需要指定编码，例：data = 'submit=1$2}2$3}3$python大法好啊'.encode("utf-8").decode("latin1")
    data = "submitdata=1$1}2$3}3$1}4$2}5$1}6$2}7$2}8$1}9$1}10$1}11$1}12$1}13$1}14$1}15$1}16$1}17$1}18$1}19$1}20$1}21$1}22$1}23$1}24$1}25$2}26$3}27$3}28$2|10|13|19}29$4|10}30$3|7}31$2}32$3}33$4}34$1}35$1}36$1}37$2}38$2}39$2}40$2}41$1}42$2}43$1}44$2}45$1}46$1}47$4}48$4}49$4}50$4}51$3}52$3}53$1}54$1}55$1}56$3}57$3}58$3}59$1}60$3}61$3"
    r = requests.post(url, headers=Get_Headers(), data=data, verify=False)
    #通过测试返回数据中表示成功与否的关键数据（’10‘or '22'）在开头,所以只需要提取返回数据中前两位元素
    result = r.text[0:2]
    return result
#剩下的就是编写自己的main函数了(这里就不多说了，只有一点就是休眠时间设置长一点)
def main():
    global PostNum
    for i in range(10):
        result = Auto_WjX()
        if int(result) in [10]:#循环10次，调用10次Auto_WjX函数（亲测提交10次，成功5次，50%的成功率）
            print('[ Response : %s ]  ===> 提交成功！！！！' % result)
            PostNum += 1
        else:
            print('[ Response : %s ]  ===> 提交失败！！！！' % result)
        time.sleep(30)  # 设置休眠时间，这里要设置足够长的休眠时间
	print('脚本运行结束，成功提交%s份调查报告' % PostNum)  # 总结提交成功的数量，并打印
	
if __name__ == '__main__':
    main()
