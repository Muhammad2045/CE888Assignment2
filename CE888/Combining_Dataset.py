import os
import zipfile 
import shutil
import numpy as np
import os,os.path,sys
import pandas as pd
import multiprocessing
from zipfile import ZipFile
from datetime import timedelta, datetime
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

#os.mkdir("work")
COMBINED_DATA_PATH = "CE888/dataProcessed"
SAVE_PATH = "CE888/working"

#if COMBINED_DATA_PATH != SAVE_PATH:
    #os.mkdir(SAVE_PATH)

print("Reading data ...")

acc, eda, hr, temp, bvp = None, None, None, None, None

signals = ['acc', 'eda', 'hr', 'temp','bvp']

def read_parallel(signal):
    print(f"combined_{signal}.csv")
    df = pd.read_csv(os.path.join(COMBINED_DATA_PATH, f"combined_{signal}.csv"), dtype={'id': str})
    return [signal, df]
results=[]
for signal in signals:
    temp=read_parallel(signal)
    results.append(temp)
#print(results)

for i in results:
    globals()[i[0]] = i[1]
    
#print(acc, eda, hr, temp)
# Merge data
#print('Merging Data ...')
ids = eda['id'].unique()
#print(ids)
columns=['X', 'Y', 'Z', 'EDA', 'HR', 'TEMP','BVP', 'id', 'datetime']

def merge_parallel(id):
    print(f"Processing {id}")
    df = pd.DataFrame(columns=columns)

    acc_id = acc[acc['id'] == id]
    eda_id = eda[eda['id'] == id].drop(['id'], axis=1)
    hr_id = hr[hr['id'] == id].drop(['id'], axis=1)
    temp_id = temp[temp['id'] == id].drop(['id'], axis=1)
    bvp_id = bvp[bvp['id'] == id].drop(['id'], axis=1)

    df = acc_id.merge(eda_id, on='datetime', how='outer')
    df = df.merge(temp_id, on='datetime', how='outer')
    df = df.merge(hr_id, on='datetime', how='outer')
    df = df.merge(bvp_id, on='datetime', how='outer')

    df.fillna(method='ffill', inplace=True)
    df.fillna(method='bfill', inplace=True)
    
    return df

for ID in ids:
    final_results=merge_parallel(ID)
    #print(final_results)
    final_results.to_csv(os.path.join(SAVE_PATH, "merged_data.csv"), mode='a',index=False)
print(SAVE_PATH,'finished')
