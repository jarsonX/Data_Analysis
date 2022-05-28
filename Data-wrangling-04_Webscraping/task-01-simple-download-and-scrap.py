#Downloading And Scraping The Contents Of A Web Page

#Scrape all links
#Scrape all images Tags
#Save results to a file

import requests
from bs4 import BeautifulSoup

#Get and prepare data
url = "http://www.ibm.com"
data  = requests.get(url).text 

soup = BeautifulSoup(data,"html.parser")

#Save data
write_file = open(r"C:\...\scrap_01.txt", 'w')

print("Links", file=write_file)
for link in soup.find_all('a',href=True):
    print(link.get('href'), file=write_file)

print("Images Tags", file=write_file)
for link in soup.find_all('img'):
    print(link, file=write_file)
    print(link.get('src'), file=write_file)
    
write_file.close()
print("Done")
