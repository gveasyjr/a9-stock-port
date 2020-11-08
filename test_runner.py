#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Test runner """

import unittest
from tests.test_buys import TestBuyStock
from tests.test_sells import TestSellStock

suite1 = unittest.TestLoader().loadTestsFromTestCase(TestBuyStock)
suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSellStock)
suite = unittest.TestSuite( [suite1, suite2] )
unittest.TextTestRunner(verbosity = 2).run(suite)

