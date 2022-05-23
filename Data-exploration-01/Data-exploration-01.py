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
    # What was the median for grades in group 2?

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

num_of_students = 60

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
        
df = pd.DataFrame(list_names)  # df = DataFrame
df.set_axis(['Name'], axis=1, inplace=True)
df['Album'] = list_album
df['Group'] = list_group
df['Colloquium_1'] = list_coll_1
df['Colloquium_2'] = list_coll_2
df['Project'] = list_project

print(df)

#(2) Solution
print('\nStudents who got max grade from Colloquium 1:','\t', (df['Colloquium_1']==5).sum())
print('Students who got max grade from Colloquium 2:','\t', (df['Colloquium_2']==5).sum())
print('Students who have not passed Colloquium 2:','\t'*2, (df['Colloquium_2']==2).sum())
print('Students who got max grade from the project:','\t'*2, (df['Project']==5).sum())

mean_I_coll_1 = round(df[df['Group'] == 'I']['Colloquium_1'].mean(),2)
mean_II_coll_1 = round(df[df['Group'] == 'II']['Colloquium_1'].mean(),2)
print('Colloquium 1 mean for Group I:', '\t'*5, mean_I_coll_1)
print('Colloquium 1 mean for Group II:', '\t'*5, mean_II_coll_1)

grades_in_II = df[df['Group'] == 'II']['Colloquium_1'].append(df[df['Group'] == 'II']['Colloquium_2']).append(df[df['Group'] == 'II']['Project'])
print('Median for grades in Group II:', '\t'*5, grades_in_II.median())






        

