# Preprocessing of data and basic analysis.

# Data includes EUR/USD rates.

# NOTE: some steps might not be that useful for this data set and are
# performed purely for illustration purposes.

# (1) Load data from csv file.
# (2) Clean data:
#   (2.1) Delete columns other than: Close, SMA14, Bulls, CCI, Decision.
#   (2.2) Deal with NaNs.
# (3) Perform analysis:
#   (3.1) Based on CCI check if there are any outliers.
#   (3.2) Perform normalization of Bulls and CCI.
#   (3.3) Check correlation of Close value and SMA14.
#   (3.4) Based on Bulls perform discretization (set intervals).
# (4) Create a line chart for Close value and CCI over time.
# (5) Save results:
#   (5.1) A txt file with summary of what have been performed.
#   (5.2) A csv file with processed data.

import pandas as pd
from datetime import date

# (1) LOAD DATA
input_file = r'C:\Users\krzys\Desktop\UE\4. Preprocessing danych rzeczywistych\Projekt\EURUSD_H4.csv'
data = pd.read_csv(input_file)

# (2) CLEANING
data.drop(['SMA50','SMA14IND','SMA50IND','DM','OSMA','RSI','Stoch'], \
          inplace=True, axis=1)

data = data.interpolate()

#To ensure no NaNs left in the file
# print("NaN values identified:")
# for i, el in enumerate(list(data.head(0))):
#     print(i, '\t', data[el].hasnans, '\t', el)

# (3) ANALYSIS

# Outliers
max_val_CCI = data['CCI'].max()
min_val_CCI = data['CCI'].min()

Q1 = data['CCI'].quantile(0.25)  #set quantiles
Q3 = data['CCI'].quantile(0.75)
IQR = Q3 - Q1

extremum = []  #check highest and lowest values in search for outliers

for el in data['CCI']:
    if (el < (Q1 - 2 * IQR)) or (el > (Q3 + 2 * IQR)):
        extremum.append(el)
        
extremum = sorted(extremum)
#print(extremum)

# Normalization

attributes = ['Bulls', 'CCI']

for att in attributes:
    max_val = data[att].max()
    min_val = data[att].min()
    # formula: x = (x - x.min) / (x.max - x.min)
    data[att] = (data[att] - min_val) / (max_val - min_val)

# Correlation
correlation = data['Close'].corr(data['SMA14'])

# Discretization
data['Bulls'] = pd.cut(data['Bulls'],2,labels = ['Up','Down'])

# (4) CHARTS
data['Close'].plot()
data['CCI'].plot()

# (5) SUMMARY

summary = open(r'C:\Users\krzys\Desktop\UE\4. Preprocessing danych rzeczywistych\Projekt\Summary.txt', 'w')
 
summary.write("File name: " + input_file[input_file.rfind('''\\''')+1:] + "\n")
summary.write("Created: " + str(date.today()) + "\n"*2)
summary.write("Summary")
summary.write("\n")
summary.write("No outliers needed to be excluded.\n")
summary.write("Normalization of Bulls and CCI performed.\n")
summary.write("Discretization of Bulls performed.\n")
summary.write('Correlation of Close value and SMA14 equals ' + str(round(float(correlation),4)) + ".") 
              
summary.close()

data.to_csv(r'C:\Users\krzys\Desktop\UE\4. Preprocessing danych rzeczywistych\Projekt\EURUSD_H4_out.cs')

print("Done!")