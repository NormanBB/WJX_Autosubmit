import requests
import re
import random
import datetime
import time


def get_fill_content(url):
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
    r1 = requests.get(url, headers=headers)
    setCookie = r1.headers['Set-Cookie']
    CookieText = re.findall(r'acw_tc=.*?;', setCookie)[0] + re.findall(r'\.ASP.*?;', setCookie)[0] + re.findall(r'jac.*?;', setCookie)[0] + re.findall(r'SERVERID=.*;', setCookie)[0]
    return r1.text, CookieText

# 从页面中获取curid,rn,jqnonce,starttime,同时构造ktimes用作提交调查问卷


def get_submit_query(content):
    curid = re.search(r'\d{8}', content).group()
    rn = re.search(r'\d{9,10}\.\d{8}', content).group()
    jqnonce = re.search(r'.{8}-.{4}-.{4}-.{4}-.{12}', content).group()
    ktimes = random.randint(5, 18)
    starttime = (datetime.datetime.now() -
                 datetime.timedelta(minutes=1)).strftime("%Y/%m/%d %H:%M:%S")
    return curid, rn, jqnonce, ktimes, starttime

# 通过ktimes,jqnonce构造jqsign


def get_jqsign(ktimes, jqnonce):
    result = []
    b = ktimes % 10
    if b == 0:
        b = 1
    for char in list(jqnonce):
        f = ord(char) ^ b
        result.append(chr(f))
    return ''.join(result)


def answer_data():
    data = "1$2}2$2}3$2}4$2}5$3}6$1}7$1}8$2}9$2}10$4}11$3}12$1}13$3}14$2}15$1}16$2}17$2}18$4}19$2}20$2}21$3"
    return data


def main():
    url = 'https://www.wjx.cn/jq/43178556.aspx'
    fill_content, cookies = get_fill_content(url)
    curid, rn, jqnonce, ktimes, starttime = get_submit_query(fill_content)
    jqsign = get_jqsign(ktimes, jqnonce)
    time_stamp = '{}{}'.format(int(time.time()), random.randint(100, 200))
    FormData = {
        'submittype': '1',
        'curID': curid,
        't': time_stamp,
        'starttime': starttime,
        'rn': rn,
        'hlv': '1',
        'ktimes': ktimes,
        'jqnonce': jqnonce,
        'jqsign': jqsign,
    }
    post_url = 'https://www.wjx.cn/joinnew/processjq.ashx'
    headers = {
        "Host": "www.wjx.cn",
        "Connection": "close",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en, zh-CN;q=0.9, zh;q=0.8",
        "Referer": url,
        "Cookie": cookies,
    }
    data = {'submitdata': str(answer_data())}
    r = requests.post(url=post_url, headers=headers,data=data, params=FormData)
        # 通过测试返回数据中表示成功与否的关键数据（’10‘or '22s'）在开头,所以只需要提取返回数据中前两位元素
    print(r.text[0:2])

main()
