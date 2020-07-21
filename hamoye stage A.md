```python
#import necessary information
import pandas as pd
import numpy as np

```


```python
np.array[(1,0,0),(0,1,0),(0,1,1)]#checking for an answer
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-ab0a1e4351bb> in <module>
    ----> 1 np.array[(1,0,0),(0,1,0),(0,1,1)]
    

    TypeError: 'builtin_function_or_method' object is not subscriptable



```python
import csv
```


```python
#import the dataset
#link was copied from the internet and read as csv
df=pd.read_csv("https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv")
print(df)
df.head
df.columns
```

                         record_id  utility_id_ferc1  report_year  \
    0        f1_fuel_1994_12_1_0_7                 1         1994   
    1       f1_fuel_1994_12_1_0_10                 1         1994   
    2        f1_fuel_1994_12_2_0_1                 2         1994   
    3        f1_fuel_1994_12_2_0_7                 2         1994   
    4       f1_fuel_1994_12_2_0_10                 2         1994   
    ...                        ...               ...          ...   
    29518  f1_fuel_2018_12_12_0_13                12         2018   
    29519   f1_fuel_2018_12_12_1_1                12         2018   
    29520  f1_fuel_2018_12_12_1_10                12         2018   
    29521  f1_fuel_2018_12_12_1_13                12         2018   
    29522  f1_fuel_2018_12_12_1_14                12         2018   
    
               plant_name_ferc1 fuel_type_code_pudl fuel_unit  fuel_qty_burned  \
    0                  rockport                coal       ton        5377489.0   
    1      rockport total plant                coal       ton       10486945.0   
    2                    gorgas                coal       ton        2978683.0   
    3                     barry                coal       ton        3739484.0   
    4                 chickasaw                 gas       mcf          40533.0   
    ...                     ...                 ...       ...              ...   
    29518    neil simpson ct #1                 gas       mcf          18799.0   
    29519  cheyenne prairie 58%                 gas       mcf         806730.0   
    29520     lange ct facility                 gas       mcf         104554.0   
    29521       wygen 3 bhp 52%                coal       ton         315945.0   
    29522       wygen 3 bhp 52%                 gas       mcf          17853.0   
    
           fuel_mmbtu_per_unit  fuel_cost_per_unit_burned  \
    0                   16.590                      18.59   
    1                   16.592                      18.58   
    2                   24.130                      39.72   
    3                   23.950                      47.21   
    4                    1.000                       2.77   
    ...                    ...                        ...   
    29518                1.059                       4.78   
    29519                1.050                       3.65   
    29520                1.060                       4.77   
    29521               16.108                       3.06   
    29522                1.059                       0.00   
    
           fuel_cost_per_unit_delivered  fuel_cost_per_mmbtu  
    0                             18.53                1.121  
    1                             18.53                1.120  
    2                             38.12                1.650  
    3                             45.99                1.970  
    4                              2.77                2.570  
    ...                             ...                  ...  
    29518                          4.78                9.030  
    29519                          3.65                6.950  
    29520                          4.77                8.990  
    29521                         14.76                1.110  
    29522                          0.00               11.680  
    
    [29523 rows x 11 columns]
    




    Index(['record_id', 'utility_id_ferc1', 'report_year', 'plant_name_ferc1',
           'fuel_type_code_pudl', 'fuel_unit', 'fuel_qty_burned',
           'fuel_mmbtu_per_unit', 'fuel_cost_per_unit_burned',
           'fuel_cost_per_unit_delivered', 'fuel_cost_per_mmbtu'],
          dtype='object')




```python
#question 1
A=[1,2,3,4,5,6]
B=[13,21,34]
A.extend(B)
A
```




    [1, 2, 3, 4, 5, 6, 13, 21, 34]




```python
#############question 2#######################
A.append(B)
A
#output is wrong 
```




    [1, 2, 3, 4, 5, 6, 13, 21, 34, [13, 21, 34]]




```python
np.identity(3)

