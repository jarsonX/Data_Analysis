#Exploring different ways to scrape data from HTML into a DataFrame

#Scrape data in respect of '10 most densly populated countries' from HTML into
#a DataFrame using:
    # (1) BeautifulSoup and Pandas
    # (2) BeautifulSoup and read_html (from Pandas)
    # (3) read_html to get DataFrame directly from url

import pandas as pd
import requests
from bs4 import BeautifulSoup

#Load data
##############################################################################
url = "https://en.wikipedia.org/wiki/World_population"
data = requests.get(url).text

soup = BeautifulSoup(data,"html.parser")

#Identify the correct table
tables = soup.find_all('table')  #finds all <table> tags


#(1) BeautifulSoup and Pandas
##############################################################################
#We load all tables, find the one that we need, create an empty DataFrame and
#fill it up column by column using a for loop.

print("(1) BeautifulSoup and Pandas")
print('---------------------------------------------------')

for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
        
print("Tables found:", len(tables))        
print("Index of the correct table:", table_index,"\n")
#print(tables[table_index].prettify())  #for inspection, if needed

#Create a DataFrame, then fill it wih a for loop
population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

print(population_data)
print("\n")

#(2) BeautifulSoup and read_html (from Pandas)
##############################################################################
#We load all tables, find the one that we need and convert it to a DataFrame.

print("(2) BeautifulSoup and read_html")
print('---------------------------------------------------')
#The table is already identified as tables[5].

#We can now use the pandas function read_html and give it the string version 
#of the table as well as the flavor which is the parsing engine bs4.

pd.read_html(str(tables[5]), flavor='bs4')

#The function read_html always returns a list of DataFrames so we must pick 
#the one we want out of the list (which basically is the only one inlcuded).

population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0]
print(population_data_read_html)
print("\n")

#(3) read_html to get DataFrame directly from url
##############################################################################
#We load all tables as DataFrames and pick the one that we need or load only
#the one we need using match (which is recommended).

print("(3) read_html to get DataFrame directly from url")
print('---------------------------------------------------')
#The table is already identified as tables[5].

#Approach 1 - load all the tables
dataframe_list = pd.read_html(url, flavor='bs4')
dataframe_list[5]

#Approach 2 - load only the table we need (recommended, if possible)
dataframe = pd.read_html(url, match="10 most densely populated countries", \
                         flavor='bs4')[0]
print(dataframe)
