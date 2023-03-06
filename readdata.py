import csv
import os
import glob
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

    for cur_col in range(1, num_col):
        i=1 #命名index用的參數
        for cur_row in range(1, num_row ):
            if data_list[0][cur_row] == '遊戲體驗模式':
                globals()['test'+str(cur_col)+'_'+str(i)] = test(data_list[cur_col][cur_row], data_list[cur_col][cur_row+1], data_list[cur_col][cur_row+2], data_list[cur_col][cur_row+3], data_list[cur_col][cur_row+4])
                i+=1     
    #print(globals()['test'+str(2)+'_'+str(1)].imm)
    
    #存test 進 game

    for cur_col in range(1, num_col):
        j=1 #命名index用的參數
        k=1 #標示test1-k的參數
        for cur_row in range(1, num_row//2 ):
            if data_list[0][cur_row] == '現在進行的遊戲':
                globals()['game'+str(cur_col)+'_'+str(j)] = game(data_list[cur_col][cur_row], globals()['test'+str(cur_col)+'_'+str(k)], globals()['test'+str(cur_col)+'_'+str(k+1)], globals()['test'+str(cur_col)+'_'+str(k+6)], globals()['test'+str(cur_col)+'_'+str(k+7)] )
                j+=1
                k+=2      
    #(game1_1.A.imm)

    # 存game 進 user
    for cur_col in range(1, num_col):
        globals()['user'+str(cur_col)] = user(globals()['game'+str(cur_col)+'_'+str(1)], globals()['game'+str(cur_col)+'_'+str(2)], globals()['game'+str(cur_col)+'_'+str(3)])       
    #print(user1.G1.A.type)

    #建data的資料夾
    data_dir = './data'
    if not os.path.isdir(data_dir):
        os.mkdir(data_dir)
    #if not os.path.isdir (os.path.join(data_dir))
    
    #寫24個csv 存 3個遊戲 -> A/B、A/C test -> 4個分數(imm, rea, enj, com)
    # G1
    # G1_A/B
    # G1_A/B_imm
    with open('./data/HLA_AB_imm.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G1.A.type, 'score': globals()['user'+str(cur_col)].G1.A.imm})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G1.B.type, 'score': globals()['user'+str(cur_col)].G1.B.imm})
    
    #G1_A/B_rea
    with open('./data/HLA_AB_rea.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G1.A.type, 'score': globals()['user'+str(cur_col)].G1.A.rea})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G1.B.type, 'score': globals()['user'+str(cur_col)].G1.B.rea})    
    
    # G1_A/B_enj
    with open('./data/HLA_AB_enj.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G1.A.type, 'score': globals()['user'+str(cur_col)].G1.A.enj})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G1.B.type, 'score': globals()['user'+str(cur_col)].G1.B.enj})
    
    # G1_A/B_com
    with open('./data/HLA_AB_com.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G1.A.type, 'score': globals()['user'+str(cur_col)].G1.A.com})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G1.B.type, 'score': globals()['user'+str(cur_col)].G1.B.com})    
    
    # G1_A/C
    # G1_A/C_imm
    with open('./data/HLA_AC_imm.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G1.C.type, 'score': globals()['user'+str(cur_col)].G1.C.imm})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G1.D.type, 'score': globals()['user'+str(cur_col)].G1.D.imm})
    
    #G1_A/C_rea
    with open('./data/HLA_AC_rea.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G1.C.type, 'score': globals()['user'+str(cur_col)].G1.C.rea})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G1.D.type, 'score': globals()['user'+str(cur_col)].G1.D.rea})    
    
    # G1_A/C_enj
    with open('./data/HLA_AC_enj.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G1.C.type, 'score': globals()['user'+str(cur_col)].G1.C.enj})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G1.D.type, 'score': globals()['user'+str(cur_col)].G1.D.enj})
    
    # G1_A/C_com
    with open('./data/HLA_AC_com.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G1.C.type, 'score': globals()['user'+str(cur_col)].G1.C.com})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G1.D.type, 'score': globals()['user'+str(cur_col)].G1.D.com})    

    # G2
    # G2_A/B
    # G2_A/B_imm
    with open('./data/B&C_AB_imm.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G2.A.type, 'score': globals()['user'+str(cur_col)].G2.A.imm})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G2.B.type, 'score': globals()['user'+str(cur_col)].G2.B.imm})
    
    # G2_A/B_rea
    with open('./data/B&C_AB_rea.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G2.A.type, 'score': globals()['user'+str(cur_col)].G2.A.rea})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G2.B.type, 'score': globals()['user'+str(cur_col)].G2.B.rea})    
    
    # G2_A/B_enj
    with open('./data/B&C_AB_enj.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G2.A.type, 'score': globals()['user'+str(cur_col)].G2.A.enj})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G2.B.type, 'score': globals()['user'+str(cur_col)].G2.B.enj})
    
    # G2_A/B_com
    with open('./data/B&C_AB_com.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G2.A.type, 'score': globals()['user'+str(cur_col)].G2.A.com})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G2.B.type, 'score': globals()['user'+str(cur_col)].G2.B.com})    
    
    # G2_A/C
    # G2_A/C_imm
    with open('./data/B&C_AC_imm.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G2.C.type, 'score': globals()['user'+str(cur_col)].G2.C.imm})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G2.D.type, 'score': globals()['user'+str(cur_col)].G2.D.imm})
    
    # G2_A/C_rea
    with open('./data/B&C_AC_rea.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G2.C.type, 'score': globals()['user'+str(cur_col)].G2.C.rea})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G2.D.type, 'score': globals()['user'+str(cur_col)].G2.D.rea})    
    
    # G2_A/C_enj
    with open('./data/B&C_AC_enj.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G2.C.type, 'score': globals()['user'+str(cur_col)].G2.C.enj})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G2.D.type, 'score': globals()['user'+str(cur_col)].G2.D.enj})
    
    # G2_A/C_com
    with open('./data/B&C_AC_com.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G2.C.type, 'score': globals()['user'+str(cur_col)].G2.C.com})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G2.D.type, 'score': globals()['user'+str(cur_col)].G2.D.com})    

    # G3
    # G3_A/B
    # G3_A/B_imm
    with open('./data/Beat_AB_imm.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G3.A.type, 'score': globals()['user'+str(cur_col)].G3.A.imm})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G3.B.type, 'score': globals()['user'+str(cur_col)].G3.B.imm})
    
    # G3_A/B_rea
    with open('./data/Beat_AB_rea.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G3.A.type, 'score': globals()['user'+str(cur_col)].G3.A.rea})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G3.B.type, 'score': globals()['user'+str(cur_col)].G3.B.rea})    
    
    # G3_A/B_enj
    with open('./data/Beat_AB_enj.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G3.A.type, 'score': globals()['user'+str(cur_col)].G3.A.enj})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G3.B.type, 'score': globals()['user'+str(cur_col)].G3.B.enj})
    
    # G3_A/B_com
    with open('./data/Beat_AB_com.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G3.A.type, 'score': globals()['user'+str(cur_col)].G3.A.com})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G3.B.type, 'score': globals()['user'+str(cur_col)].G3.B.com})    
    
    # G3_A/C
    # G3_A/C_imm
    with open('./data/Beat_AC_imm.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G3.C.type, 'score': globals()['user'+str(cur_col)].G3.C.imm})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G3.D.type, 'score': globals()['user'+str(cur_col)].G3.D.imm})
    
    # G3_A/C_rea
    with open('./data/Beat_AC_rea.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G3.C.type, 'score': globals()['user'+str(cur_col)].G3.C.rea})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G3.D.type, 'score': globals()['user'+str(cur_col)].G3.D.rea})    
    
    # G3_A/C_enj
    with open('./data/Beat_AC_enj.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G3.C.type, 'score': globals()['user'+str(cur_col)].G3.C.enj})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G3.D.type, 'score': globals()['user'+str(cur_col)].G3.D.enj})
    
    # G3_A/C_com
    with open('./data/Beat_AC_com.csv', 'w', newline='') as f:
        #寫標題進表格
        field_name = ['id', 'type', 'score']
        writer = csv.DictWriter(f, fieldnames = field_name)
        #寫入標題欄位
        writer.writeheader()
        #分別寫 id, type, score進去
        for cur_col in range(1, num_col):
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G3.C.type, 'score': globals()['user'+str(cur_col)].G3.C.com})
            writer.writerow({'id': cur_col, 'type': globals()['user'+str(cur_col)].G3.D.type, 'score': globals()['user'+str(cur_col)].G3.D.com})    
