# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 20:07:44 2019

@author: hexie
"""
import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.centrality as nxc

def get_layer_info(subject, journal_volume, edge_list):
    
    G = nx.Graph()
    G.add_weighted_edges_from(edge_list)
    
    PATH = "C:/Users/hexie/Documents/APS_result/"+str(journal_volume)+"/"+str(subject)
    
    try:
        os.mkdir(PATH)
        os.chdir(PATH)
    except:
        os.chdir(PATH)
    
    
    degree_centrality = nxc.degree_centrality(G)
    try:
        eigen_vector_centrality= nxc.eigenvector_centrality(G)
        np.save("eigen_vector_centrality.npy",eigen_vector_centrality)
    except:
        print("fail to converge within 100 iterations of power")
    
    closeness_centrality=nxc.closeness_centrality(G)
    betweeness_centrality=nxc.betweenness_centrality(G)
    
    np.save("degree_centrality.npy",degree_centrality)
    np.save("closeness_centrality.npy",closeness_centrality)
    np.save("betweeness_centrality.npy",betweeness_centrality)
    
    with open(str(subject)+str(journal_volume)+".txt", 'w') as f:
        f.write('Number of Edges: '+ str(nx.number_of_edges(G))+ "\n")
        f.write('Number of Nodes: '+ str(nx.number_of_nodes(G))+ "\n")
        
    nx.draw(G)
    plt.savefig(str(subject)+str(journal_volume)+".png")
    plt.clf()
    
    
  