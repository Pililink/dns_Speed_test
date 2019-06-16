#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import Windows
import Linux


#获取dns列表
dnslist = open('dns.txt', 'r', encoding='utf-8')
dns_list = dnslist.read().split('\n')
dnslist.close()

#获取测试网址
htmllist=open('html.txt', 'r', encoding='utf-8')
html_list=htmllist.read().split('\n')
htmllist.close()

#判断系统
local_systeam=os.name
if local_systeam == 'nt':
    Windows.run(dns_list,html_list)
if local_systeam=='posix':
    Linux.run(dns_list, html_list)







'''
ms_list={}
for x in dns_list:
    num=0
    if x[0] != '#':
        print("-----------------------------------------")
        for y in html_list:
            a = 'dig\\dig64.exe @' + x + " " + y
            print(format(x + ' ' + y, '<30'), '响应时间：', end='')
            i=0
            ms=0
            while i<10:
                zz=os.popen(a)
                z=zz.readlines()[-5]
                m = re.search('[1-9]\d*', z)
                ms=ms+int(m.group())
                i=i+1
            ms=round(ms/10,2)
            num=num+ms
            print(ms)
        ms_list[x]=str(round(num/htmllen,2))
ms=999999.0
        #print(x," ms = ",num/htmllen)
print("===========================================================")

for key in ms_list:
       print(format(key,'<20'),end="")
       print('平均响应时间：'+ms_list[key])
       if float(ms_list[key])<ms:
           ms=float(ms_list[key])
print("===========================================================")
min=list(ms_list.keys())[list(ms_list.values()).index(str(ms))]
print('最优：',min,' 平均响应时间：',round(ms,2))'''