import numpy as np
import pandas as pd
from collections import Counter
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

%matplotlib inline

data = pd.read_csv('159_matrix_numminmax_Nom.csv',header = None) 
# #############################################################################

def CateFunc(x,y):
    return (np.sum(np.not_equal(x,y)))/20

# Compute DBSCAN
model = DBSCAN(eps=1.8, min_samples=3 ,metric = CateFunc).fit(data)
outliers_df = pd.DataFrame(data)
print(model)
print (Counter(model.labels_))
print(model.labels_)
#np.savetxt("labels_dascan.csv", model.labels_)
outliers_df[model.labels_== -1]


kmeans = KMeans(n_clusters=500, random_state=0).fit(data)
kmeans.labels_
print (Counter(kmeans.labels_))
#np.savetxt("labels_kmeans.csv", model.labels_)

