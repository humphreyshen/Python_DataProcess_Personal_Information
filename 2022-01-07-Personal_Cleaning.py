import pandas as pd 
import numpy as np

original_personal=pd.read_csv('/Users/humphreyshen/Desktop/2021 Database Project/003數據預處理/Personal處理/2022-01-07/2022-01-07-dDt_alumnidb_personal.csv')
clean_personal=original_personal.replace({'\r':''},regex=True).replace(' ','',regex=True)
print(clean_personal.head(10))

clean_personal.to_csv('dDt_alumnidb_personal.csv',encoding='utf-8-sig')