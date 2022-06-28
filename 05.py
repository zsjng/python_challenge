# -*- coding = utf-8 -*-
# @Time :  上午12:20
# @Author : zsjng
# @File : 05.py
# @Software : PyCharm

# check sources.
import urllib.request
import pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"

with urllib.request.urlopen(url) as f:
    # print(pickle.load(f))
    for r in pickle.load(f):
        for i in r:
            for k in range(i[1]):
                print(i[0], end='')
        print()
# next level is http://www.pythonchallenge.com/pc/def/channel.html