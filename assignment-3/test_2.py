import math
from math import inf
import unittest

from digraph import DiGraph
from sample_data import makeData


class TestQ2(unittest.TestCase):
    def _helper(self, sample_which, src, expected):
        g = makeData(sample_which)
        ans = g.question_2(src)
        self.assertEqual(ans, expected, f"makeData({sample_which}).question_2({src}) should produce {expected}, but did not")


    def test0_1(self):
        self._helper(0, 0, {0: 0, 2: 27, 1: 52, 3: 16, 4: 24})

    def test0_2(self):
        self._helper(0, 1, {0: 26, 2: 15, 1: 0, 3: 3, 4: 23})

    def test0_3(self):
        self._helper(0, 2, {0: 11, 2: 0, 1: 25, 3: 27, 4: 9})
        
    def test0_4(self):
        self._helper(0, 4, {0: 5, 2: 3, 1: 28, 3: 21, 4: 0})


    def test1_0(self):
        self._helper(2, 3, {0: 38, 2: 23, 1: 23, 3: 0, 4: 13, 5: 29, 6: 25, 7: 19, 8: 27, 9: 15, 10: 29, 11: 9})

    def test1_4(self):
        self._helper(1, 4, {0: 21, 2: 19, 1: inf, 3: inf, 4: 0, 5: inf, 6: 46, 7: inf})

    def test1_5(self):
        self._helper(1, 5, {0: 2, 2: 17, 1: 23, 3: 40, 4: 21, 5: 0, 6: 27, 7: 23})
        
    def test1_6(self):
        self._helper(1, 6, {0: 17, 2: 14, 1: inf, 3: inf, 4: 8, 5: inf, 6: 0, 7: inf})

    def test1_7(self):
        self._helper(1, 7, {0: inf, 2: inf, 1: inf, 3: inf, 4: inf, 5: inf, 6: inf, 7: 0})


    def test2_1(self):
        self._helper(2, 1, {0: 21, 1: 0, 2: 19, 3: 3, 4: 16, 5: 27, 6: 24, 7: 22, 8: 29, 9: 18, 10: 28, 11: 4})

    def test2_2(self):
        self._helper(2, 2, {0: 15, 1: 22, 2: 0, 3: 25, 4: 30, 5: 12, 6: 5, 7: 17, 8: 10, 9: 32, 10: 22, 11: 17})

    def test2_7(self):
        self._helper(2, 7, {0: 24, 1: 22, 2: 9, 3: 25, 4: 38, 5: 21, 6: 6, 7: 0, 8: 19, 9: 40, 10: 31, 11: 26})
        
    def test2_10(self):
        self._helper(2, 10, {0: 23, 1: 18, 2: 23, 3: 21, 4: 8, 5: 1, 6: 20, 7: 14, 8: 20, 9: 10, 10: 0, 11: 22})

    def test2_11(self):
        self._helper(2, 11, {0: 30, 1: 37, 2: 15, 3: 15, 4: 28, 5: 27, 6: 20, 7: 32, 8: 25, 9: 30, 10: 37, 11: 0})

