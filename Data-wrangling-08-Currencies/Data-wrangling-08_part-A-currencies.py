#Perform pre-processing of 3 files with basic checks: EURUSD, NZDUSD, GBPUSD.

import pandas as pd

#-1-Load-----------------------------------------------------------------------
input_file = r'C:\...\GBPUSD_H4.csv'
data = pd.read_csv(input_file).head(2500)  #specify how many records we want

#-2-Clean----------------------------------------------------------------------
#Delete columns SMA14IND and SMA50IND as we don't need them
data.drop(['SMA14IND','SMA50IND'], inplace=True, axis=1)

#-Fix-datatypes----------------------------------------------------------------
#This is required only for GBPUSD because datatypes in columns SMA14 and SMA50
#are broken due to values like 'nan5', 'nan6' etc.

if input_file == r'C:\...\GBPUSD_H4.csv':
    
    to_fix = ('SMA14', 'SMA50')
    
    for col in to_fix:
        for el in data[col]:
            if (type(el) != int) and (type(el) != float) and (el[0:3] == 'nan'):
                index = data[data[col] == el].index.item()
                data.at[index, col] = 0

    data['SMA14'] = data['SMA14'].astype(float)
    data['SMA50'] = data['SMA50'].astype(float)

#------------------------------------------------------------------------------
#Interpolate nulls in Close, SMA14 and SMA50
data['Close'].interpolate(inplace=True)
data['SMA14'].interpolate(inplace=True)
data['SMA50'].interpolate(inplace=True)

#Change remaining nulls to 0s
for atrybut in ['Bulls', 'CCI', 'DM', 'OSMA', 'RSI', 'Stoch', 'Decision']:
    if data[atrybut].isnull().sum() > 0:
        data[atrybut].fillna(0, inplace=True)

#-3-Efficiency-----------------------------------------------------------------
#Check correlations for Close-SMA14, Close-SMA50. Delete the column with higher
#correlation.

#Note: redeucing the amount of data might be important if we're passing the 
#files to an algorithm. 

corr_Close_SMA14 = round(data['Close'].corr(data['SMA14']),2)
print('Close-SMA14 correlation:', corr_Close_SMA14)

corr_Close_SMA50 = round(data['Close'].corr(data['SMA50']),2)
print('Close-SMA50 correlation:', corr_Close_SMA50)

if corr_Close_SMA14 == corr_Close_SMA50:
    print('Correlations are equal. No column removed. Check the correctness of data.')
elif corr_Close_SMA14 > corr_Close_SMA50:
    to_drop = 'SMA14'
else:
    to_drop = 'SMA50'
    
data.drop([to_drop], inplace=True, axis=1)
print('Column removed:', to_drop)

#-4-Additional-checks----------------------------------------------------------

#Count of negatives for CCI
negatives_count = data['CCI'].lt(0).sum()
print('CCI negatives:', negatives_count) 

#Min-max for all attributes
attributes = list(data.head(0))
       
list_att = []
list_max = []
list_min = []        

for att in attributes:
    if att != 'Decision':  #we're skipping Decision here
        list_att.append(att)
        list_max.append(data[att].max())
        list_min.append(data[att].min())
        
df_max_min = pd.DataFrame()
df_max_min[''] = list_att
df_max_min['max'] = list_max
df_max_min['min'] = list_min    

print('\nMin and max values')
print(df_max_min.set_index(''))

#-5-normalization-min-max------------------------------------------------------
normalize = ['Bulls', 'CCI']

for att in normalize:
    max_val = data[att].max()
    min_val = data[att].min()
    data[att] = (data[att] - min_val) / (max_val - min_val)
    
#-6-discretization-------------------------------------------------------------
data['Bulls'] = pd.cut(data['Bulls'], 2, labels = ['Up','Down'])   
data['CCI'] = pd.cut(data['CCI'], 4, labels = ['A','B', 'C', 'D'])  

#-7-plotting-------------------------------------------------------------------

#Pie
buy = data['Decision'].value_counts().BUY
sell = data['Decision'].value_counts().SELL
strong_buy = data['Decision'].value_counts().STRONGBUY
strong_sell = data['Decision'].value_counts().STRONGSELL
wait = data['Decision'].value_counts().WAIT

df_decision = pd.DataFrame({'decision': [strong_sell, strong_buy, buy, wait, sell]}, \
                                        index = ['strong sell', 'strong buy', 'buy', 'wait', 'sell'])

colors = ['#f7ff00','#32ff00','#b3ffa0', '#c1c1c1', '#fdffb0']   
plot = df_decision.plot.pie(y='decision', figsize=(8, 8), colors = colors, autopct='%1.1f%%', \
                            legend=False, title = 'Decision')

#Line
data['Close'].plot(title='Close')    
    
#-8-Save-----------------------------------------------------------------------
data.to_json(r'C:\...\result')