```




    array([[1., 0., 0.],
           [0., 1., 0.],
           [0., 0., 1.]])




```python
#eye function was not identified while the np. array functions returned error of ot subscriptable
```


```python
#################question 3##############################
#calculate average fuel cost per unit
#the output of the csv file imported earlier doesnt show the columns in a single column
#to correct this we do this:
pd.options.display.max_columns=None
#recall the head of the dataframe
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>record_id</th>
      <th>utility_id_ferc1</th>
      <th>report_year</th>
      <th>plant_name_ferc1</th>
      <th>fuel_type_code_pudl</th>
      <th>fuel_unit</th>
      <th>fuel_qty_burned</th>
      <th>fuel_mmbtu_per_unit</th>
      <th>fuel_cost_per_unit_burned</th>
      <th>fuel_cost_per_unit_delivered</th>
      <th>fuel_cost_per_mmbtu</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>f1_fuel_1994_12_1_0_7</td>
      <td>1</td>
      <td>1994</td>
      <td>rockport</td>
      <td>coal</td>
      <td>ton</td>
      <td>5377489.0</td>
      <td>16.590</td>
      <td>18.59</td>
      <td>18.53</td>
      <td>1.121</td>
    </tr>
    <tr>
      <th>1</th>
      <td>f1_fuel_1994_12_1_0_10</td>
      <td>1</td>
      <td>1994</td>
      <td>rockport total plant</td>
      <td>coal</td>
      <td>ton</td>
      <td>10486945.0</td>
      <td>16.592</td>
      <td>18.58</td>
      <td>18.53</td>
      <td>1.120</td>
    </tr>
    <tr>
      <th>2</th>
      <td>f1_fuel_1994_12_2_0_1</td>
      <td>2</td>
      <td>1994</td>
      <td>gorgas</td>
      <td>coal</td>
      <td>ton</td>
      <td>2978683.0</td>
      <td>24.130</td>
      <td>39.72</td>
      <td>38.12</td>
      <td>1.650</td>
    </tr>
    <tr>
      <th>3</th>
      <td>f1_fuel_1994_12_2_0_7</td>
      <td>2</td>
      <td>1994</td>
      <td>barry</td>
      <td>coal</td>
      <td>ton</td>
      <td>3739484.0</td>
      <td>23.950</td>
      <td>47.21</td>
      <td>45.99</td>
      <td>1.970</td>
    </tr>
    <tr>
      <th>4</th>
      <td>f1_fuel_1994_12_2_0_10</td>
      <td>2</td>
      <td>1994</td>
      <td>chickasaw</td>
      <td>gas</td>
      <td>mcf</td>
      <td>40533.0</td>
      <td>1.000</td>
      <td>2.77</td>
      <td>2.77</td>
      <td>2.570</td>
    </tr>
  </tbody>
</table>
</div>




