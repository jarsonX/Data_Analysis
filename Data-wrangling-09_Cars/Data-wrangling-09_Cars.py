#Scenario: prepare dataset for price prediction ML. Dataset contains data about cars.
#Dataset: https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data.

import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib import pyplot

#Load__________________________________________________________________________

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

filename = 'auto.csv'

df = pd.read_csv(filename, names = headers)


#Clean/repair missing values___________________________________________________

df.replace("?", np.nan, inplace = True)  # '?'s were easy to spot

missing_data = df.isnull()

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")    

#Replace by mean: normalized-losses, bore, stroke, horsepower, peak-rpm
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

avg_bore = df['bore'].astype('float').mean(axis=0)
df["bore"].replace(np.nan, avg_bore, inplace=True)

avg_stroke = df["stroke"].astype('float').mean(axis=0)
df["stroke"].replace(np.nan, avg_stroke, inplace=True)

avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

#Replace by frequency: num-of-doors
replacer = df['num-of-doors'].value_counts().idxmax()  #idxmax calculates the most common type
df["num-of-doors"].replace(np.nan, replacer, inplace=True)

#Drop: price, since price is our predictor missing values are useless
df.dropna(subset=["price"], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)


#Correct data format___________________________________________________________
#print(df.dtypes)  #initial check

df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["horsepower"]] = df[["horsepower"]].astype("int")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

#print(df.dtypes)  #confirmation check


#Change mpg to L/100km_________________________________________________________

df["highway-mpg"] = 235/df["highway-mpg"]
df.rename(columns={'highway-mpg':'highway-L/100km'}, inplace=True)

df["city-mpg"] = 235/df["city-mpg"]
df.rename(columns={'city-mpg':'city-L/100km'}, inplace=True)


#Data normalization, simple feature scaling____________________________________

df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()
df['height'] = df['height']/df['height'].max()


#Binning horsepower____________________________________________________________

#Check distribution
#plt.pyplot.hist(df["horsepower"])
#plt.pyplot.xlabel("horsepower")
#plt.pyplot.ylabel("count")
#plt.pyplot.title("horsepower bins")

#Build an array
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
group_names = ['Low', 'Medium', 'High']
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )

print(df["horsepower-binned"].value_counts())  #number of vehicles in each bin

#Check distribution for bins
#pyplot.bar(group_names, df["horsepower-binned"].value_counts())
#plt.pyplot.xlabel("horsepower")
#plt.pyplot.ylabel("count")
#plt.pyplot.title("horsepower bins")

#Histogram
plt.pyplot.hist(df["horsepower"], bins = 3)
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")


#Indicator variables___________________________________________________________
dummy_variable_1 = pd.get_dummies(df["fuel-type"])
dummy_variable_1.rename(columns={'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace=True)
df = pd.concat([df, dummy_variable_1], axis=1)
df.drop("fuel-type", axis = 1, inplace=True)

dummy_variable_2 = pd.get_dummies(df['aspiration'])
dummy_variable_2.rename(columns={'std': 'aspiration-std', 'turbo': 'aspiration-turbo'}, inplace=True)
df = pd.concat([df, dummy_variable_2], axis=1)
df.drop('aspiration', axis = 1, inplace=True)


#Save__________________________________________________________________________
df.to_csv('clean_df.csv')
