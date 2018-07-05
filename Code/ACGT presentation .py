
import os
import pandas as pd
import glob
import csv

#creates a list of all csv files
globbed_files = glob.glob("*.csv") 

data = [] # pd.concat takes a list of dataframes as an agrument
for csv in globbed_files:
    frame = pd.read_csv(csv)
    frame = frame.replace({"AA": 1,"AC": 2, "AG":3, "AT":4,'CC':6, 'CG':7, 'GG':11,"TT" :16})
    #frame = frame.replace({'TA' :13})
    data.append(frame)
    del frame['Unnamed: 0']
    frame.to_csv(csv)
    total = frame.snpid.count()
    print (csv, total)