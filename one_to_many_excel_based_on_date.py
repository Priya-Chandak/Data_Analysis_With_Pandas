#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import datetime


# In[ ]:


data = pd.read_excel('C:/Users/SurajC/Downloads/Desktop/amazon/amazon_pattern.xlsx')


# In[ ]:


data.columns
data['date']=data['date'].dt.date
data


# In[ ]:


a1=[]
for i in range(0,len(data['date'])):
    a=data['date'][i]
    a2=a.strftime("%d-%m-%Y")
    a1.append(a2)


# In[ ]:


a2=pd.DataFrame(a1,columns=['date'])
a22=a2.sort_values(by='date')
a3=a22['date'].unique()
data['date']=a2


# In[ ]:


a3


# In[ ]:


for i in range(0,len(a3)):
    d = data[data['date'] == a3[i]]
    d.to_excel('C:/Users/SurajC/Downloads/Desktop/data/{}.xlsx'.format(a3[i]),index=False)    

