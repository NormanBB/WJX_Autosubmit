#使用代理
import random

def get_proxy():
    proxy_https_list = ['110.44.113.105:8080', '46.52.255.69:8080', '94.75.76.10:8080', '89.237.29.198:8080', '212.248.42.202:3128', '51.68.61.17:80', '91.206.110.190:8080', '88.99.134.61:8080', '5.187.52.68:5836', '193.178.249.22:5836', '200.105.157.218:53281', '85.143.254.20:8080', '62.171.130.72:3128', '176.115.16.250:8080', '194.61.138.12:8080', '45.173.4.249:999', '152.204.132.112:8080', '92.51.36.1:8080', '201.28.39.6:3128', '195.239.16.90:8080', '54.39.85.228:3128', '103.116.250.78:8080', '147.139.30.212:3128', '91.203.19.1:9999', '103.87.164.75:8080', '169.159.130.182:8080', '3.129.161.78:3128', '51.15.152.123:3128', '66.42.36.13:3128', '110.78.148.197:8080', '190.2.210.98:8080', '65.18.114.230:443', '194.190.30.248:8080', '36.37.160.242:8080', '34.245.226.55:80', '190.217.7.65:999', '103.146.21.4:3128', '212.47.246.46:3128', '180.183.224.198:8080', '181.40.122.102:8080', '212.83.175.205:5836', '103.86.49.193:3128', '110.44.133.135:3128', '67.219.147.12:5836', '188.226.58.86:3128', '89.221.54.114:8080', '109.75.37.113:3128', '80.89.133.210:3128', '110.76.148.242:8080', '116.197.133.90:8080', '176.103.45.24:8080', '62.69.213.149:8090', '103.14.111.218:3128', '195.22.148.7:5836', '51.158.26.132:5836', '95.161.188.246:38302', '46.0.203.186:8080', '103.122.253.149:8080', '51.68.61.17:8080', '41.254.47.196:8080', '213.129.56.108:8080', '217.130.92.230:8080', '193.233.9.167:57625', '103.88.127.178:8080', '158.101.98.173:3128', '88.150.236.115:3128', '193.85.28.235:8081', '209.159.158.234:8080', '74.208.112.84:8080', '202.5.56.71:8080', '78.37.27.139:58252', '217.163.11.223:8080', '88.99.77.54:5836', '49.0.65.246:8080', '213.136.64.118:5836', '173.82.78.187:5836', '167.88.178.54:3128', '163.172.224.241:5836', '138.219.216.142:999', '163.172.29.22:5836', '180.183.10.241:8080', '186.1.195.134:3128', '51.161.62.117:8080', '182.48.79.85:8080', '194.34.132.175:5836', '136.243.32.244:5836',
                        '51.89.34.8:3128', '136.243.81.120:8080', '108.61.247.249:8080', '5.16.11.179:8080', '35.196.42.45:3128', '164.132.22.144:8888', '79.120.177.106:8080', '195.24.53.195:8080', '88.99.77.52:5836', '176.108.47.38:3128', '51.79.27.155:80', '144.91.88.111:5836', '110.39.175.2:8080', '195.154.233.185:5836', '180.183.246.110:8080', '81.23.114.198:8080', '117.102.72.66:8080', '206.125.41.130:80', '203.210.84.59:80', '113.53.53.138:8080', '31.135.93.56:45938', '144.217.201.45:80', '51.89.32.83:3128', '92.42.46.36:8888', '88.247.153.104:8080', '181.225.213.229:999', '52.251.47.125:3128', '37.54.51.106:8080', '3.92.251.21:3128', '190.217.29.5:8080', '194.246.41.17:80', '45.224.148.5:999', '113.161.186.101:8080', '78.96.125.24:3128', '54.38.138.245:8181', '46.191.226.105:3128', '66.23.207.171:5836', '179.108.81.75:8080', '46.171.2.211:3128', '95.181.45.234:55878', '68.188.63.149:8080', '103.114.76.101:8080', '138.68.2.224:3128', '180.93.28.180:8080', '12.156.45.155:3128', '90.154.148.71:3128', '202.134.191.156:8080', '45.170.35.65:999', '197.14.14.234:80', '80.23.125.226:3128']
    return random.choice(proxy_https_list)


def get_agent():
    USER_AGENT_LIST = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]
    return random.choice(USER_AGENT_LIST)