```python
##calculate average cost per unit
df.groupby(by='fuel_type_code_pudl').mean()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>utility_id_ferc1</th>
      <th>report_year</th>
      <th>fuel_qty_burned</th>
      <th>fuel_mmbtu_per_unit</th>
      <th>fuel_cost_per_unit_burned</th>
      <th>fuel_cost_per_unit_delivered</th>
      <th>fuel_cost_per_mmbtu</th>
    </tr>
    <tr>
      <th>fuel_type_code_pudl</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>coal</th>
      <td>115.637534</td>
      <td>2004.623143</td>
      <td>1.903473e+06</td>
      <td>20.762780</td>
      <td>67.421830</td>
      <td>116.951141</td>
      <td>1.787190</td>
    </tr>
    <tr>
      <th>gas</th>
      <td>124.122062</td>
      <td>2005.978060</td>
      <td>4.843183e+06</td>
      <td>1.021913</td>
      <td>13.659397</td>
      <td>12.095172</td>
      <td>5.408876</td>
    </tr>
    <tr>
      <th>nuclear</th>
      <td>107.397311</td>
      <td>2002.970660</td>
      <td>5.454838e+06</td>
      <td>17.582120</td>
      <td>4955.157002</td>
      <td>28616.915039</td>
      <td>1.716559</td>
    </tr>
    <tr>
      <th>oil</th>
      <td>113.236235</td>
      <td>2007.195933</td>
      <td>6.311677e+04</td>
      <td>5.814377</td>
      <td>168.877086</td>
      <td>313.907691</td>
      <td>12.698732</td>
    </tr>
    <tr>
      <th>other</th>
      <td>110.467066</td>
      <td>2001.700599</td>
      <td>2.948137e+06</td>
      <td>0.572752</td>
      <td>18.253856</td>
      <td>16.871485</td>
      <td>155.084910</td>
    </tr>
    <tr>
      <th>waste</th>
      <td>154.253968</td>
      <td>2005.650794</td>
      <td>1.171914e+05</td>
      <td>0.341163</td>
      <td>19.518122</td>
      <td>18.413052</td>
      <td>822.709937</td>
    </tr>
  </tbody>
</table>
</div>




```python
##the gas fuel type shows the least average cost per unit with an amount of 13.659397
```


```python
###########question four##############
#######what is the standard deviation and 75thpercentile of energy per unit in two decimal place
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>utility_id_ferc1</th>
      <th>report_year</th>
      <th>fuel_qty_burned</th>
      <th>fuel_mmbtu_per_unit</th>
      <th>fuel_cost_per_unit_burned</th>
      <th>fuel_cost_per_unit_delivered</th>
      <th>fuel_cost_per_mmbtu</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>29523.000000</td>
      <td>29523.000000</td>
      <td>2.952300e+04</td>
      <td>29523.000000</td>
      <td>29523.000000</td>
      <td>2.952300e+04</td>
      <td>29523.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>118.601836</td>
      <td>2005.806050</td>
      <td>2.622119e+06</td>
      <td>8.492111</td>
      <td>208.649031</td>
      <td>9.175704e+02</td>
      <td>19.304354</td>
    </tr>
    <tr>
      <th>std</th>
      <td>74.178353</td>
      <td>7.025483</td>
      <td>9.118004e+06</td>
      <td>10.600220</td>
      <td>2854.490090</td>
      <td>6.877593e+04</td>
      <td>2091.540939</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>1994.000000</td>
      <td>1.000000e+00</td>
      <td>0.000001</td>
      <td>-276.080000</td>
      <td>-8.749370e+02</td>
      <td>-41.501000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>55.000000</td>
      <td>2000.000000</td>
      <td>1.381700e+04</td>
      <td>1.024000</td>
      <td>5.207000</td>
      <td>3.778500e+00</td>
      <td>1.940000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>122.000000</td>
      <td>2006.000000</td>
      <td>2.533220e+05</td>
      <td>5.762694</td>
      <td>26.000000</td>
      <td>1.737100e+01</td>
      <td>4.127000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>176.000000</td>
      <td>2012.000000</td>
      <td>1.424034e+06</td>
      <td>17.006000</td>
      <td>47.113000</td>
      <td>4.213700e+01</td>
      <td>7.745000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>514.000000</td>
      <td>2018.000000</td>
      <td>5.558942e+08</td>
      <td>341.260000</td>
      <td>139358.000000</td>
      <td>7.964521e+06</td>
      <td>359278.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#########the row std shows the standard deviation of all the columns
