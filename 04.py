# -*- coding = utf-8 -*-
# @Time :  下午11:42
# @Author : zsjng
# @File : 04.py
# @Software : PyCharm
import re
from urllib import request

# find NOTHING!
find_nothing = re.compile(r'nothing is (\d*)')
numbers = '63579'

for _ in range(400):
    # the first website is http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
    link = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={numbers}'
    answer = request.urlopen(link)
    for i in answer:
        numbers = re.findall(find_nothing, str(i))[0]
        print(numbers)
    # error with 16044. Yes. Divide by two and keep going.
    # error with 82682. There maybe misleading numbers in the text. One example is 82683. Look only for the next nothing
    #                   and the next nothing is 63579
    # error with 66831.
    # next level is http://www.pythonchallenge.com/pc/def/peak.html