# -*- coding: utf-8 -*-
"""
Created on Sun May 26 18:21:21 2019

@author: hexie
"""
import os
import util
import pandas as pd
from get_layer_info import get_layer_info

JOURNALS=['PR','PRAPPLIED','PRA','PRB','PRC','PRD','PRE',
          'PRI','PRL','PRSTAB','PRSTPER','PRX','RMP']
ROOT= 'C:/Users/hexie/Documents/APS-papers-data-010417-take2/aps-metadata/aps-dataset-metadata-2015/PRX'
INFO= ['name','authors','institutions','date','area']


def get_authors(start, number_of_papers):

    authors=[]
    for i in range(start, number_of_papers):
        mydict= util.get_idx_info(INFO,i)
        authors=authors+mydict['authors']
    
    author_id = list(set(authors))
    edge_list=[]
    for j in author_id:
        edge_list_j = [i for i, e in enumerate(authors) if e == j]
        if len(edge_list_j)>1:
            edge_list.append(edge_list_j)
        return author_id


def get_instituitions(start, number_of_papers):

    ins=[]
    for i in range(start, number_of_papers):
        mydict= util.get_idx_info(INFO,i)
        ins=ins+mydict['institutions']
    
    ins_id = list(set(ins))
    edge_list=[]
    for j in ins_id:
        edge_list_j = [i for i, e in enumerate(ins) if e == j]
        if len(edge_list_j)>1:
            edge_list.append(edge_list_j)
    
    return ins_id

def get_areas(start, number_of_papers):

    areas=[]
    for i in range(start, number_of_papers):
        mydict= util.get_idx_info(INFO,i)
        areas=areas+mydict['area']
    
    areas_id = list(set(areas))
    edge_list=[]
    for j in areas_id:
        edge_list_j = [i for i, e in enumerate(areas) if e == j]
        if len(edge_list_j)>1:
            edge_list.append(edge_list_j)
    
    return areas_id



def get_adj_matrix(start, number_of_papers, end_date):
    edge_list = None
    for i in range(start, number_of_papers):
        mydict = util.get_idx_info(INFO,i)
        edge_list =  util.to_edgelist_co_area_ins(edge_list, mydict, end_date)
    
    return edge_list


numbers= [40, 77,97,226,177]

end_date = "2016-05-27"
end_date = util.get_date(end_date)
ins_list = get_instituitions(441,617)
area_list= get_areas(441,617)
area_list= area_list[1:]

edge_list = get_adj_matrix(441,617, end_date)



try: 
    journal_volume="PRX_5"
    os.mkdir("C:/Users/hexie/Documents/APS_result/"+str(journal_volume))
except:
    journal_volume="PRX_5"
    print("already here")
for area in area_list:
    edges=[]
    for item in edge_list:
        if item[1]==area:
            edges.append((item[0][0], item[0][1],item[2]))
    get_layer_info(area, journal_volume, edges)            
    




#pd.DataFrame(A).to_csv("C:/Users/hexie/Documents/APS/PRX.csv",index=False, header=False)      