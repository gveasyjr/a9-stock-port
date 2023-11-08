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

    @given(company=st.text('ABCDELGHIJKLMNOPQRSTUVWXYZ', min_size=3, max_size=5),
           shares=st.integers(min_value=-1000, max_value=-1),  
           prices=st.floats(min_value=1, max_value=1000))
    @settings(verbosity=Verbosity.verbose, max_examples=5)
    def test_sell_one_company_with_negative_shares(self, company, shares, prices):
        with self.assertRaises(ValueError):
            self.stks.buy(company, shares, prices)

    @given(company=st.text('ABCDELGHIJKLMNOPQRSTUVWXYZ', min_size=3, max_size=5),
           shares=st.integers(min_value=1, max_value=1000000),  # Very large values for shares
           prices=st.floats(min_value=1, max_value=1000000))  # Very large values for prices
    @settings(max_examples=5, verbosity=Verbosity.verbose)
    def test_sell_one_company_with_large_values(self, company, shares, prices):
        # Attempt to buy and sell stocks with very large values
        self.stks = Stocks()
        self.stks.buy(company, shares, prices)
        self.stks.sell(company, shares)  # Attempt to sell all shares
        
        # The cost basis should be 0, as all shares have been sold
        self.assertEqual(self.stks.cost_basis(), 0)
