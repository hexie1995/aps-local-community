# -*- coding: utf-8 -*-
"""
Created on Sun May 26 18:21:21 2019

@author: hexie
"""
import util
JOURNALS=['PR','PRAPPLIED','PRA','PRB','PRC','PRD','PRE',
          'PRI','PRL','PRSTAB','PRSTPER','PRX','RMP']
ROOT= 'C:/Users/hexie/Documents/APS-papers-data-010417-take2/aps-metadata/aps-dataset-metadata-2015/PRX'
INFO= ['name','authors','institutions','date','area']


def get_authors(number_of_papers):

    authors=[]
    for i in range(number_of_papers):
        mydict= util.get_idx_info(INFO,i)
        authors=authors+mydict['authors']
    
    author_id = list(set(authors))
    edge_list=[]
    for j in author_id:
        edge_list_j = [i for i, e in enumerate(authors) if e == j]
        if len(edge_list_j)>1:
            edge_list.append(edge_list_j)
    
    return author_id

def get_adj_matrix(number_of_papers, end_date):
    edge_list = None
    for i in range(number_of_papers):
        mydict = util.get_idx_info(INFO,i)
        edge_list =  util.to_edgelist(edge_list, mydict, end_date)
    
    return util.to_adj_matrix(edge_list)


end_date = "2012-05-27"
end_date = util.get_date(end_date)

A = get_adj_matrix(6, end_date)



        