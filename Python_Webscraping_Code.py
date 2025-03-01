import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Geography_of_association_football"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
tables = soup.find_all('table', class_='wikitable')[5:10]
list=[]
for table in tables:
    rows = table.find_all('tr')
    for row in rows :
        columns = row.find_all('td')
        if len(columns) >= 2 :
            country = columns[0].get_text(strip=True)
            sub_confederation = columns[1].get_text(strip=True)
            code = columns[2].get_text(strip=True)
            list.append([country,sub_confederation,code])
           
df=pd.DataFrame(list,columns=['country','sub_confederation','code']) 
df.to_excel('countries.xlsx',index = False , engine ='openpyxl' )

        