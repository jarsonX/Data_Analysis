#STEPS
# (1) Generate a DataFrame containing the following attributes:
    # student's name,
    # student's number (5 random digits)
    # group number (I and II, 30 students in each)
    # Colloquium I grade (2-5)
    # Colloquium II grade (2-5)
    # Project grade (2-5)
# (2) Check the following:
    # How many students got the highest grade (5) from each: Colloquium 1, 2 
    # and the project?
    # How many students have not passed Colloquium 2?
    # What was the average grade for Colloquium 1 in each group?
    # What was the correlation between average grades in group I and group II?
    # What was the median for grades both groups?

import pandas as pd
import random as rd

#Functions
def gen_num():
    num = ""
    for i in range(5):
        num += str(rd.randint(0,9))
    return num

def gen_name(from_letter, to_letter):
    first_name = chr(rd.randint(ord(from_letter), ord(to_letter)))
    second_name = chr(rd.randint(ord(from_letter), ord(to_letter)))
    return first_name + "." + second_name + "."

#Main variables
list_names = []
list_album = []
list_group = []
list_coll_1 = []
list_coll_2 = []
list_project = []  

num_of_students = 100

#(1) The DataFrame:
for i in range(num_of_students):
    
    #list_names.append(rd.choice(names)+"."+rd.choice(names)+".")
    list_names.append(gen_name('A','Z'))
    list_album.append(gen_num())
    list_coll_1.append(rd.randint(2, 5))
    list_coll_2.append(rd.randint(2, 5))
    list_project.append(rd.randint(2, 5)) 
    if i < (num_of_students / 2):
        list_group.append('I')
    else:
        list_group.append('II')
        
# df = pd.DataFrame(list_names)
# df.set_axis(['Name'], axis=1, inplace=True)
# df['Album'] = list_album
# df['Group'] = list_group
# df['Colloquium_1'] = list_coll_1
# df['Colloquium_2'] = list_coll_2
# df['Project'] = list_project

#Alternatively, which is more readable for me:
df = pd.DataFrame()
df['Name'] = list_names
df['Album'] = list_album
df['Group'] = list_group
df['Colloquium_1'] = list_coll_1
df['Colloquium_2'] = list_coll_2
df['Project'] = list_project

#Averages is needed later on to calcualte correlation so it can be added to df right away.
df['Average'] = df.apply(lambda row : round(((row[3]+row[4]+row[5])/3),1), axis=1)

print(df)

#(2) Solution

# How many students got the highest grade (5) from each: Colloquium 1, 2 
# and the project?
print('\nStudents who got max grade from Colloquium 1:','\t', (df['Colloquium_1']==5).sum())
print('Students who got max grade from Colloquium 2:','\t', (df['Colloquium_2']==5).sum())
print('Students who got max grade from the project:','\t', (df['Project']==5).sum())

# How many students have not passed Colloquium 2?
print('Students who have not passed Colloquium 2:','\t'*2, (df['Colloquium_2']==2).sum())

# What was the average grade for Colloquium 1 in each group?
mean_I_coll_1 = round(df[df['Group'] == 'I']['Colloquium_1'].mean(),1)
mean_II_coll_1 = round(df[df['Group'] == 'II']['Colloquium_1'].mean(),1)
print('Colloquium 1 mean for Group I:', '\t'*5, mean_I_coll_1)
print('Colloquium 1 mean for Group II:', '\t'*4, mean_II_coll_1)

# What was the correlation between the above averages?
avg_I = pd.Series(list(df[df['Group'] == 'I']['Average']))
avg_II = pd.Series(list(df[df['Group'] == 'II']['Average']))
# For some reason I needed to take out a column, then convert it to a list,
# then back to a series. Otherwise (when calculating corr directly on columns),
# result was NaN.
correlation = avg_I.corr(avg_II)
print('Correlation between average grades in groups:', '\t', round(correlation,2))

# What was the median for grades in both groups?
grades_in_I = df[df['Group'] == 'I']['Colloquium_1'].append(df[df['Group'] == 'I']['Colloquium_2']).append(df[df['Group'] == 'I']['Project'])
print('Median for grades in Group I:', '\t'*5, grades_in_I.median())
grades_in_II = df[df['Group'] == 'II']['Colloquium_1'].append(df[df['Group'] == 'II']['Colloquium_2']).append(df[df['Group'] == 'II']['Project'])
print('Median for grades in Group II:', '\t'*5, grades_in_II.median())
