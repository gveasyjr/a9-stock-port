#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `stock_port` package."""


import unittest

from stock_port.stock_port import Stocks


class TestSellStock(unittest.TestCase):

    def setUp(self):
        self.stks = Stocks()

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_sell0_something(self):
        """Test something."""
