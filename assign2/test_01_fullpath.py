import unittest

from solution import FileNode
from sample_data import makeData


class TestFullPath(unittest.TestCase):
    def test_simple_root(self):
        root, nodes = makeData(1)
        self.assertEqual(nodes["root"].fullpath(), ["root"])

    def test_simple_another(self):
        root, nodes = makeData(1)
        self.assertEqual(nodes["another"].fullpath(), ["root", "another"])

    def test_small_glurp(self):
        root, nodes = makeData(2)
        self.assertEqual(nodes["glurp"].fullpath(), ["alpha", "baz", "glurp"])

    def test_small_gamma(self):
        root, nodes = makeData(2)
        self.assertEqual(nodes["gamma"].fullpath(), ["alpha", "beta", "gamma"])

    def test_small_epsilon(self):
        root, nodes = makeData(2)
        self.assertEqual(
            nodes["epsilon"].fullpath(), ["alpha", "beta", "delta", "epsilon"]
        )

    def test_medium_wk1(self):
        root, nodes = makeData(3)
        self.assertEqual(
            nodes["wk1.ipy"].fullpath(), ["/", "home", "tholane", "zybooks", "wk1.ipy"]
        )

    def test_medium_scooter(self):
        root, nodes = makeData(3)
        self.assertEqual(
            nodes["stupid_scooter_project"].fullpath(),
            ["/", "home", "smeechward", "stupid_scooter_project"],
        )

    def test_medium_pg_hba(self):
        root, nodes = makeData(3)
        self.assertEqual(
            nodes["pg_hba.conf"].fullpath(),
            ["/", "etc", "postgres", "12", "main", "pg_hba.conf"],
        )
