import math
import unittest

from digraph import DiGraph
from sample_data import makeData


class TestQ1(unittest.TestCase):
    def _helper(self, sample_which, src, dest, expected):
        g = makeData(sample_which)
        ans = g.question_1(src, dest)
        path = ans["path"]
        self.assertEqual(path, expected, f"makeData({sample_which}).question_1({src}, {dest}) should produce a path of {expected}, but did not")


    def test0_1(self):
        self._helper(0, 0, 1, [0, 4, 2, 1])

    def test0_2(self):
        self._helper(0, 1, 0, [1, 3, 2, 0])

    def test0_3(self):
        self._helper(0, 4, 1, [4, 2, 1])
        
    def test0_4(self):
        self._helper(0, 4, 3, [4, 0, 3])


    def test1_1(self):
        self._helper(2, 4, 4, [4])

    def test1_2(self):
        self._helper(1, 4, 5, None)

    def test1_3(self):
        self._helper(1, 4, 6, [4, 0, 6])
        
    def test1_4(self):
        self._helper(1, 4, 7, None)

    def test1_5(self):
        self._helper(1, 3, 6, [3, 5, 0, 6])


    def test2_1(self):
        self._helper(2, 10, 11, [10, 4, 9, 1, 11])

    def test2_2(self):
        self._helper(2, 7, 8, [7, 2, 8])

    def test2_3(self):
        self._helper(2, 7, 9, [7, 1, 3, 4, 9])
        
    def test2_4(self):
        self._helper(2, 1, 6, [1, 11, 2, 6])

    def test2_5(self):
        self._helper(2, 1, 7, [1, 3, 4, 9, 7])

