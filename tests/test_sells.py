#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `stock_port` package."""


import unittest
from hypothesis import given, strategies as st, settings, Verbosity
from stock_port.stock_port import Stocks

company_names = st.text(min_size=1)
num_shares = st.integers(min_value=1, max_value=1000)
unit_prices = st.floats(min_value=0, max_value=1000)
shares2 = st.integers(min_value=1, max_value=1000)


class TestSellStock(unittest.TestCase):

    """ Unit test fixtures -- setup portfolio"""
    def setUp(self):
        self.stks = Stocks()

    def tearDown(self):
        pass

    """ Sunny day tests -- all clean params"""
    # @given(strat)
    # @settings(verbosity=Verbosity.verbose, max_examples=5)


    @settings(max_examples=5)
    def test_empty_portfolio(self):
        self.assertEqual(self.stks.cost_basis(), 0.0)

    @given(company=st.text('ABCDELGHIJKLMNOPQRSTUVWXYZ', min_size=3, max_size=5), shares=st.integers(min_value=1, max_value=1000), prices= st.floats(min_value=1, max_value=1000))
    @settings(verbosity=Verbosity.verbose,max_examples=5)
    def test_sell_one_company_full(self, company, shares, prices):
        self.stks.buy(company, shares, prices)
        self.stks.sell(company, shares)
        self.assertEqual(self.stks.cost_basis(), 0.0)



    @given(company=st.text('ABCDELGHIJKLMNOPQRSTUVWXYZ', min_size=3, max_size=5), shares=st.integers(min_value=1, max_value=1000), prices=st.floats(min_value=1, max_value=1000))
    @settings(max_examples=5)
    def test_sell_one_company_partial(self, company, shares, prices):
        self.stks = Stocks()
        self.stks.buy(company, shares, prices)
        shares_sell = shares // 2
        self.stks.sell(company, shares_sell)
        remaining_shares = shares - shares_sell
        new_value = remaining_shares * prices
        self.assertEqual(self.stks.cost_basis(), new_value)


    @given(company=st.text('ABCDELGHIJKLMNOPQRSTUVWXYZ', min_size=3, max_size=5), shares=st.integers(min_value=1, max_value=1000), prices=st.floats(min_value=1, max_value=1000),
           less_shares=st.integers(min_value=1, max_value=10))
    @settings(max_examples=5)
    def test_sell_one_company_small(self, company, shares, prices, less_shares):
        self.stks = Stocks()
        self.stks.buy(company, shares, prices)
        remaining_shares = shares - less_shares
        self.stks.sell(company, less_shares)
        new_value = remaining_shares * prices
        self.assertEqual(self.stks.cost_basis(), new_value)

    # def test_buy_and_sell_multiple_companies(self, company1, shares1, prices1, company2, shares2, prices2):
    #     self.stks = Stocks()
    #     self.stks.buy(company1, shares1, prices1)
    #     self.stks.buy(company2, shares2, prices2)
    #     total_value = (shares1 * prices1) + (shares2 * prices2)
        
    #     # Selling half of the shares of each company
    #     sold_shares1 = shares1 // 2
    #     sold_shares2 = shares2 // 2
    #     self.stks.sell(company1, sold_shares1)
    #     self.stks.sell(company2, sold_shares2)
        
    #     remaining_value = ((shares1 - sold_shares1) * prices1) + ((shares2 - sold_shares2) * prices2)
    #     self.assertEqual(self.stks.cost_basis(), remaining_value)


