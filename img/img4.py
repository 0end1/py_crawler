import requests
if __name__ == '__main__':
    target = 'https://unsplash.com/napi/search/photos?query=red&xp=&per_page=20&page=2'
    headers = {'authorization':'your Client-ID'}
    req = requests.get(url=target, headers=headers, verify=False)
    print(req.text)