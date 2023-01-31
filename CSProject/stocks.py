## sudo python -m ensurepip
## sudo pip install requests
## sudo pip install bs4

## To Run -  python stocks.py <symbol>

import requests
import sys
from bs4 import BeautifulSoup

from Contract import Contract


def printValues(symbol):
  #scrape_url = 'https://www.optionistics.com/quotes/stock-option-chains/' + symbol + '?symbol=' + symbol + '&chtype=0&nonstd=-1&greeks=1&mn1min=21&mn1max=27&expmin=0&expmax=2&ovmin=0&ovmax=6&strike=&expiry=&op=chains&date=20230127&prevsym=CSCO&clear=0&prevns=-1&prevns=CSCO&v=1'
  scrape_url = 'https://www.optionistics.com/quotes/stock-option-chains/' + symbol + '?symbol=' + symbol + '&chtype=0&nonstd=-1&greeks=1&mn1min=4&mn1max=10&expmin=0&expmax=2&ovmin=0&ovmax=6&strike=&expiry=&op=chains&date=20230130&prevsym=ASA&clear=0&prevns=-1&prevns=ASA&v=1'
  html_text = requests.get(scrape_url).text
  soup = BeautifulSoup(html_text, 'html.parser')
  tables = soup.find_all('table')

  data=[]
  for table in tables:
    date=""
    for row in table.find_all('tr'):
      columns = row.find_all('td')
      col_length = len(columns)
      # print( col_length)
      if col_length == 1:
        for col in columns:
          if col.has_attr('class') and col.attrs.get("class")[0] != "disclaimer":
            date=col.text

      if col_length >= 17 and columns[0].has_attr('class'):
        #print("---------------------")
        #print(columns[0].attrs)
        strike = columns[0].text
        #print(strike)
        if (strike != "Strike"):
          price= columns[4].text
          theta = columns[12].text
          gamma = columns[13].text
          c = Contract(strike, theta, price, date, gamma)
          data.append(c)

    return data




