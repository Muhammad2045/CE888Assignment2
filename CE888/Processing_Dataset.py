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

#os.mkdir("dataProcessed")
save_path="CE888/dataProcessed"

final_columns = {
    'ACC': ['id', 'X', 'Y', 'Z', 'datetime'],
    'EDA': ['id', 'EDA', 'datetime'],
    'HR': ['id', 'HR', 'datetime'],
    'TEMP': ['id', 'TEMP', 'datetime'],
    'BVP': ['id', 'BVP', 'datetime'],
    #'IBI': ['id', 'IBI', 'datetime'],
    
}

names = {
    'ACC.csv': ['X', 'Y', 'Z'],
    'EDA.csv': ['EDA'],
    'HR.csv': ['HR'],
    'TEMP.csv': ['TEMP'],
    'BVP.csv': ['BVP'],
    #'IBI.csv': ['IBI'],
}

#desired_signals = ['ACC.csv', 'EDA.csv', 'HR.csv', 'TEMP.csv','BVP.csv','IBI.csv']
desired_signals = ['ACC.csv', 'EDA.csv', 'HR.csv', 'TEMP.csv','BVP.csv']

acc = pd.DataFrame(columns=final_columns['ACC'])
eda = pd.DataFrame(columns=final_columns['EDA'])
hr = pd.DataFrame(columns=final_columns['HR'])
temp = pd.DataFrame(columns=final_columns['TEMP'])
BVP = pd.DataFrame(columns=final_columns['BVP'])
#IBI = pd.DataFrame(columns=final_columns['IBI'])

def process_df(df, file):
    start_timestamp = df.iloc[0,0]
    sample_rate = df.iloc[1,0]
    new_df = pd.DataFrame(df.iloc[2:].values, columns=df.columns)
    new_df['id'] =  file[-2:]
    new_df['datetime'] = [(start_timestamp + i/sample_rate) for i in range(len(new_df))]
    return new_df
    
for file in os.listdir(data_path)[14:15]:
    print(f'Processing {file}')
    for sub_file in os.listdir(os.path.join(data_path, file)):
        if not sub_file.endswith(".zip"):
            for signal in os.listdir(os.path.join(data_path, file, sub_file)):
                if signal in desired_signals:
                    df = pd.read_csv(os.path.join(data_path, file, sub_file, signal), names=names[signal], header=None)
                    if not df.empty:
                        if signal == 'ACC.csv':
                            acc = pd.concat([acc, process_df(df, file)])             
                        if signal == 'EDA.csv':
                            eda = pd.concat([eda, process_df(df, file)])
                        if signal == 'HR.csv':
                            hr = pd.concat([hr, process_df(df, file)])
                        if signal == 'TEMP.csv':
                            temp = pd.concat([temp, process_df(df, file)])
                        if signal == 'BVP.csv':
                            BVP = pd.concat([hr, process_df(df, file)])
                        if signal == 'IBI.csv':
                            IBI = pd.concat([temp, process_df(df, file)])

print('Saving Data ...')
acc.to_csv(os.path.join(save_path, 'combined_acc.csv'), index=False)
eda.to_csv(os.path.join(save_path, 'combined_eda.csv'), index=False)
hr.to_csv(os.path.join(save_path, 'combined_hr.csv'), index=False)
temp.to_csv(os.path.join(save_path, 'combined_temp.csv'), index=False)
BVP.to_csv(os.path.join(save_path, 'combined_bvp.csv'), index=False)
