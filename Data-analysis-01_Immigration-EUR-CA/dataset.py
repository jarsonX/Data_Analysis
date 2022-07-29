import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.style.use(['ggplot'])
#also needed: openpyxl (install by pip)

#Load
dataset = pd.read_excel(r'C:\Users\krzys\Desktop\venv\Projekty\01-Immigration_CA\Canada.xlsx', sheet_name='Canada by Citizenship', skiprows=20, skipfooter=2)

#Modify
dataset.drop(['Type','Coverage','AREA','REG','DEV','DevName'], axis=1, inplace=True)
dataset.rename(columns={'OdName':'Country','AreaName':'Continent', 'RegName':'Region'}, inplace=True)

dataset.set_index('Country', inplace=True)
dataset.index.name = None

dataset['Total'] = dataset.sum(axis=1)
dataset.sort_values(by='Total', ascending=False, axis=0, inplace=True)  #sort by Total

dataset.columns = list(map(str, dataset.columns))

#Filter
years = list(map(str, range(1980, 2014)))  #for ease of plotting

condition = (dataset['Continent'] == 'Europe') & (dataset['Region'] == 'Eastern Europe')

datasetEE = dataset[condition]  #Eastern Europe only

print(datasetEE)
print('Done')