import requests
from bs4 import BeautifulSoup
import re
import random
import time
from collections import OrderedDict
import datetime
from fake_useragent import UserAgent
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
'''
作者：normanbb
链接：https://github.com/NormanBB/WJX_Autosubmit
来源：Github
'''

'''调查页面，获取相关参数'''
# 获取调查问卷的页面
def get_fill_content(url,proxy,user_agent):
    headers = {
    'user-agent': user_agent,
    }
    r1 = requests.get(url, headers=headers,proxies={"http": "http://{}".format(proxy)},verify=False)
    setCookie = r1.headers['Set-Cookie']
    CookieText = re.findall(r'acw_tc=.*?;', setCookie)[0] + re.findall(r'\.ASP.*?;', setCookie)[0] + re.findall(r'jac.*?;', setCookie)[0] + re.findall(r'SERVERID=.*;',setCookie)[0]
    return r1.text,CookieText

# 从页面中获取curid,rn,jqnonce,starttime,同时构造ktimes用作提交调查问卷
def get_submit_query(content):
    curid = re.search(r'\d{8}',content).group()
    rn = re.search(r'\d{9,10}\.\d{8}',content).group()
    jqnonce= re.search(r'.{8}-.{4}-.{4}-.{4}-.{12}',content).group()
    ktimes = random.randint(5, 18)
    starttime = (datetime.datetime.now()-datetime.timedelta(minutes=1)).strftime("%Y/%m/%d %H:%M:%S")
    return curid, rn, jqnonce, ktimes, starttime

#通过ktimes,jqnonce构造jqsign	
def get_jqsign(ktimes, jqnonce):
        result = []
        b = ktimes % 10
        if b == 0:
            b = 1
        for char in list(jqnonce):
            f = ord(char) ^ b
            result.append(chr(f))
        return ''.join(result)
     

'''获取随机答案'''	

# 获取调查问卷的题目
def get_title_list(content):
    main_soup = BeautifulSoup(content, 'lxml')
    title_soup_list = main_soup.find_all(id=re.compile(r'div\d'))
    title_list = []
    for title_soup in title_soup_list:
        title_str = title_soup.find(class_='div_title_question').get_text().strip()
        choice_list = [choice.get_text() for choice in title_soup.find_all('label')]		
        title_dict = {
            'title': title_str,
            'choice_list': choice_list,
            'is_choice': len(choice_list) != 0
        }
        title_list.append(title_dict)	 
    return title_list
        
# 随机选择
def random_choose(title_list):
    answer_list = []
    for title in title_list:
        if title['is_choice']:
            title['answer'] = random.randint(1, len(title['choice_list']))
        else:
            title['answer'] = ''
        answer_list.append(title['answer'])
    return answer_list
    
#构造符合样式的提交数据
def get_submit_data(title_list,answer_list):
    form_data = ''
    for num in range(len(title_list)):
        form_data += str(num+1) + '$' + str(answer_list[num]) + '}'
    return form_data[:-1]

#使用代理
def get_proxy():
    return requests.get("http://118.24.52.95/get/").json()

def Auto_WjX():
    proxy = get_proxy().get("proxy")
    user_agent=UserAgent().random
    fill_url = get_fill_url
    fill_content,cookies = get_fill_content(fill_url,proxy,user_agent)#网页源代码，cookies
    title_list = get_title_list(fill_content) #所有题目
    '''获取相关参数'''
    curid, rn, jqnonce, ktimes,starttime = get_submit_query(fill_content)
    jqsign = get_jqsign(ktimes,jqnonce)
    time_stamp = '{}{}'.format(int(time.time()), random.randint(100, 200))  # 生成一个时间戳，最后三位为随机数
    #curid, time_stamp, starttime, ktimes, rn, jqnonce, jqsign
    FormData = {
            'submittype': '1',
            'curID': curid,
            't': time_stamp,
            'starttime': starttime,
            'rn': rn,   
            'hlv': '1',
            'ktimes':ktimes,
            'jqnonce':jqnonce,
            'jqsign':jqsign,
        }
    url = 'https://www.wjx.cn/joinnew/processjq.ashx'
    headers = {
        "Host": "www.wjx.cn",
        "Connection": "keep-alive",
        "Origin": "https://www.wjx.cn",
        "User-Agent": user_agent,
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en, zh-CN;q=0.9, zh;q=0.8",
        "Referer": fill_url,
        "Cookie": cookies,
    }
    #作随机选择
    random_data = random_choose(title_list)
    #构造符合样式的提交数据
    #自定义答案可以将选择与构造部分去除
    submit_data = get_submit_data(title_list,random_data)
    data = {'submitdata':str(submit_data)}
    # 发送请求
    r = requests.post(url=url,headers=headers, data=data, params=FormData,proxies={"http": "http://{}".format(proxy)},verify=False)
    #通过测试返回数据中表示成功与否的关键数据（’10‘or '22'）在开头,所以只需要提取返回数据中前两位元素
    result = r.text[0:2]
    return result

def main(times):
    PostNum = 0
    times=int(times)
    print('程序开始运行')
    # i 为 提交次数
    for i in range(times):	
        try:
            result= Auto_WjX()
            #10表示成功，20表示失败
            if int(result) in [10]:
                print('[ Response : %s ]  ===> 提交成功！！！！' % result)
                PostNum += 1
                time.sleep(5)	# 设置休眠时间，这里要设置足够长的休眠时间
            else:
                print('[ Response : %s ]  ===> 提交失败！！！！' % result)	
        except requests.exceptions.ProxyError:
            print('代理不可用，跳过') 
            pass
        except ValueError:
            print('服务器返回非正常响应，跳过') 
            pass
    print('程序运行结束，成功提交%s份调查报告' % PostNum)  # 总结提交成功的数量，并打印
        
if __name__ == '__main__':
    print(r"""
        本程序用于构建随机答案填写问卷星问卷
    """)
    get_fill_url = input('输入问卷地址:')
    times = input('输入提交次数:')
    main(times)
    


