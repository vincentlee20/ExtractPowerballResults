import requests
from requests_html import HTMLSession  


def extractDrawResult(URL,keys): 
    page = requests.get(URL).json()
    for key in keys:
        page = page.get(key)
    #return(page.json().get('lotto').get('lottoWinningNumbers'))
    return page


#Make a HTML request to return the HTML 
def getHtml(URL):
    session = HTMLSession()
    r = session.get(URL)
    r.html.render()
    return r.html

"""
#link = 'https://apigw.mylotto.co.nz/api/results/v1/results/lotto/1947'
link= 'https://apigw.mylotto.co.nz/api/results/v1/results/lotto/1951' 
Result = extractDrawResult(link,['lotto','lottoWinningNumbers','numbers'])
Result.append(extractDrawResult(link,['lotto','lottoWinningNumbers','bonusBalls']))
print (Result)
"""