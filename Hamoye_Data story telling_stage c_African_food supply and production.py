
# coding: utf-8

# In[6]:


#import necessary ackages
import pandas as pd
import numpy as np
import csv
import os
import matplotlib as plt
import seaborn as sns


# In[7]:


#import the data
fs=pd.read_csv("C:\\Users\\HP Envy\\Downloads\\AFS.csv")
print(fs)
fp=pd.read_csv("C:\\Users\\HP Envy\\Downloads\\AFP.csv")
print(fp)


# In[3]:


fs.groupby(["Country","Year","Value"]).count()
print(fs)


# In[8]:


fp.groupby(["Country","Year","Item"]).sum().Value
print(fp)


# ######data exploration##############

# In[16]:


fig,ax=plt.subplot(figsize=(25,20))
line =fs.groupby(['Year','Country']).sum()['Value'].unstack().plot(ax=ax)
ax.set_xticks(fs.Year.unique())
ax.set_yticks(fs['Value'])
ax.set_yscale('log')
ax.set_ylim(1800,3500)
plt.ylabel('Value')
plt.xlabel('Year')
plt.title('Food Supply in Africa for the year 2004 - 2013')
plt.show()


# In[10]:


fig,ax=plt.subplots(figsize=(25,20))
line =fp.groupby(['Year','Item',]).sum()['Value'].unstack().plot(ax=ax)
ax.set_xticks(fp.Year.unique())
ax.set_yticks(fp['Value'])
ax.set_yscale('log')
ax.set_ylim(1800,4000)
plt.ylabel('Value')
plt.xlabel('Year')
plt.title('Food production in Africa')
plt.show()


# In[11]:


###########finding problem pattern#################
#looking for outliers
##use a boxplot
#i grouped my data generally by country to get good visuals  
#boxplot for food supply by country
groufs = fs.groupby(['Year','Country',]).sum()['Value'].unstack()
groufs.boxplot(rot=100, figsize=(25,20))
plt.title('Boxplot of food supply in Africa')
plt.show()


# In[12]:


#The boxes with a little circle illustrates outliers. the box with value ,kenya illustrates a possible outlier.
#according to the hamoye text on the problem of finding problem patterns
#he boxes represent data as grouped by their quartiles, while the whiskers show how the data varies outside the upper and lower quartiles
#in conclusion, we can deduce that the mean and medan are revresented by a line inside each of the boxes revresented in the diagram


# In[14]:


#for the  production dataset
groufp = fp.groupby(['Year','Item',]).sum()['Value'].unstack()
groufp.boxplot(rot=100, figsize=(30,20))
plt.title('Boxplot of food production in Africa')
plt.show()


# In[15]:


################some statistical measures and their applications##############
###calculate average food production by year
meanfp=fp.groupby(['Year']).mean()
print(meanfp)
#calculate the median food production by year
medianfp=fp.groupby(['Year']).median()
print(medianfp)

