#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
import sys


# In[2]:


data = pd.read_csv('tambaram_Utility.csv')
print(data.info())

# In[3]:


print(data.X_Cordinat.max())
print(data.X_Cordinat.min())


# In[4]:


print(data.Y_Cordinat.max())
print(data.Y_Cordinat.min())


# In[5]:


cats=data.Layer.unique()
cats


# In[6]:


dic = {}
dic = data.Layer.value_counts()
dic.to_dict()
type(dic)


# In[7]:


plt.scatter(data['X_Cordinat'], data['Y_Cordinat'], alpha=0.5)


# In[8]:


plt.show()


# In[9]:


# sns.set(style="ticks", color_codes=True)


# In[10]:


# tips = sns.load_dataset(data)
# sns.catplot(x = data.X_Cordinat, y=data.Y_Cordinat, hue=data.Layer, data=data);


# In[11]:


is_PEP =  data['Layer']=='Bus stop'
df = data[is_PEP]
# df.reset_index()
df


# In[12]:


plt.scatter(df['X_Cordinat'], df['Y_Cordinat'], alpha=0.5)


# In[20]:


i=0
fig, ax =  plt.subplots(7,2, figsize=(40, 30))
for item in cats:
    is_PEP =  data['Layer']==item
    df = data[is_PEP]
    psm = ax[i//2][i%2].scatter(df['X_Cordinat'], df['Y_Cordinat'], alpha=0.5)
    ax[i//2][i%2].title.set_text(item)
    i = i+1
plt.show()


# In[14]:


# fig, ax =  plt.subplots(7,2, figsize=(20, 10), constrained_layout=True)
# for i in range(14):
#     psm = ax[i//2][i%2].scatter()
