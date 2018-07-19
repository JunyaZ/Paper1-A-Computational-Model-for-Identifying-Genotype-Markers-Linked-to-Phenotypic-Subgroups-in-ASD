import pandas as pd
from sklearn.preprocessing import OneHotEncoder
inputData = pd.read_csv("47_SNPs.csv")
print(inputData)
df_2 = pd.get_dummies(inputData,drop_first=True)
df_2.to_csv("47_snpOneHot.csv",index=False)
