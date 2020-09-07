from threading import Thread
import random
from multiprocessing import Pool
import time
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ProxyTask(Thread):

    def __init__(self, proxy,filename):
        super().__init__()
        self._proxy = proxy
        self._filename=filename
    
    def run(self):
        url = 'https://httpbin.org/post'
        try:
            r1 = requests.post(url=url, proxies={"https": f"https://{self._proxy}"}, verify=False, timeout=10)
            if r1.status_code==200:
                with open(self._filename[0:10] + '_temp.list', 'a+') as f:
                    f.write('{0}\n'.format(format(self._proxy)))
            else:
                pass
        except :
            pass

