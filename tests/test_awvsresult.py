# -*- coding: utf-8 -*-

import unittest
from awvspy.awvsresult import AWVSResult
from sqlalchemy import create_engine

class AWVSResultTest(unittest.TestCase):

    def setUp(self):
        self.awvsresult = AWVSResult()


    def tearDown(self):
        pass

    def test_something(self):
        self.assertEqual(True, True)
