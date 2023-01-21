import unittest

from solution import FileNode
from sample_data import makeData


class TestFormatter(unittest.TestCase):
    def test_simple_unsorted(self):
        # in the sample data, "one" was added before "another"
        root, nodes = makeData(1)
        result = root.format_tree_string(sort=False)
        expected = ["root", "    one", "    another", "        whee"]
        self.assertEqual(result, expected)

    def test_simple_sorted(self):
        # when sorted, "another" comes before "one"
        root, nodes = makeData(1)
        result = root.format_tree_string(sort=True)
        expected = ["root", "    another", "        whee", "    one"]
        self.assertEqual(result, expected)

    def test_small_unsorted(self):
        # in the sample data, "one" was added before "another"
        root, nodes = makeData(2)
        result = root.format_tree_string(sort=False)
        expected = [
            "alpha",
            "    beta",
            "        gamma",
            "        delta",
            "            epsilon",
            "    foo",
            "    bar",
            "    baz",
            "        glurp",
            "        blort",
        ]
        self.assertEqual(result, expected)

    def test_small_sorted(self):
        # when sorted, "another" comes before "one"
        root, nodes = makeData(2)
        result = root.format_tree_string(sort=True)
        expected = [
            "alpha",
            "    bar",
            "    baz",
            "        blort",
            "        glurp",
            "    beta",
            "        delta",
            "            epsilon",
            "        gamma",
            "    foo",
        ]
        self.assertEqual(result, expected)

    def test_small_partial_unsorted(self):
        # in the sample data, "one" was added before "another"
        root, nodes = makeData(2)
        result = nodes['beta'].format_tree_string(sort=False)
        expected = [
            "beta",
            "    gamma",
            "    delta",
            "        epsilon",
        ]
        self.assertEqual(result, expected)

    def test_small_partial_sorted(self):
        # when sorted, "another" comes before "one"
        root, nodes = makeData(2)
        result = nodes['beta'].format_tree_string(sort=True)
        expected = [
            "beta",
            "    delta",
            "        epsilon",
            "    gamma",
        ]
        self.assertEqual(result, expected)

    def test_large_unsorted(self):
        # in the sample data, "one" was added before "another"
        root, nodes = makeData(3)
        result = root.format_tree_string(sort=False)
        expected = '''
/
    etc
        vim
            vimrc
            vimrc.tiny
        postgres
            12
                main
                    pg_hba.conf
    home
        jholman
            .bashrc
            .vimrc
            algorithms
                cruelty.md
                hilarious_misery.md
                pain.md
                suffering.md
            fswd
                arbeit_macht_frei.md
        tholane
            zybooks
                wk1.ipy
                wk2.ipy
                wk3.ipy
            .bashrc
            .vimrc
            grading
                auto_test_harness.py
                why_do_they_do_this.py
        smeechward
            .bashrc
            .vimrc
            stupid_scooter_project
                batteries.md
                wiring.md
            stupid_advent_project
                razorblades.md
                servos.md
            youtube
                latest_video.mp4
                profile.jpg
'''.strip().split('\n')
        self.assertEqual(result, expected)

    def test_large_sorted(self):
        # when sorted, "another" comes before "one"
        root, nodes = makeData(3)
        result = root.format_tree_string(sort=True)
        expected = '''
/
    etc
        postgres
            12
                main
                    pg_hba.conf
        vim
            vimrc
            vimrc.tiny
    home
        jholman
            .bashrc
            .vimrc
            algorithms
                cruelty.md
                hilarious_misery.md
                pain.md
                suffering.md
            fswd
                arbeit_macht_frei.md
        smeechward
            .bashrc
            .vimrc
            stupid_advent_project
                razorblades.md
                servos.md
            stupid_scooter_project
                batteries.md
                wiring.md
            youtube
                latest_video.mp4
                profile.jpg
        tholane
            .bashrc
            .vimrc
            grading
                auto_test_harness.py
                why_do_they_do_this.py
            zybooks
                wk1.ipy
                wk2.ipy
                wk3.ipy
'''.strip().split('\n')
        self.assertEqual(result, expected)

