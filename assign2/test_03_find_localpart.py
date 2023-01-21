import unittest

from solution import FileNode
from sample_data import makeData

class TestFind(unittest.TestCase):
    def test_simple_root_root(self):
        root, nodes = makeData(1)
        result = root.find_by_localpart("root")
        expected = [nodes["root"]]
        self.assertEqual(sorted(result, key=id), sorted(expected, key=id))

    def test_simple_root_whee(self):
        root, nodes = makeData(1)
        result = root.find_by_localpart("whee")
        expected = [nodes["whee"]]
        self.assertEqual(sorted(result, key=id), sorted(expected, key=id))


    def test_small_alpha_gamma(self):
        root, nodes = makeData(2)
        result = root.find_by_localpart("gamma")
        expected = [nodes["gamma"]]
        self.assertEqual(sorted(result, key=id), sorted(expected, key=id))


    def test_small_alpha_omega(self):
        root, nodes = makeData(2)
        result = root.find_by_localpart("omega")
        expected = []
        self.assertEqual(sorted(result, key=id), sorted(expected, key=id))


    def test_medium_vimrc(self):
        root, nodes = makeData(3)
        result = root.find_by_localpart(".vimrc")
        expected = [nodes['.vimrc1'], nodes['.vimrc2'], nodes['.vimrc3']]
        self.assertEqual(sorted(result, key=id), sorted(expected, key=id))

    def test_medium_other_vimrc(self):
        root, nodes = makeData(3)
        result = root.find_by_localpart("vimrc")
        expected = [nodes['vimrc']]
        self.assertEqual(sorted(result, key=id), sorted(expected, key=id))

    def test_medium_looking_wrong_place(self):
        # cannot find pg_hba.conf in the /home directory
        root, nodes = makeData(3)
        result = nodes['home'].find_by_localpart("pg_hba.conf")
        expected = []
        self.assertEqual(sorted(result, key=id), sorted(expected, key=id))





