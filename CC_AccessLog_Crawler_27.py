#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
from bs4 import BeautifulSoup


r = requests.get('http://rate.bot.com.tw/xrt?Lang=zh-TW')
soup = BeautifulSoup(r.text, 'lxml')


data=[]
lns=['price','mon','dad','triger','mon1','dad1','triger1','mon2','dad2','triger2','mon3','dad3','triger3','mon4','dad4','triger4','mon5','dad5','triger5']

for i, j in enumerate(soup.find_all("td", attrs={"data-table":"本行現金買入", "class":"rate-content-cash text-right print_hide"})):
	print i,j.text
	data.append(lns[i])
	data.append(j.text)
#with open('somefile.txt', 'wb') as f:
#	json.dump(data, f)
#print data[0]
		


with open('somefile.txt', 'rb') as json_data:
    jvar = json.load(json_data)
print jvar[0] 

if data[1] == jvar[0]:
	print "the same" 
else:
	print "got the shit"


with open('somefile.txt', 'wb') as f:
        json.dump(data, f)
