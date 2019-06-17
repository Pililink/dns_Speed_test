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
