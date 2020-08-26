
# coding: utf-8

# In[2]:


#import necessary ackages
import pandas as pd
import numpy as np
import csv
import os
import matplotlib as plt
import seaborn as sns


# In[4]:


#import the data
fs=pd.read_csv("C:\\Users\\HP Envy\\Downloads\\AFS.csv")
print(fs)
fp=pd.read_csv("C:\\Users\\HP Envy\\Downloads\\AFP.csv")
print(fp)


# In[6]:


fs.groupby(["Country","Year","Value"]).count()
print(fs)


# In[7]:


fp.groupby(["Country","Year","Item"]).sum().Value
print(fp)


# In[9]:


######data exploration##############
#what country produced highest quantity of rice


# In[13]:


group = fp.groupby(['Country','Item','Year'], as_index = False).sum()

#to check the highest producers of oats 
Oats = group[group.Item == 'Oats']
Oats.nlargest(12,'Value')


# In[20]:




