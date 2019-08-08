import requests
from bs4 import BeautifulSoup
import re
import random
import time
from fake_useragent import UserAgent
from collections import OrderedDict

'''伪造提交ip'''

#访问西刺代理,获取代理地址池，西刺代理将ip地址放在网页td标签中，读取所有td标签，并切片，获取ip地址
def Get_POOLS():
	headers = {'User-Agent': UserAgent().random}
	html = requests.get(url='https://www.xicidaili.com/nn/', headers=headers)
	#以下为细节说明，来源于re官方文档
	#正则匹配（在带有 'r' 前缀的字符串字面值中，反斜杠不必做任何特殊处理。）
	#(...)（组合），匹配括号内的任意正则表达式，并标识出组合的开始和结尾。
	pools = re.findall(r'<td>(.+?)</td>', html.text)[0:499:5]
	return pools

#从代理池中提取地址用于构造headers提交数据伪造提交ip
def Get_Headers(pools):
	Random_IP = random.choice(pools)
	headers = {	 
		'User-Agent':UserAgent().random,
		'X-Forwarded-For':Random_IP,
		}
	return headers


'''调查页面，获取相关参数'''
# 获取调查问卷的页面
def get_fill_content(url):
	headers = {
	'user-agent': UserAgent().random
	}
	res = requests.get(url, headers=headers)#, headers=headers)
	cookies = res.cookies
	return res.text,cookies

# 从页面中获取curid,rn,jqnonce,starttime,同时构造ktimes用作提交调查问卷
def get_submit_query(content):
	curid = re.search(r'\d{8}',content).group()
	rn = re.search(r'\d{9,10}\.\d{8}',content).group()
	jqnonce= re.search(r'.{8}-.{4}-.{4}-.{4}-.{12}',content).group()
	ktimes = random.randint(5, 18)
	starttime = re.search(r'\d+?/\d+?/\d+?\s\d+?:\d{2}',content).group()
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
	 
#通过各个需要的参数构造提交url
def get_submit_url(curid, rn,jqnonce,ktimes,jqsign,starttime):
	time_stamp = '{}{}'.format(int(time.time()), random.randint(100, 200))  # 生成一个时间戳，最后三位为随机数
	url = 'http://www.wjx.cn/joinnew/processjq.ashx?submittype=1&curID={}&t={}&starttime={}&ktimes={}&rn={}&jqnonce={}&jqsign={}'.format(curid, time_stamp, starttime, ktimes, rn, jqnonce, jqsign)
	return url

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
		title = title_list[num]
		form_data += str(num+1) + '$' + str(answer_list[num]) + '}'
	return form_data[:-1]

def Auto_WjX():
	'''页面请求'''
	fill_url = ''
	fill_content,cookies = get_fill_content(fill_url)#网页源代码，cookies
	title_list = get_title_list(fill_content) #所有题目
	
	'''获取相关参数'''
	curid, rn, jqnonce, ktimes,starttime = get_submit_query(fill_content)
	jqsign = get_jqsign(ktimes,jqnonce)
	url= get_submit_url(curid,rn,jqnonce,ktimes,jqsign,starttime)
	
	#作随机选择
	random_data = random_choose(title_list)
	#构造符合样式的提交数据
	submit_data = get_submit_data(title_list,random_data)
	data = {'submitdata':str(submit_data)}
	# 发送请求
	r = requests.post(url=url, data=data,headers=Get_Headers(pools),cookies = cookies,verify=False)
	#通过测试返回数据中表示成功与否的关键数据（’10‘or '22'）在开头,所以只需要提取返回数据中前两位元素
	result = r.text[0:2]
	return result

def main():
	PostNum = 0
	#提交50次
	for i in range(50):
		result = Auto_WjX()
		#10表示成功，20表示失败
		if int(result) in [10]:
			print('[ Response : %s ]  ===> 提交成功！！！！' % result)
			PostNum += 1
		else:
			print('[ Response : %s ]  ===> 提交失败！！！！' % result)
		time.sleep(2)	# 设置休眠时间，这里要设置足够长的休眠时间
	print('脚本运行结束，成功提交%s份调查报告' % PostNum)  # 总结提交成功的数量，并打印
	
if __name__ == '__main__':
	pools = Get_POOLS()
	main()
	


