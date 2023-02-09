import math
import sys

from Contract import Contract
from stocks import printValues
from datetime import date
from datetime import datetime

import tkinter as tk

from tabulate import tabulate


# For the following two methods, moneyRange is the amount of market prices to show the user

# This calculates the profit if one were to exercise the call option
def calculate1(contract, moneyRange):
    rangeVal = int(contract.getStrike())
    rangeVal2 = int(contract.getStrike())
    for i in range(rangeVal - int(moneyRange / 2), rangeVal2 + int(moneyRange / 2)):
        print(i)
        profit = (i - float(contract.getStrike())) * 100 - float(contract.getPrice()) * 100
        print("For market price of: ", i, "your profit is ", profit)


# This calculates the profit if one were to exercise the put option
def calculatePut1(contract, moneyRange):
    rangeVal = int(contract.getStrike())
    rangeVal2 = int(contract.getStrike())
    for i in range(rangeVal - int(moneyRange / 2), rangeVal2 + int(moneyRange / 2)):
        print(i)
        profit = (float(contract.getStrike()) - i) * 100 - float(contract.getPrice()) * 100
        print("For market price of: ", i, "your profit is ", profit)


# This calculates the profit if one were to Sell to close a current call contract position
# The following two methods implement the greeks, specifically theta and delta
# They are used to predict the way that the contract's price will move based on the elapsed time and how the market price changes
# GreekDelta is the amount that the option will vary from the original price
# profit equals the amount the price has changed, which is greekDelta
# this profit calculation assumes that implied volatility's delta has been minimal
# ^ predicting that requires much more analysis of the current market

def calculate2(contract, moneyRange, stc, dayRange):
    rangeVal = int(float(contract.getStrike()))
    rangeVal2 = int(float(contract.getStrike()))
    table = []
    headers = []
    headers.append("market Price")
    for i in range(dayRange):
        headers.append("days " + str(i))
    table.append(headers)
    print()
    for i in range(rangeVal - int(moneyRange / 2), rangeVal2 + int(moneyRange / 2)):
        data = []
        data.append(i)
        for day in range(dayRange):
            #amt the price of the option changes per dollar that the market price changes
            deltaGrowth = (i - float(contract.getStrike())) * float(contract.getDelta()) * 100
            #amt the price of the option decreases per day
            thetaDecay = float(contract.getTheta()) * day * 100
            greekDelta = deltaGrowth + (thetaDecay)
            profit = (greekDelta)
            roundProfit = round(profit, 2)
            data.append(roundProfit)
        table.append(data)
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))



    # print("Growth", gammaGrowth)
        # print("Decay", thetaDecay)
        # print("Delta", greekDelta)


# This calculates the profit if one were to Sell to close a current put contract position
def calculatePut2(contract, moneyRange, stc, dayRange):
    rangeVal = int(float(contract.getStrike()))
    rangeVal2 = int(float(contract.getStrike()))
    table = []
    header=[]
    header.append("marketPrice")
    for i in range(dayRange):
        header.append("day " + str(i))
    table.append(header)
    for i in range(rangeVal - int(moneyRange / 2), rangeVal2 + int(moneyRange / 2)):
        dataRow = []
        dataRow.append(i)
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
            dataRow.append(roundProfit)

        table.append(dataRow)
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

        # print("Growth", gammaGrowth)
        # print("Decay", thetaDecay)
        # print("Delta", greekDelta)


class Main:
    tickr = input("Enter a tickr symbol from NYSE: ")
    print(tickr)

    data = printValues(tickr)

    x=0
    for d in data:
        x+=1
        print(x, ': ', d)

    contractNum = int(input("Enter the number corresponding to the contract you want: "))

    myContract = data[contractNum-1]

    print("Here is the contract you chose: ", myContract)



    if ("Call" in myContract.getDate()):
        orderType = input("exercise or stc? ")
        if (orderType == "exercise"):
            moneyRange = int(input("Please enter the money range you want to display"))
            calculate1(myContract, moneyRange)
        if (orderType == "stc"):
            moneyRange = int(input("Please enter the money range you want to display"))
            dayRange = int(input("Please enter the day range you want to display"))

            print("Calc2")
            calculate2(myContract, moneyRange, True, dayRange)

    if ("Put" in myContract.getDate()):
        orderType = input("exercise or stc? ")
        if (orderType == "exercise"):
            moneyRange = int(input("Please enter the money range you want to display"))
            calculatePut1(myContract, moneyRange)
        if (orderType == "stc"):
            moneyRange = int(input("Please enter the money range you want to display"))
            dayRange = int(input("Please enter the day range you want to display"))

            print("CalculatePut2")
            calculatePut2(myContract, moneyRange, True, dayRange)
