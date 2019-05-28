# -*- coding: utf-8 -*-

import os
import json
import pandas as pd
import time
import datetime
import itertools
import networkx as nx
import numpy as np
from collections import Counter
"""
get_idx_info: return a dictionary with index information
get_idx_name: return a name that correspond to index
get_date: return a int that represent corresponding date
"""


JOURNALS=['PR','PRAPPLIED','PRA','PRB','PRC','PRD','PRE',
          'PRI','PRL','PRSTAB','PRSTPER','PRX','RMP']
ROOT= 'C:/Users/hexie/Documents/APS-papers-data-010417-take2/aps-metadata/aps-dataset-metadata-2015/PRX'
INFO= ['name','authors','institutions','date','area']

def get_idx_info(INFO, idx):
    """
    Returns the path to the requested data directory.
    example usage:
        get_idx_dir(journal_name="PRX", volume=1, idx=10)
    should return everything you need for this data set in a dictionary.
    i.e. you should get:
        'name' :'PhysRevX.1.010001',
        'journal': 'PRX',
        'authors': ['A','B','C'],
        'institution':['AA','BB','CC'],
        'date':[123]-a number representing year,date,and time.
        'area':['Quantum Physics','statistic','machine learning']
    """
    
    name,path =get_idx_name(idx)
    idx_dict = {}
    for field in INFO:
        idx_dict[field] = []
        
    with open(path) as json_file:  
        data = json.load(json_file)
        try:
            for p in data['authors']:
                idx_dict['authors'].append(p['name'])
        except:
            idx_dict['authors'].append('NOAUTHORS')
        
        try:
            
            for p in data['affiliations']:            
                idx_dict['institutions'].append(p['name'])
        
        except:
            idx_dict['institutions'].append('NOAFFLI')
        
        try:  
            p = data['classificationSchemes']['subjectAreas']            
            for x in p:
                idx_dict['area'].append(x['label'])
        except:
            idx_dict['area'].append('NOAREAS')
        
        
        idx_dict['date']= get_date(data['date'])  
        idx_dict['name']= name
    return idx_dict

def get_idx_name(idx):
    """
    Return filename of idx in the adjacency matrix
    example usage:
        name=get_idx_name(10)
        name='PhysRevX.1.011009'
    """
    maps = pd.read_csv('idx_map.csv')
    return maps['name'][idx],maps['path'][idx]
    
    
def get_date(date):
    #format="%Y-%m-%d %H:%M:%S"
    format="%Y-%m-%d"
    return time.mktime(datetime.datetime.strptime(date, format).timetuple())

def to_adj_matrix(edge_list):
    G= nx.Graph()
    G.add_edges_from(edge_list)
    A = nx.to_numpy_matrix(G)
    U = np.triu(A)
    L = np.tril(A)
    
    U_upper=np.triu_indices(len(U),1) 
    U[U_upper]=U.T[U_upper]
    
    L_lower=np.tril_indices(len(L),-1) 
    L[L_lower]=L.T[L_lower]

    A = U+L
    
    return A

def to_edgelist(my_edges, mydict, mydate):
    authors = mydict['authors']
    date = mydict['date']
    if date <= mydate :
        edge_list = list(itertools.combinations(authors, 2))
        if my_edges is not None:
            my_edges=my_edges+edge_list
        else:
            my_edges=edge_list
    output=[]
    counter=Counter(my_edges)
    author_pairs = list(set(my_edges))
    for x in author_pairs:
        output.append((x[0],x[1],counter[x]))
    
    print(output)
    
    return my_edges



