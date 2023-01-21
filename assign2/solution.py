# Pham Minh Tan A01215507

class FileNode:
    def __init__(self, name, parent=None, data=""):
        self.name = name
        self.parent = parent
        self.children = []
        self.data = data
        if parent:
            parent.children.append(self)

    def __str__(self):
        # I recommend ignoring this method
        bytestring = f"  ({len(self.data)} bytes)" if len(self.data) else ""
        childrenstring = (
            f"  (contains {len(self.children)} files)" if len(
                self.children) else ""
        )

        return f"{self.name}{bytestring}{childrenstring}"

    def __repr__(self):
        # I recommend ignoring this method
        return f"<solution.FileNode object at {id(self)} (name='{self.name}')>"

    def squashNested(self, val):
        # Return val because there is no list to work on
        if type(val) is not list:
            return [val]
        # Return final value when val becomes a layer deep
        if val == []:
            return val
        # Perform recursion when found element in val is a list
        if isinstance(val[0], list):
            return self.squashNested(val[0]) + self.squashNested(val[1:])
        # Perform recursion on next element in the nested list val
        return val[:1] + self.squashNested(val[1:])

    # Q1

    def fullpath(self):

        output = []
        if self.parent:
            return self.squashNested([self.parent.fullpath(), self.name])
        return [self.name]

    # Q2
    def count_normal_files(self):
        count = 0
        if self.children:
            for child in self.children:
                count += child.count_normal_files()
        else:
            count += 1
        return count

    # Q3
    def find_by_localpart(self, target_name):
        nodes_founded = []
        if target_name[0] == '.':
            if target_name in self.name:
                return self
        else:
            if target_name == self.name:
                return [self]
        if self.children:
            for child in self.children:
                nodes_founded.append(child.find_by_localpart(target_name))
        return self.squashNested(nodes_founded)

    def format_std(self, tab_in, sort):
        def partition(arr, lo, hi):
            pivot = arr[hi]
            i = lo - 1
            for j in range(lo, hi):
                if arr[j].name <= pivot.name:
                    i = i + 1
                    (arr[i], arr[j]) = (arr[j], arr[i])
            (arr[i + 1], arr[hi]) = (arr[hi], arr[i + 1])

            return i + 1

        def qSort(arr, lo, hi):
            if lo < hi:
                pi = partition(arr, lo, hi)
                qSort(arr, lo, pi - 1)
                qSort(arr, pi + 1, hi)
        tab = '    '
        node = [tab*tab_in+self.name]
        if self.children:
            if sort:
                qSort(self.children, 0, len(self.children)-1)
            for child in self.children:
                node.append(child.format_std(tab_in+1, sort))
        return node

    # Q4
    def format_tree_string(self, sort=False):
        return self.squashNested(self.format_std(0, sort))

    def find_node(self, target):
        if self.name == target:
            return self
        if self.parent:
            return self.parent.find_node(target)
        if self.children:
            return self.children.find_node(target)
        return None

    # Q5
    def closest_common_ancestor(self, other_node):
        def partition(arr, lo, hi):
            pivot = arr[hi]
            i = lo - 1
            for j in range(lo, hi):
                if arr[j] <= pivot:
                    i = i + 1
                    (arr[i], arr[j]) = (arr[j], arr[i])
            (arr[i + 1], arr[hi]) = (arr[hi], arr[i + 1])

            return i + 1

        def qSort(arr, lo, hi):
            if lo < hi:
                pi = partition(arr, lo, hi)
                qSort(arr, lo, pi - 1)
                qSort(arr, pi + 1, hi)

        def performBinarySearch(haystack, needle, lo, hi):
            # Condition to perform
            if hi >= lo:
                # Main index for finding needle
                centre = lo + (hi - lo)//2

                # When find at mid, return index of the found element
                if haystack[centre] == needle:
                    return centre

                # Recursively search the left half
                elif haystack[centre] > needle:
                    return performBinarySearch(haystack, needle, lo, centre-1)

                # Recursively search the right half
                else:
                    return performBinarySearch(haystack, needle, centre + 1, hi)
            # Return None when lo exceeds hi but still cannot find value
            else:
                return None
        if self.name == other_node.name and self.parent == other_node.parent:
            return self
        node_sorted = self.fullpath()
        node_sorted.pop()
        qSort(node_sorted, 0, len(node_sorted)-1)
        other_node_sorted = other_node.fullpath()
        other_node_sorted.pop()
        qSort(other_node_sorted, 0, len(other_node_sorted)-1)

        if len(self.fullpath()) < len(other_node.fullpath()):
            for item in reversed(self.fullpath()):
                if item != '/':
                    if performBinarySearch(other_node_sorted, item, 0, len(other_node_sorted)-1) != None:
                        return self.find_node(item)
                # return self.fullpath(), ' and ', other_node.fullpath()
        else:
            for item in reversed(other_node.fullpath()):
                if item != '/':
                    if performBinarySearch(node_sorted, item, 0, len(node_sorted)-1) != None:
                        return other_node.find_node(item)
        return None

        # return other_node_sorted
        # return node_sorted
        # return other_node.fullpath()
