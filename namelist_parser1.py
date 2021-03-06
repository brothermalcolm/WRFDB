# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 17:00:53 2017

@author: SERNMO
"""

import re
import pandas as pd

fhand = open('./data/namelist.input')
classes = []
fields = []
namelist = {}

for line in fhand:
    line = line.rstrip()
    name = re.findall('^\s*(\S+)', line)
    if len(name) == 0:
        continue
    if re.search('/', name[0]):
        continue
    if re.search('^!', name[0]):
        continue
    if re.search('^&', name[0]):
        print()
        print('name_class is:', name[0])
        classe = name[0] 
        classes.append(name[0])
    else:
        #print('name_field is:', name[0])
        value = re.findall('=\s*(.*)', line)
        value = value[0].split(',')
        try:
            value.remove('')
        except ValueError:
            pass
        #print('values are:', value)
        field = name[0]
        fields.append(name[0])
        print('%s : %s' % (field, value))
        namelist[field] = value
        
df = (pd.DataFrame.from_dict(namelist, orient='index')
        .rename(columns={0:'d1',1:'d2',2:'d3',3:'d4'}))
