#Scrape data from HTML table in respect of color name and hex code.
#Save findings to a file.

import requests
from bs4 import BeautifulSoup

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
data  = requests.get(url).text 

soup = BeautifulSoup(data, 'html.parser')

table = soup.find('table')

with open(r"C:\Users\krzys\Desktop\scrap_02.txt", "w") as writefile:

    for row in table.find_all('tr'):
        cols = row.find_all('td')
        color_num = cols[0].string
        color_name = cols[2].string
        color_code = cols[3].string
        if color_num.isalnum():  #we do not need the headings
            print("{} \t {} \t {}".format(color_num, color_code, color_name), \
                  file = writefile)

print("Done")
