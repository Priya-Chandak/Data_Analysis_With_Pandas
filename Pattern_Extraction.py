#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

d = pd.read_excel("C:/Users/SurajC/Downloads/Desktop/amazon/amazon_pattern.xlsx",sheet_name="Sheet1")
data=pd.DataFrame(d)


# In[ ]:


data


# In[ ]:


n = len(data['pattern'])
data['pattern']=data['pattern'].replace(np.nan,0)
data


# In[ ]:


b=[]
last_string = 0

for i in range(0,n):
    
    if data['pattern'][i] != 0:
        last_string = data['pattern'][i]
    b.append(last_string)


# In[ ]:


data['b']=pd.DataFrame(b)


# In[ ]:


data.to_excel('C:/Users/SurajC/Downloads/Desktop/amazon/demo1.xlsx',index=False)


# In[ ]:


data['pattern'].unique()


# In[ ]:




