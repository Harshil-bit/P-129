import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page=requests.get(url)
print(page)

soup=bs(page.text,'html.parser')
star_table=soup.find_all('table')

print(len(star_table))
temp_list=[]
table_row=star_table[4].find_all('tr')
for tr in table_row:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td ]
    temp_list.append(row)

star_names=[]
distance=[]
mass=[]
radius=[]

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])
    
df2= pd.DataFrame(list(zip(star_names,distance,mass,radius)),columns=['Star_name','Distance','Mass', 'Radius'])
df2.to_csv('dwarf_stars.csv')