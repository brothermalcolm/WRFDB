# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 17:00:53 2017

@author: SERNMO
"""

import re

fhand = open('namelist.input')

for line in fhand:
    line = line.rstrip()
    name = re.findall('^\s(\S+)', line)
    if len(name) == 0:
        continue
    if re.search('/', name[0]):
        continue
    if re.search('^!', name[0]):
        continue
    if re.search('^&', name[0]):
        print('name_class is:', name[0])
    else:
        print('name_field is:', name[0])
        value = re.findall('=\s*(.*)', line)
        value = value[0].split(',')
        print('values are:', value)

        