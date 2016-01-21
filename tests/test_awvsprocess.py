# -*- coding: utf-8 -*-

import unittest
from awvspy.awvsprocess import AWVSProcess

class CaseTest(unittest.TestCase):
    def setUp(self):
        self.awvsprocess = AWVSProcess()

    def tearDown(self):
        pass

    def test_something(self):
        self.assertEqual(True, True)
