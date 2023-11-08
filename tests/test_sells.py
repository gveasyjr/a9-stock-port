#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `stock_port` package."""


import unittest
from hypothesis import given, strategies as st, settings, Verbosity
from stock_port.stock_port import Stocks

company_names = st.text(min_size=1)
num_shares = st.integers(min_value=1, max_value=1000)
unit_prices = st.floats(min_value=0, max_value=1000)
custom_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'


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

    @given(company=st.text(min_size=3, max_size=5), shares=st.integers(min_value=1, max_value=1000), prices= st.floats(min_value=0, max_value=1000))
    @settings(verbosity=Verbosity.verbose,max_examples=5)
    def test_sell_one_company_full(self, company, shares, prices):
        self.stks.buy(company, shares, prices)
        self.stks.sell(company, shares)
        self.assertEqual(self.stks.cost_basis(), 0.0)


    @given(company=st.text(min_size=3, max_size=5), shares=st.integers(min_value=1, max_value=1000), prices= st.floats(min_value=0, max_value=1000))
    @settings(max_examples=5)
    def test_sell_one_company_partial(self, company, shares, prices):
        self.stks = Stocks()
        self.stks.buy(company, shares, prices)
        shares_sell = shares // 2
        self.stks.sell(company, shares_sell)
        if(prices < 0):
            self.assertEqual(self.stks.cost_basis(), 0.0)
        new_value = (shares * - shares_sell) - (prices)
        self.assertEqual(self.stks.cost_basis(), new_value)


 
    # def test_sell_2nd_company_bought(self):
    #     self.stks.buy('AAPL', 10, 200)
    #     self.stks.buy('MSFT', 50, 100)
    #     self.stks.sell('MSFT', 50)
    #     self.assertEqual(self.stks.cost_basis(), 2000)


