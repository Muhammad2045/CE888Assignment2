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

data_path="CE888/stressDataset" #Main working directory path

#os.mkdir("stressDataset") #create directory to store unzip data
fr="CE888/Stress_dataset.zip"   #reading stress data zip folder
with ZipFile(fr, 'r') as file:  #ZipeFile is a function from zipfile build in python library to read the zipfiles data
    for i in file.namelist():
        #print(i)
        file.extract(i,'CE888/stressDataset')#namelist() is a function from zipfile to get the list of all the folders from the zip file
    
for root,dirs,files in os.walk(r"CE888/stressDataset"): #help read sub directories 
    for filenames in files:  #read sub directories name
        #print(root.split("/"))
        path = root+"/"+filenames.split(".")[0] #to unzip sub directories data
        #print(path)
        os.mkdir(path) #create directories to store unzip data
        if os.path.exists(path): #to check if the directory is already present or not
            #print(filenames, root)
            filename=root+ "/" + filenames  #combine the file name
            #print(filename, path)
            shutil.unpack_archive(filename, path)  #unzip the files
print("Done")
