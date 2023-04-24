import pandas as pd

#combing_all_nurses data into one file
data = ['15','5C','6B','6D','7A','7E','83','8B','94','BG','CE','DF','E4','EG','F5']
PATH = 'CE888/working'
df_15 = pd.read_csv(os.path.join(PATH, 'merged_data_label_15.csv'), dtype={'id': str})
df_5C = pd.read_csv(os.path.join(PATH, 'merged_data_label_5C.csv'), dtype={'id': str})
df_6B = pd.read_csv(os.path.join(PATH, 'merged_data_label_6B.csv'), dtype={'id': str})
df_6D = pd.read_csv(os.path.join(PATH, 'merged_data_label_6D.csv'), dtype={'id': str})
df_7A = pd.read_csv(os.path.join(PATH, 'merged_data_label_7A.csv'), dtype={'id': str})
df_7E = pd.read_csv(os.path.join(PATH, 'merged_data_label_7E.csv'), dtype={'id': str})
df_83 = pd.read_csv(os.path.join(PATH, 'merged_data_label_83.csv'), dtype={'id': str})
df_8B = pd.read_csv(os.path.join(PATH, 'merged_data_label_8B.csv'), dtype={'id': str})
df_94 = pd.read_csv(os.path.join(PATH, 'merged_data_label_94.csv'), dtype={'id': str})
df_BG = pd.read_csv(os.path.join(PATH, 'merged_data_label_BG.csv'), dtype={'id': str})
df_CE = pd.read_csv(os.path.join(PATH, 'merged_data_label_CE.csv'), dtype={'id': str})
df_DF = pd.read_csv(os.path.join(PATH, 'merged_data_label_DF.csv'), dtype={'id': str})
df_E4 = pd.read_csv(os.path.join(PATH, 'merged_data_label_E4.csv'), dtype={'id': str})
df_EG = pd.read_csv(os.path.join(PATH, 'merged_data_label_EG.csv'), dtype={'id': str})
df_F5 = pd.read_csv(os.path.join(PATH, 'merged_data_label_F5.csv'), dtype={'id': str})

frames=[df_15,df_5C,df_6B,df_6D,df_7A,df_7E,df_83,df_8B,df_94,df_BG,df_CE,df_DF,df_E4,df_EG,df_F5]

results = pd.concat(frames)
print(pd.unique(results['id']))
  
  #print(pd.unique(df['id']))

print('Saving ...')
results.to_csv(os.path.join(PATH, 'merged_data_label.csv'),index=False)

print('Done')
