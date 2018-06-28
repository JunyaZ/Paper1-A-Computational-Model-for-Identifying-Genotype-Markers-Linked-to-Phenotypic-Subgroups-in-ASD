import os
import pandas as pd
import glob
import csv

df= pd.read_csv('C:\data\gwas.csv')
#creates a list of all csv files
globbed_files = glob.glob("*.csv") 

#data = pd.DataFrame() # pd.concat takes a list of dataframes as an agrument
for csv in globbed_files:
    frame = pd.read_csv(csv, index_col=None, header=0)
    #data.append(frame)
    df = df.merge(frame, how ='left', on=['snpid'])    
    #List = []
   # for i in merged:
     #   List.append(merged)
    #    merged = pd.concat(List, axis=1)
#final= df.fillna(0)
cols = [col for col in final if not col.startswith('Unnamed:')]
final[cols].to_csv('153_matrix.csv')
    
    #total = frame.snpid.count()
    #print (csv, total)
print(final)
