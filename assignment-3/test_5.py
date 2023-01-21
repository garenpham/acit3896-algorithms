import math
from math import inf
import unittest

from digraph import DiGraph
from sample_data import makeData


class TestQ5(unittest.TestCase):
    def _helper(self, sample_which, src, expected):
        g = makeData(sample_which)
        ans = g.question_5(
            src,
        )
        self.assertEqual(
            sorted(ans),
            sorted(expected),
            f"makeData({sample_which}).question_5({src}) on sample {sample_which} should produce {expected}, but did not",
        )

    def test0_0(self):
        self._helper(0, 0, [0, 1, 2, 3, 4])

    def test0_2(self):
        self._helper(0, 2, [0, 1, 2, 3, 4])

    def test1_0(self):
        self._helper(1, 0, [0, 4, 6])

    def test1_1(self):
        self._helper(1, 1, [5, 1, 3])

    def test1_2(self):
        self._helper(1, 2, [2])

    def test1_3(self):
        self._helper(1, 3, [1, 5, 3])

    def test1_4(self):
        self._helper(1, 4, [0, 4, 6])

    def test1_5(self):
        self._helper(1, 5, [1, 3, 5])

    def test1_6(self):
        self._helper(1, 6, [0, 4, 6])

    def test1_7(self):
        self._helper(1, 7, [7])

    def test2_0(self):
        self._helper(2, 0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test2_2(self):
        self._helper(2, 2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
