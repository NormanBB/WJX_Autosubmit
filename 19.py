import requests
import re
r1 = requests.get('https://www.wjx.cn/jq/43178556.aspx')
setCookie = r1.headers['Set-Cookie']
CookieText = re.findall(r'acw_tc=.*?;', setCookie)[0] + re.findall(r'\.ASP.*?;', setCookie)[0] + re.findall(r'jac.*?;', setCookie)[0] + re.findall(r'SERVERID=.*;',setCookie)[0]