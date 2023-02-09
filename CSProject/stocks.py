#Scrape class

## sudo python -m ensurepip
## sudo pip install requests
## sudo pip install bs4

## To Run -  python stocks.py <symbol>

import requests
import sys
from bs4 import BeautifulSoup

from Contract import Contract
from datetime import date
import datetime

#This is to get the current date, since the query will change
#Doesn't work currently due to the way market hours work
#From 6:30 am to 1 pm on a given day, the website for options chains considers it the previous day
#For example, irl it is Jan 31 at 12 Am, but for the options chain, it is Jan 31 starting at 1 pm, after market closes
date = date.today()
today = date.today()
dateStr = (str(today).replace("-", ""))

def printValues(symbol):
  #This value must be changed daily
  #getting the current date does not work because of market hours
  date = '20230208'
  #This is the url and query that we want to scrap
  scrape_url = 'https://www.optionistics.com/quotes/stock-option-chains/' + symbol + '?symbol=' + symbol + '&chtype=0&nonstd=-1&greeks=1&mn1min=4&mn1max=10&expmin=0&expmax=2&ovmin=0&ovmax=6&strike=&expiry=&op=chains&date=' + date + '&prevsym=ASA&clear=0&prevns=-1&prevns=ASA&v=1'
  html_text = requests.get(scrape_url).text
  soup = BeautifulSoup(html_text, 'html.parser')
  tables = soup.find_all('table')

  #array to contain the contracts
  data=[]
  for table in tables:
    date=""
    #strings like 'tr' and 'td' are identifiers for the tables on the website to scrape
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
          delta = columns[11].text
          #create a contract object with the scraped attributes
          c = Contract(strike, theta, price, date, gamma, delta)
          data.append(c)

    return data