####the  75% row shows the percentile of all the colummns
#round the values to 2 decimal places
#std and 75% for fuel_mmbtu_per_unit is 10.600220  and 17.06000 respectively
#rounded up as 10.60 and 17.06 respectively
```


```python
#####question five########
###what is the skewness and kurtosis for the fuel quantity burned
from scipy.stats import skew
df.skew() ####skewness
df.kurtosis()  ###kurtosis
```




    utility_id_ferc1                    1.088432
    report_year                        -1.145656
    fuel_qty_burned                   651.369450
    fuel_mmbtu_per_unit                55.595695
    fuel_cost_per_unit_burned         485.255851
    fuel_cost_per_unit_delivered    11765.054226
    fuel_cost_per_mmbtu             29489.132594
    dtype: float64




```python
#############question six####################
#which feature has missing value and what is the total number of missing values
df.isna().sum()
```




    record_id                         0
    utility_id_ferc1                  0
    report_year                       0
    plant_name_ferc1                  0
    fuel_type_code_pudl               0
    fuel_unit                       180
    fuel_qty_burned                   0
    fuel_mmbtu_per_unit               0
    fuel_cost_per_unit_burned         0
    fuel_cost_per_unit_delivered      0
    fuel_cost_per_mmbtu               0
    dtype: int64




```python
### the fuel unit has an output of 180 missing values
```


```python
#####percentage of the missing row as a factor of the total number of rows in three decimal places
#here, we divide the percentage by the length of the dataframe
#first calculate the  miss
per=df.isna().sum()/len(df)
print(per*100)
```

    record_id                       0.000000
    utility_id_ferc1                0.000000
    report_year                     0.000000
    plant_name_ferc1                0.000000
    fuel_type_code_pudl             0.000000
    fuel_unit                       0.609694
    fuel_qty_burned                 0.000000
    fuel_mmbtu_per_unit             0.000000
    fuel_cost_per_unit_burned       0.000000
    fuel_cost_per_unit_delivered    0.000000
    fuel_cost_per_mmbtu             0.000000
    dtype: float64
    


```python
#output shows 0.609694 approximately 0.610 percent


```


```python
#####question seven##########
#the feature with missing value falls under which category
#to check for category of a data we use the .dtype function as this gives analysis of the datatypes for all the columns
df.dtypes
```




    record_id                        object
    utility_id_ferc1                  int64
    report_year                       int64
    plant_name_ferc1                 object
    fuel_type_code_pudl              object
    fuel_unit                        object
    fuel_qty_burned                 float64
    fuel_mmbtu_per_unit             float64
    fuel_cost_per_unit_burned       float64
    fuel_cost_per_unit_delivered    float64
    fuel_cost_per_mmbtu             float64
    dtype: object




```python
#the ouptut shows that the fuel unit which as the missing values in this dataset as shown previous shows a result of object datatype
#the columns with the object datatype shows the possible categorical features of the dataset.
#since output shows categorical datatype,
#the imputation method used for categorical datatype of missing values is usually imputing categorical features by the most commmon class(modal class)
#or just replacing them with unknown or missing values
#so the best option is categorical or modal imputation
```


```python
########question 8##########
#which feature has the second and third lowest correlation with the fuel cost per unit burned
#here correlation function is used
df.corr().abs()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>utility_id_ferc1</th>
      <th>report_year</th>
      <th>fuel_qty_burned</th>
      <th>fuel_mmbtu_per_unit</th>
      <th>fuel_cost_per_unit_burned</th>
      <th>fuel_cost_per_unit_delivered</th>
      <th>fuel_cost_per_mmbtu</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>utility_id_ferc1</th>
      <td>1.000000</td>
      <td>0.093323</td>
      <td>0.057447</td>
      <td>0.066946</td>
      <td>0.037863</td>
      <td>0.016414</td>
      <td>0.006122</td>
    </tr>
    <tr>
      <th>report_year</th>
      <td>0.093323</td>
      <td>1.000000</td>
      <td>0.012952</td>
      <td>0.110853</td>
      <td>0.013599</td>
      <td>0.014043</td>
      <td>0.010261</td>
    </tr>
    <tr>
      <th>fuel_qty_burned</th>
      <td>0.057447</td>
      <td>0.012952</td>
      <td>1.000000</td>
      <td>0.080946</td>
      <td>0.018535</td>
      <td>0.003551</td>
      <td>0.001896</td>
    </tr>
    <tr>
      <th>fuel_mmbtu_per_unit</th>
      <td>0.066946</td>
      <td>0.110853</td>
      <td>0.080946</td>
      <td>1.000000</td>
      <td>0.010034</td>
      <td>0.009039</td>
      <td>0.005884</td>
    </tr>
    <tr>
      <th>fuel_cost_per_unit_burned</th>
      <td>0.037863</td>
      <td>0.013599</td>
      <td>0.018535</td>
      <td>0.010034</td>
      <td>1.000000</td>
      <td>0.011007</td>
      <td>0.000437</td>
    </tr>
    <tr>
      <th>fuel_cost_per_unit_delivered</th>
      <td>0.016414</td>
      <td>0.014043</td>
      <td>0.003551</td>
      <td>0.009039</td>
      <td>0.011007</td>
      <td>1.000000</td>
      <td>0.000109</td>
    </tr>
    <tr>
      <th>fuel_cost_per_mmbtu</th>
      <td>0.006122</td>
      <td>0.010261</td>
      <td>0.001896</td>
      <td>0.005884</td>
      <td>0.000437</td>
      <td>0.000109</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
