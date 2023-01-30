## sudo python -m ensurepip
## sudo pip install requests
## sudo pip install bs4

## To Run -  python stocks.py <symbol>

import requests
import sys
from bs4 import BeautifulSoup

from CSProject.Contract import Contract




def printValues(symbol):
  scrape_url = 'https://www.optionistics.com/quotes/stock-option-chains/' + symbol + '?symbol=' + symbol + '&chtype=0&nonstd=-1&greeks=1&mn1min=21&mn1max=27&expmin=0&expmax=2&ovmin=0&ovmax=6&strike=&expiry=&op=chains&date=20230127&prevsym=CSCO&clear=0&prevns=-1&prevns=CSCO&v=1'

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

      if col_length >= 17 and col.has_attr('class') and (col.attrs.get("class")[0] != "inmoney" or col.attrs.get("class")[0] != "outmoney"):
        strike = columns[0].text
        if (strike != "Strike"):
          price= columns[4].text
          thetha = columns[12].text
          gamma = columns[13].text
          output = "strike:" + strike + ", price:" + price + ", thetha:" + thetha + ", gamma:" + gamma
          #print(output)

          c = Contract(strike, thetha, price, date, gamma)

          output_map = {
            "date": date,
            "strike": strike,
            "price": price,
            "thetha": thetha,
            "gamma": gamma
          }
          data.append(c)
    return data



symbol=sys.argv[1]





