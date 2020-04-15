# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:19:37 2020

@author: Vincent
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:53:43 2020

@author: Vincent
"""

from bs4 import BeautifulSoup
import csv
import requests
from requests_html import HTMLSession  
import Utilities

link = 'https://mylotto.co.nz/results'
apiLink = 'https://apigw.mylotto.co.nz/api/results/v1/results/lotto/'
parseType = 'lxml'
keyDrawTerm = 'lotto-draw-select-dropdown'
columnHeader = ['Date of Draw','Number 1','Number 2','Number 3','Number 4','Number 5','Number 6','Bonus Ball']
keyPowerball = ['lotto','lottoWinningNumbers','numbers']
keyBonusball = ['lotto','lottoWinningNumbers','bonusBalls']
outFilename = 'output.csv'

page = requests.get(link)

myhtml = Utilities.getHtml(link).html
#soup = BeautifulSoup (myhtml, "lxml")
soup = BeautifulSoup (myhtml, parseType)

#Extract the draw number
#options = soup.find(id="lotto-draw-select-dropdown")
options = soup.find(id=keyDrawTerm)

drawDate = []
drawTerm = []
for option in options:
    drawTerm.append (option.text[:4])
    drawDate.append (option['value'])

#First Item is coming draw, remove from array
drawTerm.pop(0)
drawDate.pop(0)


Resultlist = []
i=0
Resultlist.append(columnHeader)
for term in drawTerm:
    Result = []
    link = apiLink + term
    print (link)
    Result.append(drawDate[i])
    numbers = Utilities.extractDrawResult(link,keyPowerball)
    for number in numbers:
        Result.append(number)
    Result.append(Utilities.extractDrawResult(link,keyBonusball))
    Resultlist.append(Result)
    i+=1

with open(outFilename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(Resultlist)
