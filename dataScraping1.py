import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

BRIGHT_STARS_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page=requests.get(BRIGHT_STARS_URL)
print(page)

soup=bs(page.text,'html.parser')
star_table=soup.find('table')

temp_list=[]
table_row=star_table.find_all('tr')
for tr in table_row:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td ]
    temp_list.append(row)

star_names=[]
distance=[]
mass=[]
radius=[]
lum=[]

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    lum.append(temp_list[i][7])
df2= pd.DataFrame(list(zip(star_names,distance,mass,radius,lum)),columns=['Star_name','Distance','Mass', 'Radius', 'Luminosity'])
df2.to_csv('bright_stars.csv')