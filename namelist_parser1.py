# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 17:00:53 2017

@author: SERNMO
"""

import re

fhand = open('namelist.input')
names  = {}
regex = '^\s(\S+)'

for line in fhand:
    line = line.rstrip()
#    print(line)
    name = re.findall(regex, line)
    if len(name) > 0 and not re.search('/', name[0]):
        if re.search('^&', name[0]):
            print('name_class is:', name[0])
        else:
            print('name_field is:', name[0])