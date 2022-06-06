import pandas as pd
import numpy as np
import pandas_datareader as dr
import datetime
from datetime import timedelta

today = datetime.date.today()
today_minus_4 = today + timedelta(days = -4)
year = 365


class Asset:
    def __init__(self, name, ticker, cost, shares, date_bought, index):
        self.name = name
        self.index = index
        self.ticker = ticker
        self.cost = cost
        self.shares = shares
        self.date_bought = date_bought
        self.days_owned = today - self.date_bought
        self.days_owned = self.days_owned.days
        self.prelast4 = dr.get_data_tiingo(self.ticker, today_minus_4, today, api_key=  "7b520850b29450407b9494de68d597853a5e61c5")
        self.last4 = self.prelast4.reset_index(drop = True)
        self.price = self.last4.iloc[[-1], [0]]
        self.price = float(self.price.to_string(index = False, header = None))
        self.ur_profit = self.price - self.cost 

    def dividend(self):
        self.dividend = self.last4.iloc[[-1], [6]]
        self.dividend = float(self.dividend.to_string(index = False, header = None))
        self.cash = self.shares * self.dividend
        self.cash_total += self.cash
        self.total_ur_profit = self.cash_total + self.ur_profit
    def returns5year(self):
        years5 = year * (-5)
        start = today + timedelta(days = years5)
        data = dr.get_data_tiingo(self.ticker, start, today, api_key=  "7b520850b29450407b9494de68d597853a5e61c5")
        prices = data["adjClose"].reset_index(drop = True)
        returns = ((prices / prices.shift(1)) - 1) * 100
        self.variance5 = returns.var()
        self.std5 = returns.std()
        self.returns5 = ((prices.iloc[-1] / prices.iloc[0]) - 1) * 100
        return self.variance5, self.std5, self.returns5;
    def returns1(self):
        years1 = year * (-1)
        start = today + timedelta(days = years1)
        data = dr.get_data_tiingo(self.ticker, start, today, api_key=  "7b520850b29450407b9494de68d597853a5e61c5")
        prices = data["adjClose"].reset_index(drop = True)
        returns = ((prices / prices.shift(1)) - 1) * 100
        self.variance1 = returns.var()
        self.std1 = returns.std()
        self.returns1 = ((prices.iloc[-1] / prices.iloc[0]) - 1) * 100
        return self.variance1, self.std1, self.returns1;
    def annualized_return(self):
        a = ((self.cost + self.ur_profit) / self.cost) ** (365/self.days_owned) - 1
        return a
portfolio = []
def add_to_portfolio(name, ticker, cost, shares, date):
    x = len(portfolio)
    ticker = Asset(name, ticker, cost, shares, date, x)
    portfolio.append(ticker)
def portfolio_weight():
    a = []
    for i in portfolio:
        a.append((i.price / (sum(i.price for i in portfolio))) * 100)
    return a
def portfolio_purchase_weight():
    a = []
    for i in portfolio:
        a.append((i.cost / (sum(i.cost for i in portfolio))) * 100)
    return a

def portfolio_annualized_return_part1():
    a = []
    for i in portfolio:
        a.append(i.annualized_return() * (i.price / (sum(i.price for i in portfolio))))
    return a
def portfolio_annualized_return():
    a = sum(portfolio_annualized_return_part1())
    return a


#test
a = input("Stock Name")
b = input("Stock Ticker")
c = input("Cost")
d = input("Shares")
e = int(input("Year"))
f = int(input("month"))
g = int(input("day"))
add_to_portfolio(a, b, float(c), float(d), datetime.date(e, f, g))
print(portfolio[0].ticker)
print(portfolio[0].dividend())
