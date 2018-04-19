# -*- coding:UTF-8 -*-
import requests
if __name__ == '__main__':
    target = 'https://unsplash.com/napi/search/photos?query=red&xp=&per_page=20&page=2'
    req = requests.get(url=target, verify=False)
    print(req.text)