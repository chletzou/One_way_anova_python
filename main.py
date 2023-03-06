import numpy as np
import pandas as pd
from statsmodels.stats.anova import AnovaRM
import csv
import os
import glob
from readdata import read_data

def anova():
    #建result的資料夾
    data_dir = './data'
    result_dir = './result'
    if not os.path.isdir(result_dir):
        os.mkdir(result_dir)

    #perform the repeated measures ANOVA
    #列出資料夾data中所有csv
    allcsv = os.listdir('./data')
    #print(allcsv)
    for f in allcsv:
        file = pd.read_csv(os.path.join( data_dir +'/'+ f))
        #export the result
        result = AnovaRM(data=file, depvar= 'score', subject= 'id',  within= ['type']).fit()
        #print(result)
        table = result.anova_table
        #with open(os.path.join(result_dir+'/'+f), 'w', newline='') as csvfile:
        #    writer = csv.writer(csvfile)
        table.to_csv(os.path.join( result_dir +'/'+f ), sep = ',', index= True, header= True)
        #AnovaRM(datato_csv(os.path.join(result_dir+'/'+f), sep = ',', index= True, header= True )

def p_value():
    #讀檔名
    allcsv = os.listdir('./result')
    csv_name = []
    p_value = [[], []]
    for f in allcsv:
        #先把名字取出來
        csv_split = os.path.splitext(f)[0]
        csv_name.append(csv_split)
    for name in csv_name:
        with open (os.path.join( './result'+'/'+name+'.csv' ), newline='', encoding='UTF-8') as result:
            reader = csv.reader(result)
            csv_list = list(reader)
            #print(csv_list) 
            p_value[0].append(name)
            p_value[1].append(csv_list[1][4])
    #print(p_value)
    with open('p_value.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(p_value)
    


if __name__ == '__main__':
    read_data() #只要跑過一次產生csv就好
    anova()
    p_value()