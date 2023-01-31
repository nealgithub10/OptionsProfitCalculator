import math
import sys

from Contract import Contract
from stocks import printValues

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
#you mfs do this
def calculate(Contract, moneyRange, stc, dayRange):
    rangeVal = int(Contract.getStrike())
    rangeVal2 = int(Contract.getStrike())
    #for i in range(dayRange):
        #print("     day: ", i, "     ", end = "")
    for i in range(rangeVal-int(moneyRange/2), rangeVal2+int(moneyRange/2)):
        for day in range(dayRange):

            print((Contract.getTheta()))

            gammaGrowth = (i-float(Contract.getStrike())) * float(Contract.getGamma())
            thetaDecay = float(Contract.getTheta())*day

            greekDelta = gammaGrowth + (thetaDecay)

            print(Contract.getGamma())

            #print(greekDelta)

            profit = (float(Contract.getPrice()) + greekDelta)*100

def calculatePut(Contract, moneyRange):
    rangeVal = int(Contract.getStrike())
    rangeVal2 = int(Contract.getStrike())
    for i in range(rangeVal - int(moneyRange / 2), rangeVal2 + int(moneyRange / 2)):
        print(i)
        profit = (float(Contract.getStrike())-i) * 100 - float(Contract.getPrice()) * 100
        print("For market price of: ", i, "your profit is ", profit)
    print("hello")

def calculatePut(Contract, moneyRange, stc, dayRange):
    rangeVal = int(Contract.getStrike())
    rangeVal2 = int(Contract.getStrike())
    for i in range(rangeVal - int(moneyRange / 2), rangeVal2 + int(moneyRange / 2)):
        print(i)
        profit = (float(Contract.getStrike())-i) * 100 - float(Contract.getPrice()) * 100
        print("For market price of: ", i, "your profit is ", profit)
    print("hello")

class Main(Contract):


    test = Contract(92.5, -0.0032, 0.72, "023-02-10", 0.09)

    data = printValues("GOOG")
    calculate(data[3], 20, True, 20)

    x = 1
    for c in data:
        if c.getDate().__contains__("2023-02-10"):
            print(x, " - ", c)
            x = x + 1
