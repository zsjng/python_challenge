# -*- coding = utf-8 -*-
# @Time :  下午11:02
# @Author : zsjng
# @File : 01.py
# @Software : PyCharm
str1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\
'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


# print(str1)
# print(ord('a'))
# print(ord('z'))
# just change the alpha. use chr ord

def change(str1):
    str2 = ''
    for i in str1:
        if ord(i) in range(97, 123):
            if ord(i) > 120:
                str2 += chr(ord(i) - 24)
            else:
                str2 += chr(ord(i) + 2)
        else:
            str2 += i
    return str2


print(change(str1))
print(change(r'http://www.pythonchallenge.com/pc/def/map.html'))
# jvvr://yyy.ravjqpejcnngpig.eqo/re/fgh/ocr.jvon
# next level is http://www.pythonchallenge.com/pc/def/ocr.html
