import unittest

from solution import FileNode
from sample_data import makeData


class TestCounting(unittest.TestCase):
    def test_simple_root(self):
        # 2 normal files under the root (the other 2 are directories)
        root, nodes = makeData(1)
        self.assertEqual(nodes["root"].count_normal_files(), 2)

    def test_simple_another(self):
        # only 1 normal file under another
        root, nodes = makeData(1)
        self.assertEqual(nodes["another"].count_normal_files(), 1)

    def test_small_alpha(self):
        # gamma, epsilon, foo, bar, glurp, blort
        root, nodes = makeData(2)
        self.assertEqual(nodes["alpha"].count_normal_files(), 6)

    def test_small_gamma(self):
        # count yourself, but have no children
        root, nodes = makeData(2)
        self.assertEqual(nodes["gamma"].count_normal_files(), 1)

    def test_medium_smeechward(self):
        root, nodes = makeData(3)
        self.assertEqual(nodes["smeechward"].count_normal_files(), 8)

    def test_medium_jholman(self):
        root, nodes = makeData(3)
        self.assertEqual(nodes["jholman"].count_normal_files(), 7)



