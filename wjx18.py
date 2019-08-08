import requests
from bs4 import BeautifulSoup
import re
import random
import time


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}

session = requests.Session()

# 获取调查问卷的页面
def get_fill_content(url):
    res = session.get(url, headers=headers)#, headers=headers)
    res.raise_for_status()
    return res.text

# 获取调查问卷的题目
def get_title_list(content):
    main_soup = BeautifulSoup(content, 'lxml')
    title_soup_list = main_soup.find_all(id=re.compile(r'div\d'))
    title_list = []
    for title_soup in title_soup_list:
        title_str = title_soup.find(class_='div_title_question').get_text().strip()             #field-label
        choice_list = [choice.get_text() for choice in title_soup.find_all('label')]            #select('.label')
        title_dict = {
            'title': title_str,
            'choice_list': choice_list,
            'is_choice': len(choice_list) != 0
        }
        title_list.append(title_dict)    
    return title_list

A_num = ord('A')
# 打印题目
def print_title_list(title_list):
    for title_num, title in enumerate(title_list):
        print(str(title_num+1) + '.' + title['title'])
        for choice_num, choice_str in enumerate(title['choice_list']):
            print(chr(A_num + choice_num) + '.' + choice_str, end='  ')
        print('\n')

# 随机选择
def random_choose(title_list):
    for title in title_list:
        if title['is_choice']:
            title['answer'] = random.randint(1, len(title['choice_list']))
        else:
            title['answer'] = ''

# 构造提交表单数据
def get_submit_data(title_list):
    form_data = ''
    for num in range(len(title_list)):
        title = title_list[num]
        form_data += str(num+1) + '$' + str(title['answer']) + '}'
    return {
        'submitdata': form_data[:-1]
    }

# 获取随机ip，避免访问频繁而导致的验证码
def get_random_ip():
    return (str(random.randint(1,255))+".")+(str(random.randint(1,255))+".")+(str(random.randint(1,255))+".")+str(random.randint(1,255))

submit_host_url = 'https://www.wjx.cn/joinnew/processjq.ashx?'
# 构造提交的url
def get_submit_url(curid, rnnum):
    start_time = time.localtime(time.time() - random.randint(300, 1000))
    query_dict = {
        'curID': str(curid),                                                # 从填写页面获取的问卷curid
        'starttime': time.strftime('%Y/%m/%d %H:%M:%S', start_time),        # 模拟开始时间
        'submittype': '1',
        'rn': str(rnnum),                            # 从填写页面获取的rn
        't': str(int(time.time()*1000)),                                    # 模拟提交时间
    }
    query_str = ''
    for key, value in query_dict.items():
        query_str += key + '=' + value + '&'
    return submit_host_url + query_str[:-1]

# 从页面中获取curid和rnnum，用作提交调查问卷
def get_submit_query(content):
    curid_reg = re.compile(r'activityId = ?\'?(\d+?)\'?;')
    rnnum_reg = re.compile(r'rndnum="(\d+.?\d+?)";')
    curid = curid_reg.search(fill_content).group(1)
    rnnum = rnnum_reg.search(fill_content).group(1)
    return curid, rnnum

# 请求头
submit_headers = {
    # 'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;',
    # 'cookie': '.ASPXANONYMOUS=weSCc8wu1AEkAAAANjE3MGMxZGItNDQ5OC00YWI3LTkxZGEtNmVkNTY5MzU5OTdlVi6pfvz50MfKv5R7T8xKFWe2LqE1; UM_distinctid=163b2116ddfbbc-048109171a2d4f-737356c-144000-163b2116de07fd; jac24389107=04539338; CNZZDATA4478442=cnzz_eid%3D1533293032-1527696898-%26ntime%3D1527730790; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1527700877,1527732232; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=1527732232',
    'origin': 'https://www.wjx.cn',
    'referer': 'https://www.wjx.cn/m/24389107.aspx',
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

# 需要填写调查问卷的url
fill_url = 'https://www.wjx.cn/jq/xxxxxxxx.aspx'
#'https://ks.wjx.top/jq/xxxxxxxx.aspx'#'https://www.wjx.cn/jq/xxxxxxxx.aspx' #'https://www.wjx.cn/m/xxxxxxxx.aspx'

# 调查问卷填写页面的内容
fill_content = get_fill_content(fill_url)
# 调查问卷的题目
title_list = get_title_list(fill_content)
# 从页面中获取的两个有关提交需要的参数
curid, rnnum = get_submit_query(fill_content)
# print_title_list(title_list)

# 提交次数
n = 190

# 运行部分
for i in range(n):
    # if (i % 5 == 0):
    '''页面请求'''
    # 调查问卷填写页面的内容
    fill_content = get_fill_content(fill_url)
    # 调查问卷的题目
    title_list = get_title_list(fill_content)
    # 从页面中获取的两个有关提交需要的参数
    curid, rnnum = get_submit_query(fill_content)

    '''提交'''
    # 随机选择答案
    random_choose(title_list)                           #随机选择答案
    # 构造不同时间点提交的url
    submit_url = get_submit_url(curid, rnnum)           #获取请求的url
    # 生成提交表单数据
    submit_data = get_submit_data(title_list)
    # 修改X-Forwarded-For避免多次重复访问而出现验证码
    submit_headers['X-Forwarded-For'] = get_random_ip() #随机IP
    # 发送请求
    res = session.post(submit_url, data=submit_data, headers=submit_headers)
    # 查看结果
    print(res.text)
    print(res.request.url)
    time.sleep(0.5)
    session = requests.Session()








