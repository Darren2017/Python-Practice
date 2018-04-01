#-*-coding:utf-8-*-

import requests
import os

path = "/Users/darren/Pictures/abc.mp4"
url = "https://v.stu.126.net/mooc-video/nos/mp4/2017/03/07/1005926034_cbc3e80d4e20437ba300c88ece789d42_shd.mp4?ak=f1d079e752df40c9f2415d0e3c69a18f8eca9dfec01d528f6df24f2ffaea58cb635e00453296b91231655b90cb96106ceff6a55d15491982836e42383e13363e08f378e8261b44b439695a93c870697d1e46d140b7b30f910299bee40b26a5c2d9e1e3c44585e5de5b539ccdbe8423a821b91261e44e538d2765af73aa008299a7f5cc498d43fe59a782bc973c30c066b767da1f870bc890754ea6567cb70ca9830b67d08aac63e1ac0c534090a89323f6fd9d4e9030d5d8cb0cb4b5fcb8e77c"

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