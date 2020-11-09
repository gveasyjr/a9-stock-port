#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for buy methods in `stock_port` package."""


import unittest

from stock_port.stock_port import Stocks


class TestBuyStock(unittest.TestCase):

    """Tests fixtues for `stock_port` package."""
    def setUp(self):
        self.stks = Stocks()

    def tearDown(self):
        """Tear down test fixtures, if any."""

    """ Sunny day tests -- no errors in input params """
    def test_buy_one_company(self):
        self.stks.buy('HON', 100, 132.0)
        self.assertEqual(self.stks.cost_basis(), 13200.0)

    def test_buy_two_companies(self):
        self.stks.buy('HON', 100, 132.0)
        self.stks.buy('MSFT', 50, 200.0)
        self.assertEqual(self.stks.cost_basis(), 23200)

    def test_buy_one_company_twice(self):
        self.stks.buy('AAPL',100, 102.0)
        self.stks.buy('MSFT', 50, 200.0)
        self.stks.buy('AAPL', 100, 102.0)
        self.assertEqual(self.stks.cost_basis(), 30400.)

    """ rainy day tests -- app errors caused via unexpected param values """
    def test_negative_shares(self):
        self.assertEqual(self.stks.buy('GOOG', -1, 1000), -1)

