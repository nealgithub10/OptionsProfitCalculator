import sys

from CSProject.Contract import Contract
from CSProject.stocks import printValues


class Main:

    tickr = input("Please enter Tickr Symbol: ")

    date = input("Please enter expiry date: ")

    data = printValues(tickr)
    for c in data:
        if c.getDate().__contains__(date):
            print(c)


