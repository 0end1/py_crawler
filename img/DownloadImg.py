# -*- coding:UTF-8 -*-
import requests, json, time, sys
from contextlib import closing

class get_photos(object):

    def __init__(self):
        self.photos_id = []
        self.download_server = 'https://unsplash.com/photos/xxx/download?force=true'
        self.target = 'https://unsplash.com/napi/search/photos?query=red&xp=&per_page=20&page=1'
        self.headers = {'authorization':'Client-ID 72664f05b2aee9ed032f9f4084f0ab55aafe02704f8b7f8ef9e28acbec372d09'}

    """
    函数说明:获取图片ID
    Parameters:
        无
    Returns:
        无
    Modify:
        2018-04-19
    """
    def get_ids(self):
        req = requests.get(url=self.target, headers=self.headers, verify=False)
        html = json.loads(req.text)
        for each in html['results']:
            self.photos_id.append(each['id'])
        print(self.photos_id)
        for i in range(5):
            req = requests.get(url=self.target, headers=self.headers, verify=False)
            html = json.loads(req.text)
            for each in html['results']:
                self.photos_id.append(each['id'])
            time.sleep(1)
    """
    函数说明:图片下载
    Parameters:
        无
    Returns:
        无
    Modify:
        2018-04-19
    """ 
    def download(self, photo_id, filename):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        target = self.download_server.replace('xxx', photo_id)
        with closing(requests.get(url=target, stream=True, verify = False, headers = self.headers)) as r:
            with open('%d.jpg' % filename, 'ab+') as f:
                for chunk in r.iter_content(chunk_size = 5):
                    if chunk:
                        f.write(chunk)
                        f.flush()    


if __name__ == '__main__':
    gp = get_photos()
    print('获取图片连接中:')
    gp.get_ids()
    print('图片下载中:')
    for i in range(len(gp.photos_id)):
        if i <= 4:
            print('正在下载第%d张图片' % (i+1))
            gp.download(gp.photos_id[i], (i+1))