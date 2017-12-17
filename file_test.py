#!/usr/bin/env python

'''
fp = open('通讯录.txt','wb')
mail_list = ['张三', 1809809990809, '李四', 494583948299, 'rtr']
for i in mail_list:
    fp.write(i.encode('utf-8') + b'\n')
fp.close()
'''

file_1 = open('通讯录.txt', 'rb')
a = file_1.readlines()
print(a)
file_1.close()
