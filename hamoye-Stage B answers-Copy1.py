
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import csv
import os


# In[2]:


pwd


# In[3]:


#imort the data
df=pd.read_csv("C:\\Users\\HP Envy\\Downloads\\energydata_complete.csv")
df


# In[4]:


# listing the available columns in the data in order to remove relevant columns 
list(df.columns)


# In[5]:


# dropping passed columns 
df.drop(["date", "lights"], axis = 1, inplace = True)
df


# In[6]:


#normalize the dataset
#Firstly, we normalise our dataset to a common scale using the min max scaler
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
normalised_df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
normalised_df
#showing the target feature
target_feature = normalised_df['Appliances']
target_feature


# In[7]:


#split into train and test dataset
#Now, we split our dataset into the training and testing dataset. Recall that we
#had earlier segmented the features and target variables.
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(df, target_feature,
test_size=0.3, random_state=42)
#viewing all train and test values in x and y respectively
x_train=x_train
x_test=x_test
y_train=y_train
y_test=y_test


# In[20]:


#fit the model
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)
#evaluate the model
testredictmodel=model.predict(x_test)
testredictmodel


# In[9]:


################question twelve##############
#fit a linear model between two variables 
#temerature in the the building"T2" and outside"T6"
#create the t2 and t6 data from the dataframe 
inb = np.array(normalised_df['T2'])
outb= np.array(normalised_df['T6'])


# In[10]:


#train and test the data of t2 and t6
inb_train,inb_test,outb_train,outb_test=train_test_split(inb,outb,test_size=0.3,random_state=42)
lim=LinearRegression()
lim.fit(inb_train.reshape(-1,1),outb_train.reshape(-1,1))
limred=lim.predict(inb_test.reshape(-1,1))


# In[11]:


#calculate r squared
from sklearn.metrics import r2_score
rsquared=r2_score(outb_test,limred)
print(rsquared)


# In[12]:


############question thirteeen###################
#what is the mean absolute error of the whole dataset
#recall necessary information from the realdataset

from sklearn.metrics import mean_absolute_error
#recall y test and redict model
meanabserr= mean_absolute_error(y_test, testredictmodel)
meanabserr

