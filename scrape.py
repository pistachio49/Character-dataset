from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import requests
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
url = "https://www.ssec.wisc.edu/~tomw/java/unicode.html#x0D00"
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.content, "html.parser")
table = soup.find_all('table',{"border" : "2"})
data=list()

for tab in table:
    rows=soup.find_all('tr')
    
    for tr in rows:
        td = tr.find_all('td')
        row = [i.text  for i in td]
        if row:
            row.pop(2)
    
        data.append(row)
        # break
    break

df_bs=pd.DataFrame(data,columns=['Position','Decimal','Appearance'])
df_bs.set_index('Position',inplace=True)
df_bs.to_csv('beautifulsoup.csv')


# with open("table.txt", "w", encoding="utf-8") as f:
#     for tab in table:
#         rows=soup.find_all('tr')
        
#         for tr in rows:
#             td = tr.find_all('td')
#             row = [i.text for i in td]
#             data.append(row)
#             f.write(str(data))

# f.close()

# import time

# page = ''
# while page == '':
#     try:
#         page = requests.get(url, headers=headers)
#         break
#     except:
#         print("Connection refused by the server..")
#         print("Let me sleep for 5 seconds")
#         print("ZZzzzz...")
#         time.sleep(5)
#         print("Was a nice sleep, now let me continue...")
#         continue