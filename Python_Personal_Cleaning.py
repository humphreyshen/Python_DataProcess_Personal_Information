import pandas as pd
import numpy as np

print('\n\n==============================================\n歡迎使用由HumphreyShen所設計之個資整理程式\n==============================================\n')
print('請依序輸入您預計整理之資料檔案路徑」')
print('請注意，本程式所截取之檔案預設為CSV檔！如您輸入錯誤系統會主動提醒您！')

Path=()

while True:
    temp_input_1 = input ('\n\n >> 請先輸入您預計整理之資料檔案路徑：')
    if (temp_input_1 != 'Y') and ('.csv' in temp_input_1):
        Path=temp_input_1
        print('\n初步驗證正確，請在下方鍵入"Y"以做為確認')
    elif temp_input_1 == 'Y':
        break
    else:
        print('您似乎輸入了錯誤路徑或檔案，請檢查後重新輸入！\n')

original_personal=pd.read_csv(Path)
clean_personal=original_personal.replace({'\r':''},regex=True).replace(' ','',regex=True)

print(clean_personal.head(10))
print('\n↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑請確認上方由程式整理的前十筆資料↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑')
print('\n如無問題請於下方輸入匯出相關資訊')

check=()

while True:
    print('請注意，本程式預設輸出格式為CSV檔！如您輸入錯誤系統會主動提醒您！')
    temp_input_2=input ('您預計輸入的檔案名稱：')
    if (temp_input_2!= 'Y') and ('.csv' in temp_input_2):
        check=temp_input_2
    elif temp_input_2 == 'Y':
        break
    else:
        print('您似乎輸入了錯誤檔案名稱，請檢查後重新輸入！\n')
        
clean_personal.to_csv(check,encoding='utf-8-sig')

print('\n您的資料已輸出完成')