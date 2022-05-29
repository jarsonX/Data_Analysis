#DIABETES DATASET ANALYSIS

# Context: This dataset is originally from the National Institute of Diabetes and 
# Digestive and Kidney Diseases. The objective of the dataset is to diagnostically 
# predict whether or not a patient has diabetes, based on certain diagnostic 
# measurements included in the dataset. Several constraints were placed on the 
# selection of these instances from a larger database. In particular, all patients 
# here are females at least 21 years of age of Pima Indian heritage.

# Content: The datasets consists of several medical predictor variables and one 
# target variable, Outcome. Predictor variables includes the number of pregnancies 
# the patient has had, their BMI, insulin level, age, and so on.

# Structure: 768 rows and 9 columns. The first 8 columns respresent the features
# and the last column represent the target/label.

# Things to check:
    # data structure
    # missing values
    # data types
    # basic statistics

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_rows", 10, "display.max_columns", None) 

df = pd.read_csv(r'C:\Users\krzys\Desktop\diabetes.csv')

#Data structure
df.shape  #rows x cols
df.ndim   #dimensions

#Technical overview
#df.info()

#The above already gave us most answers we required, yet we will do additional
#checks just for practice.

#Missing data
missing_data = df.isnull()  #alternative: df.notnull() approach

for column in missing_data.columns.values.tolist():
     print(column)
     print (missing_data[column].value_counts())
     print("") 

#Data types
df.dtypes
 
#Statistical overview
df.describe()  

#Visualization
plt.pie(df['Outcome'].value_counts(),labels=['Diabetic', 'Not Diabetic'],autopct='%0.02f%%')
plt.legend()
plt.show()
