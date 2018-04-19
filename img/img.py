# -*- coding:UTF-8 -*-
import requests
if __name__ == '__main__':
    target = 'https://unsplash.com/search/photos/red'
    req = requests.get(url=target)
    print(req.text)

