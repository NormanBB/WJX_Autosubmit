import requests
import re
import time
import random
from bs4 import BeautifulSoup


class WenJuanXing:
	def __init__(self, url):
		"""
		:param url:要填写的问卷的url
		"""
		self.wj_url = url
		self.post_url = None
		self.header = None
		self.cookie = None
		self.data = None
		
	# 获取调查问卷的题目
	def get_title_list(self,content):
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
	def random_choose(self,title_list):
		answer_list = []
		for title in title_list:
			if title['is_choice']:
				title['answer'] = random.randint(1, len(title['choice_list']))
			else:
				title['answer'] = ''
			answer_list.append(title['answer'])
		return answer_list
# 构造提交表单数据
	def get_submit_data(self,title_list,answer_list):
		form_data = ''
		for num in range(len(title_list)):
			title = title_list[num]
			form_data += str(num+1) + '$' + str(answer_list[num]) + '}'
		return form_data[:-1]

	def set_header(self):
		"""
		随机生成ip，设置X-Forwarded-For
		ip需要控制ip段，不然生成的大部分是国外的
		:return:
		"""
		ip = '{}.{}.{}.{}'.format(112, random.randint(64, 68), random.randint(0, 255), random.randint(0, 255))
		self.header = {
			'X-Forwarded-For': ip,
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko\
						) Chrome/71.0.3578.98 Safari/537.36',
		}

	def get_ktimes(self):
		"""
		随机生成一个ktimes,ktimes是构造post_url需要的参数，为一个整数
		:return:
		"""
		return random.randint(15, 50)

	def get_response(self):
		"""
		访问问卷网页，获取网页代码
		:return: get请求返回的response
		"""
		response = requests.get(url=self.wj_url, headers=self.header)
		self.cookie = response.cookies
		return response

	def get_jqnonce(self, response):
		"""
		通过正则表达式找出jqnonce,jqnonce是构造post_url需要的参数
		:param response: 访问问卷网页，返回的reaponse
		:return: 找到的jqnonce
		"""
		jqnonce = re.search(r'.{8}-.{4}-.{4}-.{4}-.{12}', response.text)
		return jqnonce.group()

	def get_rn(self, response):
		"""
		通过正则表达式找出rn,rn是构造post_url需要的参数
		:param response: 访问问卷网页，返回的reaponse
		:return: 找到的rn
		"""
		rn = re.search(r'\d{9,10}\.\d{8}', response.text)
		return rn.group()

	def get_id(self, response):
		"""
		通过正则表达式找出问卷id,问卷是构造post_url需要的参数
		:param response: 访问问卷网页，返回的reaponse
		:return: 找到的问卷id
		"""
		id = re.search(r'\d{8}', response.text)
		return id.group()

	def get_jqsign(self, ktimes, jqnonce):
		"""
		通过ktimes和jqnonce计算jqsign,jqsign是构造post_url需要的参数
		:param ktimes: ktimes
		:param jqnonce: jqnonce
		:return: 生成的jqsign
		"""
		result = []
		b = ktimes % 10
		if b == 0:
			b = 1
		for char in list(jqnonce):
			f = ord(char) ^ b
			result.append(chr(f))
		return ''.join(result)

	def get_start_time(self, response):
		"""
		通过正则表达式找出问卷starttime,问卷是构造post_url需要的参数
		:param response: 访问问卷网页，返回的reaponse
		:return: 找到的starttime
		"""
		start_time = re.search(r'\d+?/\d+?/\d+?\s\d+?:\d{2}', response.text)
		return start_time.group()

	def set_post_url(self):
		"""
		生成post_url
		:return:
		"""
		self.set_header()  # 设置请求头，更换ip
		response = self.get_response()	# 访问问卷网页，获取response
		ktimes = self.get_ktimes()	# 获取ktimes
		jqnonce = self.get_jqnonce(response)  # 获取jqnonce
		rn = self.get_rn(response)	# 获取rn
		id = self.get_id(response)	# 获取问卷id
		jqsign = self.get_jqsign(ktimes, jqnonce)  # 生成jqsign
		start_time = self.get_start_time(response)	# 获取starttime
		time_stamp = '{}{}'.format(int(time.time()), random.randint(100, 200))	# 生成一个时间戳，最后三位为随机数
		url = 'https://www.wjx.cn/joinnew/processjq.ashx?submittype=1&curID={}&t={}&starttim' \
			  'e={}&ktimes={}&rn={}&jqnonce={}&jqsign={}'.format(id, time_stamp, start_time, ktimes, rn, jqnonce, jqsign)
		self.post_url = url	 # 设置url

	def post_data(self):
		"""
		发送数据给服务器
		:return: 服务器返回的结果
		"""
		response = self.get_response()
		title_list = self.get_title_list(response.text)
		random_data = self.random_choose(title_list)
		submit_data = self.get_submit_data(title_list,random_data)
		data = {'submitdata':str(submit_data)}
		response = requests.post(url=self.post_url, data=data, headers=self.header, cookies=self.cookie)
		return response
		
	def mul_run(self, n):
		"""
		填写多次问卷
		:return:
		"""
		PostNum = 0
		for i in range(n):
			self.set_post_url()
			result = self.post_data()
			print(result.content.decode())
			if int(result.text[0:2]) in [10]:#循环10次，调用10次Auto_WjX函数
				print('[ Response : %s ]  ===> 提交成功！！！！' %result.text[0:2])
				PostNum += 1
			else:
				print('[ Response : %s ]  ===> 提交失败！！！！' %result.text[0:2])
			time.sleep(2)	# 设置休眠时间，这里要设置足够长的休眠时间
		print('脚本运行结束，成功提交%s份调查报告' % PostNum)  # 总结提交成功的数量，并打印
			
			
if __name__ == '__main__':
	w = WenJuanXing('')
	w.mul_run(100)
