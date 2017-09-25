#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re
import time
from time import gmtime, strftime

a = 0
n = 0
u = 0

var = 1
while var == 1 :
        with open ('/PATH01/'+strftime("%Y%m%d", gmtime()), 'r') as fjawfnblaiuew:
                lines = fjawfnblaiuew.readlines()
                last_line=lines[-1]
                print last_line
                try:
                        x = re.match(r"(?P<Date>\d{4}(\-\d{2}){2}) (?P<Time>\d{2}(\:\d{2}){2}) (?P<Msg>\w{7}|\w{7}\s\w{7}|\w{2}\s\w{7}) \: (?P<CMD>(\d\s){3}\d) \| accuracy \: (?P<AR>\d{2})", last_line)
                        if str(x.group(5)) == "unknown command":
                                a = 0
                                n = 0
                                u += 1
                                if u == 3:
                                        b = x.group(1) + " " + x.group(3) + " " +  "指令錯誤"
                                        f = open('/PATH/ans.txt', 'ab+')
                                        f.write(b + "\n")
                                        f.closed
                                        u = 0
                        elif str(x.group(5)) == "command" and int(x.group(8)) < 70:
                                a += 1
                                n = 0
                                u = 0
                                if a == 3:
                                        b = x.group(1) + " " + x.group(3) + " " + "準確度不夠"
                                        f = open('/PATH/ans.txt', 'ab+')
                                        f.write(b + "\n")
                                        f.closed
                                        a = 0
                except:
                        x = re.match(r"(?P<Date>\d{4}(\-\d{2}){2}) (?P<Time>\d{2}(\:\d{2}){2}) (?P<Msg>\w{7}|\w{7}\s\w{7}|\w{2}\s\w{7})", last_line)
                        if str(x.group(5)) == "no command":
                                a = 0
                                n += 1
                                u = 0
                                if n == 3:
                                        b = x.group(1) + " " + x.group(3) + " " + "沒指令"
                                        f = open('/PATH/ans.txt', 'ab+')
                                        f.write(b + "\n")
                                        f.closed
                                        n = 0
                time.sleep(5)
