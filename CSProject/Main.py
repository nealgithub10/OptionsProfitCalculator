import math
import sys

from CSProject.Contract import Contract
from CSProject.stocks import printValues


def calculate(Contract, moneyRange):
    rangeVal = math.floor(Contract.getStrike())
    rangeVal2 = math.ceil(Contract.getStrike())
    for i in range(rangeVal-moneyRange/2, rangeVal2+moneyRange/2):
        profit = (i-Contract.getStrike())*100 - Contract.getPrice()*100
        print("For market price of: " + i + "your profit is " + profit)
    print("hello")



class Main(Contract):

    #tickr = input("Please enter Tickr Symbol: ")

    ##date = input("Please enter expiry date: ")

    #data = printValues(tickr)
    #x = 1
    #for c in data:
    #    if c.getDate().__contains__(date):
    #        print(x, " - ", c)
    #        x=x+1



    test = Contract(21.5, -0.00324, 0.01, "2023 - 02 - 17")
    print(test.getDate())
    print(int(test.getStrike()))
    #contractSelection = int(input("Enter the number corresponding to the contract you want"))
    #print(contractSelection)
    #calculate(data[contractSelection], 20)


