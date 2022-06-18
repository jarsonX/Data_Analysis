#Create random example dataset to compare it with the previous set.

import pandas as pd
import random as rd

i = 2500  #number of records

#-Base-dataset-----------------------------------------------------------------
#Create a dataset similar to the one created in part A.

input_file = r'C:\...\EURUSD_H4.csv'

data = pd.read_csv(input_file).head(i)
data.drop(['SMA14', 'SMA14IND','SMA50IND', 'Decision'], inplace=True, axis=1)
data = data.interpolate()  

#-Fix-datatypes----------------------------------------------------------------
if input_file == r'C:\...\GBPUSD_H4.csv':
    
    to_fix = ['SMA50']
    
    for col in to_fix:
        for el in data[col]:
            if (type(el) != int) and (type(el) != float) and (el[0:3] == 'nan'):
                index = data[data[col] == el].index.item()
                data.at[index, col] = 0

    data['SMA50'] = data['SMA50'].astype(float)
#------------------------------------------------------------------------------

#Normalization
normalize = ['Bulls', 'CCI']

for att in normalize:
    max_val = data[att].max()
    min_val = data[att].min()
    data[att] = (data[att] - min_val) / (max_val - min_val)
    
    
#-Dataset-for-comparison-------------------------------------------------------

#Column headings as keys
cols = {'Close': [], 'SMA50': [], 'Bulls': [], 'CCI': [], \
            'DM': [], 'OSMA': [], 'RSI': [], 'Stoch': []}

#Create lists for dataframe columns 
for key, value in cols.items():
    
    minimum_fixed = data[key].min()
    maximum_fixed = data[key].max() 
    
    minimum = data[key].min()
    maximum = data[key].max()
    
    first_val = rd.uniform(minimum, maximum)  #First row
    
    cols[key].append(first_val)
        
#i of random rows
    for x in range(i):
        minimum = minimum - minimum*0.01
        maximum = maximum + maximum*0.01
        
        next_value = rd.uniform(minimum, maximum)
        
        if next_value < minimum_fixed:
            next_value = minimum_fixed
        
        if next_value > maximum_fixed:
            next_value = maximum_fixed
        
        cols[key].append(next_value)

#The second dataset
data_2 = pd.DataFrame(cols)

#Normalization
for att in normalize:
    max_val = data_2[att].max()
    min_val = data_2[att].min()
    data_2[att] = (data_2[att] - min_val) / (max_val - min_val)

#Samples
print('\n----First-dataset----')
print(data.head(5))

print('\n----Second-dataset----')
print(data_2.head(5))
        
#Korelacje    
atts = ['Close', 'SMA50', 'Bulls', 'CCI', 'DM', 'OSMA', 'RSI', 'Stoch']

print('\n----Correlations----')
for att in atts:
    corr = data[att].corr(data_2[att])
    print("%8.4f" % (corr), '\t', att)
