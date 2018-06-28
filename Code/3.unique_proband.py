import pandas as pd
import glob
import os
mypath = "\\\\egr-1l11qd2\\CLS_lab\\Junya Zhao\\GWAS SNPs_2018\\newGWAS_data_April18\\Allproband\\"
allFiles = glob.glob(mypath+'*.csv')
for csv in allFiles:
    frame = pd.read_csv(csv)
    total = frame['0'].count()
    frame['allele'] = frame[['5', '6']].apply(lambda x: ''.join(x), axis=1)
    print("unique", frame.allele.nunique())
    frame.rename(columns={'allele': os.path.basename(csv)}, inplace=True)
    frame.rename(columns={'2': "snpid"}, inplace=True)
    del frame['Unnamed: 0']
    del frame['Unnamed: 0.1']
    del frame['0']
    del frame['1']
    del frame['3']
    del frame['4']
    del frame['5']
    del frame['6']
    del frame['7']
    frame.to_csv(csv+".csv")
    print (csv, total)
