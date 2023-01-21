import math
import unittest

from math import inf

from digraph import DiGraph
from sample_data import makeData


class TestQ3(unittest.TestCase):
    def _helper(self, sample_which, src, dest, expected):
        g = makeData(sample_which)
        ans = g.question_3(src, dest)
        self.assertEqual(ans, expected, f"makeData({sample_which}).question_3({src}, {dest}) should produce a cost of {expected}, but did not")


    def test0_1(self):
        self._helper(0, 0, 1, 59)

    def test0_2(self):
        self._helper(0, 1, 0, 32)

    def test0_3(self):
        self._helper(0, 4, 1, 32)
        
    def test0_4(self):
        self._helper(0, 4, 3, 24)


    def test1_1(self):
        self._helper(2, 4, 4, 0)

    def test1_2(self):
        self._helper(1, 4, 5, inf)

    def test1_3(self):
        self._helper(1, 4, 6, 51)
        
    def test1_4(self):
        self._helper(1, 4, 7, inf)

    def test1_5(self):
        self._helper(1, 3, 6, 40)


    def test2_1(self):
        self._helper(2, 10, 11, 30)

    def test2_2(self):
        self._helper(2, 7, 8, 24)

    def test2_3(self):
        self._helper(2, 7, 9, 48)
        
    def test2_4(self):
        self._helper(2, 1, 6, 29)

    def test2_5(self):
        self._helper(2, 1, 7, 29)

