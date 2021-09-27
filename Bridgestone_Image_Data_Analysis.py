#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os, os.path
import wget
import numpy as np


# ### Enter the path where the data files are stored

# In[ ]:


DIR = input("path:")
n=len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
n


# In[ ]:


from os.path import isfile, join
from os import listdir
onlyfiles = [f for f in listdir(DIR) if isfile(join(DIR, f))]
onlyfiles


# In[ ]:


c=[]
for i in range(0,n):
    c1=os.path.splitext(onlyfiles[i])[0]
    c.append(c1)


# In[ ]:


for i in range(0,n):
    if os.path.isfile(DIR):
        directory = c[i]
        parent_dir=DIR
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        print("Directory '%s' created" %directory)
           
    else:
        print('Folder exist')
        


# In[ ]:


onlyfiles


# In[ ]:


excel_files = []
csv_files=[]

for i in range(0,len(onlyfiles)):
    filename1 = onlyfiles[i]
    if ".xlsx" in filename1:
        excel_files.append(filename1)    
    else:
        csv_files.append(filename1)


# ### Working with a .xlsx files 

# In[ ]:


excel_files


# In[ ]:


path = input('Path: + /filename.xlsx')
d1=pd.read_excel(path)
d1=d1.drop(['Docket No','Damage Description','Engineer Name'],axis=1)


# In[ ]:


new_df = d1['Picture 1']
new_df=new_df.append([d1['Picture 2'],d1['Picture 3'],d1['Picture 4'],d1['Picture 5'],d1['Picture 6'],d1['Picture 7'],d1['Picture 8']],ignore_index=True)
new_df


# In[ ]:


new_df=pd.DataFrame(new_df)
new_df.replace(np.nan,0,inplace=True)
a_series = (new_df != 0).any(axis=1)
new_df1 = new_df.loc[a_series]
new_df1


# In[ ]:


new_df1=pd.DataFrame(new_df1)
new_df1


# In[ ]:


folder=os.listdir(DIR)
folder

onlyfolders = [f for f in listdir(DIR) if os.path.isdir(join(DIR, f))]
onlyfolders[0]


# In[ ]:


ab=new_df1[0].to_list()
ab
n=len(ab)


# In[ ]:


path = input('Give a path of directory who have same name as file:')
for i in range(0,n):
    img1 = ab[i]
    img=wget.download(img1,path)
    print(img)


# In[ ]:


new_dir=path
print(len([name for name in os.listdir(new_dir) if os.path.isfile(os.path.join(new_dir, name))]))


# ### Working with .csv files

# In[ ]:


csv_files


# In[ ]:


path = input('Path: + /filename.xlsx')
d2=pd.read_csv(path)
d2=d2.drop(['Docket No','Damage Description','Engineer Name'],axis=1)


# In[ ]:


new_df_csv = d2['Picture 1']
new_df_csv=new_df_csv.append([d2['Picture 2'],d2['Picture 3'],d2['Picture 4'],d2['Picture 5'],d2['Picture 6'],d2['Picture 7'],d2['Picture 8']],ignore_index=True)
new_df_csv


# In[ ]:


new_df_csv=pd.DataFrame(new_df_csv)
new_df_csv.replace(np.nan,0,inplace=True)
a_series = (new_df_csv != 0).any(axis=1)
new_df_csv1 = new_df_csv.loc[a_series]
new_df_csv1


# In[ ]:


new_df_csv1=pd.DataFrame(new_df_csv1)
new_df_csv1


# In[ ]:


folder=os.listdir(DIR)
folder

onlyfolders = [f for f in listdir(DIR) if os.path.isdir(join(DIR, f))]
onlyfolders


# In[ ]:


ab=new_df_csv1[0].to_list()
ab
n=len(ab)
n


# In[ ]:


path = input('Give a path of directory who have same name as file:')
for i in range(0,n):
    img1 = ab[i]
    img=wget.download(img1,path)
    print(img)    


# In[ ]:


print(len([name for name in os.listdir(new_dir) if os.path.isfile(os.path.join(new_dir, name))]))

