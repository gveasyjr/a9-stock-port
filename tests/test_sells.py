#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `stock_port` package."""


import unittest

from stock_port.stock_port import Stocks


class TestSellStock(unittest.TestCase):

    """ Unit test fixtures -- setup portfolio"""
    def setUp(self):
        self.stks = Stocks()

    def tearDown(self):
        pass

    """ Sunny day tests -- all clean params"""
    def test_empty_portfolio(self):
        self.assertEqual(self.stks.cost_basis(), 0.0)

    def test_sell_one_company_full(self):
        self.stks.buy('HON', 100, 132.0)
        self.stks.sell('HON', 100)
        self.assertEqual(self.stks.cost_basis(), 0.0)

    def test_sell_one_company_partial(self):
        self.stks.buy('HON', 100, 132.0)
        self.stks.sell('HON', 50)
        self.assertEqual(self.stks.cost_basis(), 6600.0)
 
    def test_sell_2nd_company_bought(self):
        self.stks.buy('AAPL', 10, 200)
        self.stks.buy('MSFT', 50, 100)
        self.stks.sell('MSFT', 50)
        self.assertEqual(self.stks.cost_basis(), 2000)


