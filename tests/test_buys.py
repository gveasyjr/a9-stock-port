#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for buy methods in `stock_port` package."""


import unittest
from hypothesis import given, strategies as st, settings, Verbosity
from stock_port.stock_port import Stocks


class TestBuyStock(unittest.TestCase):

    """Tests fixtues for `stock_port` package."""
    def setUp(self):
        self.stks = Stocks()

    def tearDown(self):
        pass

    """ Sunny day tests -- no errors in input params """
    @settings(verbosity=Verbosity.verbose, max_examples=5)
    @given(num_shares=st.integers(min_value=1))
    def test_buy_one_company(self, num_shares):
        old_basis = self.stks.cost_basis()
        self.stks.buy('HON', num_shares, 132.0)
        self.assertEqual(self.stks.cost_basis(), num_shares * 132.0 + old_basis)


    @given(company1=st.text(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', min_size=3, max_size=5),
    num_shares1=st.integers(min_value=1), price_per_share1=st.floats(min_value=1, max_value=1000))
    @settings(verbosity=Verbosity.verbose, max_examples=5)
    def test_buy_one(self, company1, num_shares1, price_per_share1):
        stks = Stocks() 
        stks.buy(company1, num_shares1, price_per_share1) 
        expected_basis_company1 = num_shares1 * price_per_share1
        actual_basis_company1 = stks.cost_basis_company(company1)
        self.assertEqual(actual_basis_company1, expected_basis_company1)


    @given(company1=st.text(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', min_size=3, max_size=5), price_per_share1=st.floats(min_value=1, max_value=1000))
    @settings(verbosity=Verbosity.verbose, max_examples=5)
    def test_buy_0(self, company1, price_per_share1):
        stks = Stocks() 
        num_shares1 = 0.0
        stks.buy(company1, num_shares1, price_per_share1)
        self.assertEqual(self.stks.cost_basis(), 0.0)

    # def test_buy_one_company_twice(self):
    #     self.stks.buy('AAPL',100, 102.0)
    #     self.stks.buy('MSFT', 50, 200.0)
    #     self.stks.buy('AAPL', 100, 102.0)
    #     self.assertEqual(self.stks.cost_basis(), 30400.)

    # """ rainy day tests -- app errors caused via unexpected param values """
    # def test_negative_shares(self):
    #     self.assertRaises(ValueError, self.stks.buy, *('GOOG', -1, 1000))

    # def test_fractional_shares(self):
    #     # signature for assertRaises(TypeError, test_function, args) 
    #     self.assertRaises(ValueError, self.stks.buy, 'GOOG', 5.5, 1000)