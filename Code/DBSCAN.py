# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 12:58:03 2018

@author: ya000
"""

import numpy as np
import pandas as pd
from collections import Counter
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
# #############################################################################
#data = pd.read_csv('winequality-red.csv') 
data = pd.read_csv('156_matrix_binary_output.csv',header = None) 
#data = pd.read_csv('153_matrix_all_num.csv')
#data = pd.read_csv('test.csv',header= None) 
def CateFunc(x,y):
    return (np.sum(np.not_equal(x,y)))/20
# #############################################################################
# Compute DBSCAN

model = DBSCAN(eps=1.8, min_samples=3 ,metric = CateFunc).fit(data)
outliers_df = pd.DataFrame(data)
print(model)
print (Counter(model.labels_))
print(model.labels_)
print("=====")
#np.savetxt("labels_dascan.csv", model.labels_)
print(outliers_df[model.labels_== -1])
for i in range(-1,299):
    outliers_df[model.labels_== i].to_csv(f"{'label'+str(i)}.csv")
        
        