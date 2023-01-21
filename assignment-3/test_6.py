import math
from math import inf
import unittest

from digraph import DiGraph
from sample_data import makeData


class TestQ6(unittest.TestCase):
    def _helper(self, sample_which, expected):
        g = makeData(sample_which)
        ans = g.question_6()
        self.assertEqual(
            sorted(sorted(x) for x in ans),
            sorted(sorted(x) for x in expected),
            f"makeData({sample_which}).question_6() on sample {sample_which} should produce {expected}, but did not",
        )

    def test0(self):
        self._helper(0, [[0, 1, 2, 3, 4]])

    def test1(self):
        self._helper(1, [[0, 6, 4], [2], [7], [1, 3, 5]])

    def test2(self):
        self._helper(2, [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]])
