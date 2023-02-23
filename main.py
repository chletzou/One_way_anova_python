import numpy as np
import pandas as pd
from statsmodels.stats.anova import AnovaRM
import csv
from objects import test
from objects import game
from objects import user


def main():
    #開啟csv並讀取進list
    with open ('form.csv', newline='', encoding='UTF-8') as f:
        reader = csv.reader(f)
        data_list = list(reader)
        #print(data_list)
    num_row = len(data_list[1])
    num_col = len(data_list)-1 #扣掉上面那一排題目敘述
    #print(data_list[1][8])
    #print(data_list[1][33])
    #print(data_list[1][58])
    #print(data_list[1][83])
    #print(num_col)
    #print(num_row)

    #存進
    for i in range(1, num_col):
        globals()['user'+str(i)] = user(data_list[1][8], data_list[1][33], data_list[1][58], data_list[1][83])
        #process_list = list[]
        process_list = list.append(globals()['user'+str(i)] )
        print('process_list[1]')

    
    

    

def anova(f):
    #perform the repeated measures ANOVA
    print (AnovaRM(data=f, depvar= 'score', subject= 'id',  within= ['type']).fit())

if __name__ == '__main__':
    main()
    #anova()