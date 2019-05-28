# -*- coding: utf-8 -*-
"""
Created on Sun May 26 19:05:30 2019

@author: hexie
"""

import pandas as pd
import os
#
#JOURNALS=['PR','PRAPPLIED','PRA','PRB','PRC','PRD','PRE',
#          'PRI','PRL','PRSTAB','PRSTPER','PRX','RMP']
JOURNALS=['PRX']
ROOT= 'C:/Users/hexie/Documents/APS-papers-data-010417-take2/aps-metadata/aps-dataset-metadata-2015/PRX'

path=[]
name=[]

for subdir, dirs, files in os.walk(ROOT):
    for file in files:
        if file.endswith('.json'):    
            mypath = os.path.join(subdir, file)
            name.append(str(file))
            path.append(mypath)
        

list_of_tuples = list(zip(name, path))
df = pd.DataFrame(list_of_tuples, columns = ['name', 'path']) 
df.to_csv('idx_map.csv',index=False)