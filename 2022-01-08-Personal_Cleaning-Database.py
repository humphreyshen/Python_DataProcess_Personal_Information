import pandas as pd 
import numpy as np
from pandas._libs.tslibs import NullFrequencyError
from pandas.core.dtypes.missing import notna

df_personal_origin=pd.read_csv('/Users/humphreyshen/Desktop/2021 Database Project/001總表最新資料/2022-01-07_updated_csv/dDt_alumnidb_personal.csv')

email_result=[]
for i in df_personal_origin.email:
    if i == i | i !='NaN':
        email_result.append(i)
        
count=len(email_result)
print(count)
#print(count)

#duplitcated_mask=df_personal_origin.duplicated(subset=['email'],keep='first')
#duplitcated_email=df_personal_origin.dropna(subset=['email'])[duplitcated_mask]
#print(duplitcated_email['email'])