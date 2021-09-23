#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import pandas as pd
data=pd.read_excel('C:/Users/SurajC/Downloads/Desktop/amazon/20-09-2021.xlsx', sheet_name='Sheet2')

df1=pd.DataFrame(data)
df1.head(5)


# In[2]:


a=[]
str=df1['product_name']
for i in str:
    
    if re.findall(r' (\d{3}/)', i):
        x=re.findall(r' (\d{3}/)', i)
        if x[0] in i:
            start_index = i.index(x[0])
            s= i[start_index:start_index+10]
            a.append(s)
            
    else :
        a.append('--')
    

df1 = pd.DataFrame(a)
df1['new'] = pd.DataFrame(a)
print(df1)


# In[3]:


df1['new'] = df1['new'].str.replace(',', '')
df1['new'] = df1['new'].str.replace('215/75/15/', '215/75/15')
df1['new'] = df1['new'].str.replace('165/70/14/', '165/70/14')
df1['new'] = df1['new'].str.replace('235/70/16/', '235/70/16')
df1['new'] = df1['new'].str.replace('215/75/15/', '215/75/15')
df1['new'] = df1['new'].str.replace('165/70/14/', '165/70/14')
df1['new'] = df1['new'].str.replace('235/70/16/', '235/70/16')
df1['new'] = df1['new'].str.replace('215/75/15/', '215/75/15')
df1['new'] = df1['new'].str.replace('235/70/16/', '235/70/16')
df1['new'] = df1['new'].str.replace('215/65/16/', '215/65/16')

df1['new'] = df1['new'].str.replace('235/70/16/', '235/70/16')
df1['new'] = df1['new'].str.replace('195/55/16/', '195/55/16')
df1['new'] = df1['new'].str.replace('175/65/15/', '175/65/15')
df1['new'] = df1['new'].str.replace('110/70/17/', '110/70/17')
df1['new'] = df1['new'].str.replace('185/80D14', '185/80/14')
df1['new'] = df1['new'].str.replace('215/60/17/', '215/60/17')
df1['new'] = df1['new'].str.replace('145/70/80/', '145/70/80')
df1['new'] = df1['new'].str.replace('215/60/16/', '215/60/16')
df1['new'] = df1['new'].str.replace('215/65/16/', '215/65/16')
df1['new'] = df1['new'].str.replace('215/75/15/', '215/75/15')
df1['new'] = df1['new'].str.replace('102/1008', '102/10/08')
df1['new'] = df1['new'].str.replace('165/80D13', '165/80/13')
df1['new'] = df1['new'].str.replace('155/80/D', '155/80')
df1['new'] = df1['new'].str.replace('235/6517/', '235/65/17')
df1['new'] = df1['new'].str.replace('205/65 R16', '205/65/16')
df1['new'] = df1['new'].str.replace('215/60R17-', '215/60/17')
df1['new'] = df1['new'].str.replace('165/70R14 ', '165/70/14')
df1['new'] = df1['new'].str.replace('205/65R16', '205/65/16')
df1['new'] = df1['new'].str.replace('155/70R13', '155/70/13')
df1['new'] = df1['new'].str.replace('ST', '')
df1['new'] = df1['new'].str.replace('165/70/14/', '165/70/14')
df1['new'] = df1['new'].str.replace('235/65/', '235/65')
df1['new'] = df1['new'].str.replace('LT', '')
df1['new'] = df1['new'].str.replace('265/60/18/', '265/60/18')
df1['new'] = df1['new'].str.replace('235/75/15/', '235/75/15')
df1['new'] = df1['new'].str.replace('(', '')
df1['new'] = df1['new'].str.replace('145/70/12/', '145/70/12')
df1['new'] = df1['new'].str.replace('145/55/70/', '145/55/70')
df1['new'] = df1['new'].str.replace('205/60/16/', '205/60/16')
df1['new'] = df1['new'].str.replace('205/60/16/', '205/60/16')
df1['new'] = df1['new'].str.replace('145/70/12/', '145/70/12')
df1['new'] = df1['new'].str.replace(' ', '')
df1['new'] = df1['new'].str.replace('R', '/')
df1['new'] = df1['new'].str.replace('-', '/')
df1['new'] = df1['new'].str.replace('//', '/')
df1['new'] = df1['new'].str.replace('r', '/')
df1['new'] = df1['new'].str.replace('A', '')
df1['new'] = df1['new'].str.replace('z', '')
df1['new'] = df1['new'].str.replace('k', '')
df1['new'] = df1['new'].str.replace('K', '')
df1['new'] = df1['new'].str.replace('Z', '')
df1['new'] = df1['new'].str.replace('205/60/16/', '205/60/16')
df1['new'] = df1['new'].str.replace('215/75/15/', '215/75/15')
df1['new'].unique()
final = df1['new']
final
a = final.to_excel('C:/Users/SurajC/Downloads/Desktop/amazon/extracted.xlsx',index=False)


# In[4]:


df1['new'].unique()


# In[5]:


df1

