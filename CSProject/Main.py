import math
import sys

from CSProject.Contract import Contract
from CSProject.stocks import printValues

#exercise option
def calculate(Contract, moneyRange):
    rangeVal = int(Contract.getStrike())
    rangeVal2 = int(Contract.getStrike())
    for i in range(rangeVal-int(moneyRange/2), rangeVal2+int(moneyRange/2)):
        print(i)
        profit = (i-float(Contract.getStrike()))*100 - float(Contract.getPrice())*100
        print("For market price of: ", i, "your profit is ", profit)
    print("hello")


#Sell to close
def calculate(Contract, moneyRange, stc, dayRange):
    rangeVal = int(Contract.getStrike())
    rangeVal2 = int(Contract.getStrike())
    for i in range(dayRange):
        print("     day: ", i, "     ", end = "")
    for i in range(rangeVal-int(moneyRange/2), rangeVal2+int(moneyRange/2)):
        for i in range(dayRange):
            profit = float(Contract.getPrice())*100 - float()

test=Contract(101,-0.09,0.3,"2023-02-10",0.09)
calculate(test,20,True,20)




class Main(Contract):
    data = printValues("GOOG")
    x = 1
    for c in data:
        if c.getDate().__contains__("GOOG"):
            print(x, " - ", c)
            x = x + 1
    calculate(data[6], 20, True, 7)
