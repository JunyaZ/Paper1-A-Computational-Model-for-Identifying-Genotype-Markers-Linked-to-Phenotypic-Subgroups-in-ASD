import pandas as pd
import numpy as np
import multiprocessing as mp

#read the file and delimte to colums

mypath = "\\\\egr-1l11qd2\\CLS_lab\\Junya Zhao\\GWAS SNPs_2018\\newGWAS_data_April18\\"
def GetProband_id(filename, infile, outfile):
    list_= []
    with open (filename) as f :
        for i in f:
            a = i.strip('\n')  # delete the \n in each line
            list_.append(a)
    print(list_)
    with open(infile) as read_file, open(outfile,"w") as out_file:
        header = next(read_file)
        out_file.write(header)
        for read_line in read_file:
            if any ([read_line.startswith(id) for id in list_]):
                out_file.write(read_line)
def filter(filename):
    df = pd.read_csv(outfile, header=None, delimiter=' ')
    df = df[df[8] >= 0.05]
    df = df[df[7] != '-']
    df = df[df[6] != '-']
    # output the csv
    df.to_csv(mypath + "gwas_omni25_output.csv")
    # count the unique number of genoid
    num_1 = df[1].nunique()
    num_3 = len(df)
    print("The unique number is  ", num_1)
    print("The final total number is", num_3)
    print(df[1].unique)


if __name__ == "__main__":
    filename = mypath + "proband_list.csv"
    infile = mypath +"gwas_omni25.csv"
    outfile = mypath + "gwas_omni25_out.csv"
    GetProband_id(filename, infile, outfile)
    print("getData done")
    filter(outfile)

