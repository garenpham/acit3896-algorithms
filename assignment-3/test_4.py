import math
from math import inf
import unittest

from digraph import DiGraph
from sample_data import makeData


class TestQ4(unittest.TestCase):
    def _helper(self, sample_which, expected):
        g = makeData(sample_which)
        ans = g.question_4()
        self.assertEqual(
            ans,
            expected,
            f"makeData({sample_which}).question_4() on sample {sample_which} should produce {expected}, but did not",
        )

    def test0(self):
        self._helper(
            0,
            [
                [None, None, None, 16, 24],
                [None, None, None, 3, None],
                [11, 25, None, None, 9],
                [None, None, 12, None, 20],
                [5, None, 3, None, None],
            ],
        )

    def test1(self):
        self._helper(
            1,
            [
                [None, None, 17, None, 19, None, 25, None],
                [None, None, None, 17, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, 6, None, None],
                [21, None, 19, None, None, None, None, None],
                [2, 23, 17, None, None, None, None, 23],
                [17, None, 14, None, 8, None, None, None],
                [None, None, None, None, None, None, None, None],
            ],
        )

    def test2(self):
        self._helper(
            2,
            [
                [None, None, None, None, None, 6, None, 11, None, None, 7, None],
                [21, None, None, 3, None, None, None, None, None, None, None, 4],
                [15, 22, None, None, None, None, 5, None, 10, None, 23, None],
                [None, None, 23, None, 13, None, 25, None, None, None, None, 9],
                [None, None, None, None, None, None, 20, None, None, 2, None, None],
                [22, None, None, None, None, None, None, None, 19, None, None, None],
                [22, None, 9, None, None, None, None, 12, 20, None, None, None],
                [None, 22, 9, None, None, None, 6, None, None, None, None, None],
                [None, None, None, None, 20, 2, None, 7, None, None, None, 7],
                [None, 8, None, None, None, None, None, 4, 12, None, 14, None],
                [None, None, 24, None, 8, 1, 24, None, None, None, None, None],
                [None, None, 15, 15, None, None, None, None, None, None, None, None],
            ],
        )
