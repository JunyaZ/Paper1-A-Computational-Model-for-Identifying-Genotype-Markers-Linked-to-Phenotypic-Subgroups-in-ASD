import pandas as pd
mypath = "\\\\egr-1l11qd2.missouristate.edu\\CLS_lab\\Junya Zhao\\GWAS SNPs_2018\\newGWAS_data_April18\\"
df = pd.read_csv (mypath+"gwas_1mv3_output.csv",index_col=None).groupby('0')
print(df.ngroups)
df.apply(lambda x: x.to_csv(r'\\egr-1l11qd2.missouristate.edu\\CLS_lab\\Junya Zhao\\GWAS SNPs_2018\\newGWAS_data_April18\\Allproband\\{}.csv'.format(x.name)))
