from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import requests
import json

languages=["arab","bengali","english","german","greek","gujarati","hungarian",
            "italian","japanese-katakana","latin","malayalam","myanmar",
            "french","oriya","polish","russian","devanagari","saurashtra",
            "japanese-hiragana","sinhala","tamil","telugu","thai",
            "spanish","turkish"
            ]

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

filename = "newset.csv"
# opening the file with w+ mode truncates the file
f = open(filename, "w+")
f.close()

for language in languages:
    url="https://unicode-table.com/en/alphabets/"+language+"/"
    r=requests.get(url,headers=headers)

    soup=BeautifulSoup(r.content,"html.parser")
    li=soup.find_all('li',{ "class" : "character-list__item" })
    # print(li[0])
    data=list()

    for item in li:
        div=item.find_all('div')
        el = [i.text  for i in div]
        # print(el)
        data.append(el[::-1])

    
    df_bs=pd.DataFrame(data,columns=['Unicode','Character'])
    df_bs.set_index('Unicode',inplace=True)
    df_bs.to_csv('newset.csv', mode='a', index='Unicode', header=False)
    # df_bs.to_csv('newset.csv')

