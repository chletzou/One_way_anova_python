import numpy as np
import pandas as pd
from statsmodels.stats.anova import AnovaRM
import csv
import os
from objects import test
from objects import game
from objects import user

num_col = list

def read_data():
    #開啟csv並讀取進nested list
    with open ('form.csv', newline='', encoding='UTF-8') as f:
        reader = csv.reader(f)
        data_list = list(reader)
        #print(data_list)
    num_row = len(data_list[1])
    globals()['num_col'] = len(data_list)
    #print(num_col)
    #print(num_row)

    #存資料進test
    i=1 #命名index用的參數
    for cur_col in range(1, num_col):
        for cur_row in range(1, num_row ):
            if data_list[0][cur_row] == '遊戲體驗模式':
                globals()['test'+str(cur_col)+'_'+str(i)] = test(data_list[cur_col][cur_row], data_list[cur_col][cur_row+1], data_list[cur_col][cur_row+2], data_list[cur_col][cur_row+3], data_list[cur_col][cur_row+4])
                i+=1
        i-=16     
    #print(globals()['test'+str(3)+'_'+str(8)].com)

    #存test 進 game
    j=1 #命名index用的參數
    for cur_col in range(1, num_col):
        k=1 #標示test1-k的參數
        for cur_row in range(1, num_row ):
            if data_list[0][cur_row] == '現在進行的遊戲':
                globals()['game'+str(cur_col)+'_'+str(j)] = game(data_list[cur_col][cur_row], globals()['test'+str(cur_col)+'_'+str(k)], globals()['test'+str(cur_col)+'_'+str(k+1)], globals()['test'+str(cur_col)+'_'+str(k+2)], globals()['test'+str(cur_col)+'_'+str(k+3)] )
                j+=1
                k+=4
        j-=4        
    #print(game4_4.D.com)

    # 存game 進 user
    for cur_col in range(1, num_col):
        globals()['user'+str(cur_col)] = user(globals()['game'+str(cur_col)+'_'+str(1)], globals()['game'+str(cur_col)+'_'+str(2)], globals()['game'+str(cur_col)+'_'+str(3)], globals()['game'+str(cur_col)+'_'+str(4)])       
    #print(user3.G4.D.type)

    #建data的資料夾
    data_dir = './data'
    if not os.path.isdir(data_dir):
        os.mkdir(data_dir)
    #if not os.path.isdir (os.path.join(data_dir))
    
    #寫32個csv 存 4個遊戲 -> A/B、A/C test -> 4個分數(imm, rea, enj, com)
    global num_col
    with open('./data/Half_life_alyx_AB.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        writer.writeheader()
        #分別寫 id, type, score進去
        for i in range(1, 2*(num_col-1)):
            writer.writerow({'id': 'user', 'type'})
    
    with open('./data/Half_life_alyx_AC', 'w') as f:
        pass
    with open('./data/_AB', 'w') as f:
        pass
    with open('./data/Half_life_alyx_AB', 'w') as f:
        pass

    

def anova(f):
    #perform the repeated measures ANOVA
    print (AnovaRM(data=f, depvar= 'score', subject= 'id',  within= ['type']).fit())

    #export the result

if __name__ == '__main__':
    read_data()
    #anova()