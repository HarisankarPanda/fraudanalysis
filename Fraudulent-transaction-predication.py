#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


df= pd.read_csv('C:\\Users\\Harisankar Panda\\Downloads\\Fraud.csv')


# In[4]:


df.head()


# In[8]:


df.dropna()

df.drop_duplicates(inplace =True)

print(df.info())
print(df.describe())
print(df.isnull().sum())
df.boxplot()
df.to_csv("filtered_csv" ,index=True)


# In[10]:


print(df.columns.tolist())


# In[ ]:




