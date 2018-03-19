#-*-coding:utf-8-*-

import requests
import os

path = "/Users/darren/Pictures/abc.jpg"
url = "https://ps.ssl.qhmsg.com/t014e4a3f6893abfaef.jpg"

try:
    if not os.path.exists(path):
        r = requests.get(url)
        r.status_code
        with open (path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")