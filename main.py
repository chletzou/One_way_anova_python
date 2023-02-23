import numpy as np
import pandas as pd
from statsmodels.stats.anova import AnovaRM
import csv
from objects import test
from objects import game
from objects import user


def read_data():
    #開啟csv並讀取進nested list
    with open ('form.csv', newline='', encoding='UTF-8') as f:
        reader = csv.reader(f)
        data_list = list(reader)
        #print(data_list)
    num_row = len(data_list[1])
    num_col = len(data_list)
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
    
'''
    #存進
    for i in range(1, num_col):
        #globals()['user'+str(i)] = user(data_list[i][8], data_list[i][33], data_list[i][58], data_list[i][83])
        #process_list = list[]
        #process_list = list.append(globals()['user'+str(i)] )
        #print(globals()['user'+str(i)].G1)
        for j in range(1, 14, 4):
            globals()['game'+str(j)] = game(data_list[i][7+j], data_list[i][8+j], data_list[i][13+j], data_list[i][20+j], data_list[i][25+j])
            globals()['game'+str(j+1)] = game(data_list[i][32+j], data_list[i][8+j+1], data_list[i][13+j], data_list[i][20+j], data_list[i][25+j])
            globals()['game'+str(j+2)] = game(data_list[i][7+j+2], data_list[i][8+j+2], data_list[i][13+j], data_list[i][20+j], data_list[i][25+j])
            globals()['game'+str(j+3)] = game(data_list[i][7+j+3], data_list[i][8+j+3], data_list[i][13+j], data_list[i][20+j], data_list[i][25+j])

    #print(user1.G1)
    print(game2.A)
'''  

def write_data():
    with

    

def anova(f):
    #perform the repeated measures ANOVA
    print (AnovaRM(data=f, depvar= 'score', subject= 'id',  within= ['type']).fit())

    #export the result

if __name__ == '__main__':
    read_data()
    #write_data()
    #anova()