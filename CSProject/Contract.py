class Contract:
    def __init__(self, strike, theta, price, date, gamma):
        self.strike = strike
        self.theta = theta
        self.price = price
        self.date = date
        self.gamma = gamma

    def getStrike(self):
        return self.strike

    def getTheta(self):
        return self.theta

    def getPrice(self):
        return self.price

    def getDate(self):
        return self.date

    def setStrike(self, strike):
        self.strike = strike

    def setTheta(self, theta):
        self.theta = theta

    def setPrice(self, price):
        self.price = price

    def setDate(self, date):
        self.date = date

    def setGamma(self, gamma):
        self.gamma = gamma

    def getGamma(self):
        return self.gamma

    def __str__(self):
        return  "strike:" + self.strike + ", price:" + self.price + ", thetha:" + self.theta + ", date: " + self.date + ", gamma:" + self.gamma



