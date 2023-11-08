# -*- coding: utf-8 -*-

class Stocks(object):

    def __init__(self):
        # stocks is a list of lists where each element
        # is a list of company name, num shares purchased
        # and the price per share
        self.stocks = []
        self.cash_on_hand = 15000

    def buy(self, company, num_shares, unit_price):
        if company != company.upper():
            company = company.upper()
        if num_shares < 0:
            raise ValueError('Number shares purchased less than 0')
        self.stocks.append([company, num_shares, unit_price])

    def sell(self, company, num_shares):
        if num_shares < 0:
            return 0  
        for xact in self.stocks:
            if xact[0] == company:
                num_to_sell = min(num_shares, xact[1]) 
                xact[1] -= num_to_sell
                if xact[1] == 0:
                    self.stocks.remove(xact)
                num_shares -= num_to_sell
                if num_shares == 0:
                    break

    def cost_basis(self):
        """Calculate the cost basis for all stocks acquired in the portfolio"""
        basis = 0.0
        for company, shares, unit_price in self.stocks:
            basis += shares * unit_price
        return basis

    def cost_basis_company(self, target_company):
        """Calculate the cost basis for stocks in one specific company"""
        basis = 0.0
        for company, shares, unit_price in self.stocks:
            if company == target_company:
                basis += shares * unit_price
        return basis

    def last_xact_cost_basis(self):
        return self.stocks[-1][1] * self.stocks[-1][2]

    def print_portfolio(self):
        print('Company,', 'Number Shares,', 'Share Price')
        for company, num_shares, unit_price in self.stocks:
            print(company, num_shares, unit_price)

