# -*- coding: utf-8 -*-

class Stocks(object):

    def __init__(self):
        self.stocks = []
        self.cash_on_hand = 15000

    def buy(self, company, num_shares, unit_price):
        self.stocks.append([company, num_shares, unit_price])

    def sell(self, company, num_shares):
        idx = -1
        for xact in self.stocks:
            if xact[0] == company:
                xact[1] -= num_shares
                if xact[1] == 0:
                    idx = self.stocks.index(xact)
                    break
        if idx != -1:
            del self.stocks[idx]

    def cost_basis(self):
        """Calculate the cost basis for the stocks acquired"""
        basis = 0.0
        for company, shares, unit_price in self.stocks:
            basis += shares * unit_price
        return basis

    def print_portfolio(self):
        print('Company,', 'Number Shares,', 'Share Price')
        for company, num_shares, unit_price in self.stocks:
            print(company, num_shares, unit_price)