####from the table above, it is evident that the third and fourth rows shows the output as python counts first row as zer
#so answer is fuel_qty_burned and fuel_mmbtu_per_unit
```


```python
#############question nine#############
#what is the percentage change in fuel cost per unit burned in 1998 compared to 1994
#we group the data together and find the total number of fuel type occuring after grouping all by itstotal occurence
df.groupby(["fuel_type_code_pudl", "report_year"]).sum()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>utility_id_ferc1</th>
      <th>fuel_qty_burned</th>
      <th>fuel_mmbtu_per_unit</th>
      <th>fuel_cost_per_unit_burned</th>
      <th>fuel_cost_per_unit_delivered</th>
      <th>fuel_cost_per_mmbtu</th>
    </tr>
    <tr>
      <th>fuel_type_code_pudl</th>
      <th>report_year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">coal</th>
      <th>1994</th>
      <td>50430</td>
      <td>7.172082e+08</td>
      <td>10293.429297</td>
      <td>14984.572</td>
      <td>59215.371</td>
      <td>682.14697</td>
    </tr>
    <tr>
      <th>1995</th>
      <td>51231</td>
      <td>1.257398e+09</td>
      <td>10262.019015</td>
      <td>14571.785</td>
      <td>13704.146</td>
      <td>663.74149</td>
    </tr>
    <tr>
      <th>1996</th>
      <td>45720</td>
      <td>6.988514e+08</td>
      <td>9269.878000</td>
      <td>12694.803</td>
      <td>12087.581</td>
      <td>581.57661</td>
    </tr>
    <tr>
      <th>1997</th>
      <td>44254</td>
      <td>8.169024e+08</td>
      <td>9000.095755</td>
      <td>43742.178</td>
      <td>11308.641</td>
      <td>551.68662</td>
    </tr>
    <tr>
      <th>1998</th>
      <td>46403</td>
      <td>8.982095e+08</td>
      <td>9212.781694</td>
      <td>11902.597</td>
      <td>308602.749</td>
      <td>557.06574</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">waste</th>
      <th>2014</th>
      <td>2840</td>
      <td>3.607257e+06</td>
      <td>8.715213</td>
      <td>591.594</td>
      <td>545.293</td>
      <td>343.82900</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>2837</td>
      <td>3.737472e+06</td>
      <td>8.738479</td>
      <td>629.270</td>
      <td>591.380</td>
      <td>391.21400</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>2547</td>
      <td>3.782403e+06</td>
      <td>8.828807</td>
      <td>539.079</td>
      <td>504.245</td>
      <td>429.59900</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>2183</td>
      <td>3.534230e+06</td>
      <td>8.686320</td>
      <td>452.079</td>
      <td>417.818</td>
      <td>359311.75300</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>2277</td>
      <td>3.296373e+06</td>
      <td>8.693921</td>
      <td>660.972</td>
      <td>514.749</td>
      <td>315.19300</td>
    </tr>
  </tbody>
</table>
<p>148 rows × 6 columns</p>
</div>




```python
#to calculate this, we say sum of coal gotten foryear 1998 -1994 / that of 1994 *100
dif=11902.597-14984.572
(dif/14984.572)*100
```




    -20.567654518260518




```python
#approximately a -21%
```


```python
##################question ten####################
#which year has the average fuel cost per unit delivered
year=df['report_year'][(df['fuel_cost_per_unit_delivered']==df['fuel_cost_per_unit_delivered'].max())]
print(year)
```

    3564    1997
    Name: report_year, dtype: int64
    


```python
#therefore year 1997 has the average fuel cost per unit
```
