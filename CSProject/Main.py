import math
import sys

from CSProject.Contract import Contract
from CSProject.stocks import printValues

#exercise option
def calculate(contract, moneyRange):
    rangeVal = int(contract.getStrike())
    rangeVal2 = int(contract.getStrike())
    for i in range(rangeVal-int(moneyRange/2), rangeVal2+int(moneyRange/2)):
        print(i)
        profit = (i-float(contract.getStrike()))*100 - float(contract.getPrice())*100
        print("For market price of: ", i, "your profit is ", profit)
    print("hello")


#Sell to close
#inprogress
def calculate(contract, moneyRange, stc, dayRange):
    rangeVal = int(contract.getStrike())
    rangeVal2 = int(contract.getStrike())
    for i in range(dayRange):
        print("     day: ", i, "     ", end = "")
    print()
    for i in range(rangeVal-int(moneyRange/2), rangeVal2+int(moneyRange/2)):
        print(i, end=" ")
        for day in range(dayRange):
            counter = 1
            gammaGrowth = (i-float(contract.getStrike())) * float(contract.getGamma())
            thetaDecay = float(contract.getTheta())*day
            greekDelta = gammaGrowth + (thetaDecay)
            profit = (float(contract.getPrice()) + greekDelta)*100
            roundProfit = round(profit,2)
            print(roundProfit, end = " ")

            # print("Growth", gammaGrowth)
            # print("Decay", thetaDecay)
            # print("Delta", greekDelta)


#done
def calculatePut(contract, moneyRange):
    rangeVal = int(contract.getStrike())
    rangeVal2 = int(contract.getStrike())
    for i in range(rangeVal - int(moneyRange / 2), rangeVal2 + int(moneyRange / 2)):
        print(i)
        profit = (float(contract.getStrike())-i) * 100 - float(contract.getPrice()) * 100
        print("For market price of: ", i, "your profit is ", profit)
    print("hello")

#inprogress
def calculatePut(contract, moneyRange, stc, dayRange):
    rangeVal = int(contract.getStrike())
    rangeVal2 = int(contract.getStrike())
    for i in range(rangeVal - int(moneyRange / 2), rangeVal2 + int(moneyRange / 2)):
        print(i)
        profit = (float(contract.getStrike())-i) * 100 - float(contract.getPrice()) * 100
        print("For market price of: ", i, "your profit is ", profit)
    print("hello")






class Main(Contract):
    test = Contract(92.5, -0.0032, 0.72, "2023-02-10", 0.09)
    data = printValues("CSCO")
    #calculate(b, 20, True, 20)
    x = 0
    for c in data:
        x=x+1
        if c.getDate().__contains__("Calls"):
            print(x, " - ", c)

    calculate(data[25], 20, True, 7)


