import unittest
from solution import FileNode
from sample_data import makeData


class TestCca(unittest.TestCase):
    def test_simple_one_one(self):
        # a node is its own CCA
        root, nodes = makeData(1)
        result = nodes["one"].closest_common_ancestor(nodes["one"])
        expected = nodes["one"]
        self.assertEqual(result, expected)

    def test_simple_one_whee(self):
        root, nodes = makeData(1)
        result = nodes["one"].closest_common_ancestor(nodes["whee"])
        expected = root
        self.assertEqual(result, expected)

    def test_small_foo_bar(self):
        root, nodes = makeData(2)
        result = nodes["foo"].closest_common_ancestor(nodes["bar"])
        expected = root
        self.assertEqual(result, expected)

    def test_small_two_different_trees(self):
        # it shouldn't crash if even users give nodes from two totally unrealted trees
        root, nodes = makeData(2)
        result = nodes["foo"].closest_common_ancestor(FileNode("/", data=None))
        expected = None
        self.assertEqual(result, expected)

    def test_medium_zybooks(self):
        root, nodes = makeData(3)
        result = nodes["wk1.ipy"].closest_common_ancestor(nodes["wk3.ipy"])
        expected = nodes["zybooks"]
        self.assertEqual(result, expected)

    def test_medium_zybooks_mirrored(self):
        root, nodes = makeData(3)
        result = nodes["wk2.ipy"].closest_common_ancestor(nodes["wk1.ipy"])
        expected = nodes["zybooks"]
        self.assertEqual(result, expected)

    def test_medium_vimrcs(self):
        root, nodes = makeData(3)
        result = nodes[".vimrc2"].closest_common_ancestor(nodes[".vimrc3"])
        expected = nodes["home"]
        self.assertEqual(result, expected)
