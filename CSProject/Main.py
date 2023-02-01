import math
import sys

from CSProject.Contract import Contract
from CSProject.stocks import printValues
from datetime import date
from datetime import datetime


# For the following two methods, moneyRange is the amount of market prices to show the user

# This calculates the profit if one were to exercise the call option
def calculate(contract, moneyRange):
    rangeVal = int(contract.getStrike())
    rangeVal2 = int(contract.getStrike())
    for i in range(rangeVal - int(moneyRange / 2), rangeVal2 + int(moneyRange / 2)):
        print(i)
        profit = (i - float(contract.getStrike())) * 100 - float(contract.getPrice()) * 100
        print("For market price of: ", i, "your profit is ", profit)
    print("hello")


# This calculates the profit if one were to exercise the call option
def calculatePut(contract, moneyRange):
    rangeVal = int(contract.getStrike())
    rangeVal2 = int(contract.getStrike())
    for i in range(rangeVal - int(moneyRange / 2), rangeVal2 + int(moneyRange / 2)):
        print(i)
        profit = (float(contract.getStrike()) - i) * 100 - float(contract.getPrice()) * 100
        print("For market price of: ", i, "your profit is ", profit)
    print("hello")


# This calculates the profit if one were to Sell to close a current call contract position
# The following two methods implement the greeks, specifically theta and delta
# They are used to predict the way that the contract's price will move based on the elapsed time and how the market price changes
# GreekDelta is the amount that the option will vary from the original price
# profit equals the amount the price has changed, which is greekDelta
# this profit calculation assumes that implied volatility's delta has been minimal
# ^ predicting that requires much more analysis of the current market

def calculate(contract, moneyRange, stc, dayRange):
    rangeVal = int(contract.getStrike())
    rangeVal2 = int(contract.getStrike())
    print("            ")
    for i in range(dayRange):
        print("       day: ", i, end="")
    print()
    for i in range(rangeVal - int(moneyRange / 2), rangeVal2 + int(moneyRange / 2)):
        print(i, end=" ")
        for day in range(dayRange):
            #amt the price of the option changes per dollar that the market price changes
            deltaGrowth = (i - float(contract.getStrike())) * float(contract.getDelta()) * 100
            #amt the price of the option decreases per day
            thetaDecay = float(contract.getTheta()) * day * 100
            greekDelta = deltaGrowth + (thetaDecay)
            profit = (greekDelta)
            roundProfit = round(profit, 2)
            print("      ", end=" ")
            print(roundProfit, end=" ")
        print()

        # print("Growth", gammaGrowth)
        # print("Decay", thetaDecay)
        # print("Delta", greekDelta)


# This calculates the profit if one were to Sell to close a current put contract position
def calculatePut(contract, moneyRange, stc, dayRange):
    rangeVal = int(contract.getStrike())
    rangeVal2 = int(contract.getStrike())
    print("            ")
    for i in range(dayRange):
        print("       day: ", i, end="")
    print()
    for i in range(rangeVal - int(moneyRange / 2), rangeVal2 + int(moneyRange / 2)):
        print(i, end=" ")
        for day in range(dayRange):
            value = float(contract.getDelta())
            if float(contract.getDelta()) > 0:
                contract.setDelta(value * -1)
            #amt the price of the option changes per dollar that the market price changes
            deltaGrowth = (i - float(contract.getStrike())) * (float(contract.getDelta())) * 100
            #amt the price of the option decreases per day
            thetaDecay = float(contract.getTheta()) * day * 100
            greekDelta = deltaGrowth + (thetaDecay)
            profit = (greekDelta)
            roundProfit = round(profit, 2)
            print("      ", end=" ")
            print(roundProfit, end=" ")
        print()

        # print("Growth", gammaGrowth)
        # print("Decay", thetaDecay)
        # print("Delta", greekDelta)
