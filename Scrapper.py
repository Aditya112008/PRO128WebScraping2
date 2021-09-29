from bs4 import BeautifulSoup as bs
from selenium import webdriver
import requests
import pandas as pd


list_of_brown_dwarfs= 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
browser = webdriver.Chrome("D:/Aditya/Whitehat Jr/Module 3/PRO128/chromedriver")
browser.get(list_of_brown_dwarfs)
page = requests.get(list_of_brown_dwarfs)                           
print(page) 

soup = bs(page.text,'html.parser')

star_table = soup.find('table')

temp_list= []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)



Star_name = []
Distance =[]
Mass = []
Radius =[]


for i in range(1,len(temp_list)):
    Star_name.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    
df2 = pd.DataFrame(list(zip(Star_name,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('list_of_brown_dwarfs.csv')