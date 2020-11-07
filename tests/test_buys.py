#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for buy methods in `stock_port` package."""


import unittest

from stock_port.stock_port import Stocks


class TestBuyStock(unittest.TestCase):
    """Tests for `stock_port` package."""

    def setUp(self):
       self.stks = Stocks()

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_buy_something(self):
        """Test buy something."""
