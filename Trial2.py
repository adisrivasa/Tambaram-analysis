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


# In[26]:


i=0
df=[]
print(type(df))
fig, ax =  plt.subplots(1,1, figsize=(100, 100))
for item in cats:
    is_PEP =  data['Layer']==item
    df.append(data[is_PEP])
#     psm = ax[i//2].scatter(df[i]['X_Cordinat'], df[i]['Y_Cordinat'], alpha=0.5)
#     ax[i//2].title.set_text(item)
    i = i+1
# plt.show()
df


# In[33]:


lst = [1,2,6,7,8]

# for item in lst:
plt.scatter(df[1]['X_Cordinat'], df[1]['Y_Cordinat'], alpha=0.5)
plt.show()
plt.scatter(df[2]['X_Cordinat'], df[2]['Y_Cordinat'], alpha=0.5)
plt.show()
plt.scatter(df[6]['X_Cordinat'], df[6]['Y_Cordinat'], alpha=0.5)
plt.show()
plt.scatter(df[7]['X_Cordinat'], df[7]['Y_Cordinat'], alpha=0.5)
plt.show()
plt.scatter(df[8]['X_Cordinat'], df[8]['Y_Cordinat'], alpha=0.5)
plt.show()
# plt.scatter(df['X_Cordinat'], df['Y_Cordinat'], alpha=0.5)
# plt.scatter(df['X_Cordinat'], df['Y_Cordinat'], alpha=0.5)
# plt.scatter(df['X_Cordinat'], df['Y_Cordinat'], alpha=0.5)


# In[14]:


# fig, ax =  plt.subplots(7,2, figsize=(20, 10), constrained_layout=True)
# for i in range(14):
#     psm = ax[i//2][i%2].scatter()

