# -*- coding:UTF-8 -*-
# force = true
import requests, json
if __name__ == '__main__':
    target = 'https://unsplash.com/napi/search/photos?query=red&xp=&per_page=20&page=2'
    headers = {'authorization':'Client-ID 72664f05b2aee9ed032f9f4084f0ab55aafe02704f8b7f8ef9e28acbec372d09'}
    req = requests.get(url=target, headers=headers, verify=False)
    html = json.loads(req.text)
    for each in html['results']:
        print('图片ID:',each['id'])