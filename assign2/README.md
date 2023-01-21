

In this Assignment, you will solve problems related to tree traversal.  We'll work on a simplified version of a filesystem as our examples.

As you may know, a real filesystem is not actually a tree, because of features like links (symlinks, hardlinks, etc).  But in this assignment you can ignore that; our filesystems in this assignment will truly be trees (in the computer science sense).

Our filesystem will also be simplified in that our "files" will have much less detail to them than real filesystem files.


In all cases, you should write your solution as a method of the `FileNode` class.


## Our Filesystem


Each file in the filesystem is represented by an object from a class, like this:

```python
class FileNode:
    def __init__(self, name, parent=None, data=""):
        self.name = name
        self.parent = parent
        self.children = []
        self.data = data
        if parent:
            parent.children.append(self)
    def __str__(self):
        return f"{self.name} ({len(self.children)})"
```

So every file has a name, plus it might have children, and also it might have data.


## Dates

This assignment was published on November 2nd.

It is due at 11:59pm on the night of Wednesday November 9th, which is one week plus a bit.

## Grading

Each problem is worth 1 mark (that is, all 5 problems have equal weight).

Problems that flagrantly violate the asymptotic complexity goals may be worth zero marks.

In general, expect for each problem to be graded either correct (1 mark) or incorrect (0 marks).  Expect exceptions only if I think the error is my fault.

## Solo work

Please remember that this assignment is solo work.  Do not share your work with others, nor use the work of other students, nor get help from others.

However, you may use what you can find on the internet, assuming that it was published before I handed out this assignment.  Remember that if you use more than a line or two from a source you found on the internet, too much citation (in comments or in a separate CREDITS.md file) is safer and better than too little.

## Submitting your work

As you will already know by the time you read this, this assignment is being submitted via Github Classroom.



As in the last assignment:

* modify the `studentid.txt` file, doing ONE of the following two things:
    * a) put your A00 number in that file, so that I can associate your github work with your D2L account
        * note that this would mean sending PII to a US company, so instead you may do (b) if you prefer
    * b) write the word "EMAIL" in that file, and then send me an email at my BCIT email address
        * the email should have this in the subject line:   [D2L/GITHUB LINK]
        * the body of the email should contain your name as seen in D2L, your A00* student number, and your github account name
            * in the past I have received wrong github account names.  you can get it right!
    * the file should have exactly one line it in when you submit

As many times as necessary (before the deadline), `git commit` and `git push`.


## Explanations of the Questions


### Q1 : node.fullpath()

When called on a node object, like `node.fullpath()`, this returns an array of strings, representing the path from the root to the named file.  The first string in the list obviously should be the name of the root file (real filesystems don't have a name for the root file, but ours does), and the last string in the list should be the name of the node on which the method was called.

So, for example don't output `/etc/postgresql/12/main/pg_hba.conf`, do output `['/', 'etc', 'postgresql', '12', 'main', 'pg_hba.conf']` (assuming that the root node has been named "/", which it has in one of my examples but not in all of them).

This method should run in `O(x)`, where `x` is the size of the *output*.


### Q2 : node.count_normal_files()

This method should return a count of the number of non-directory files, in the subtree starting at the node on which the method is called.

What do we mean by "non-directory files"?  This filesystem doesn't really have filetypes, but we can argue that any file-node with children is a directory, and any other file-node is not, and we'll call these non-directories "normal" nodes.  So those files, the ones without children, are the ones we're counting.

Because this is a method on a node, it should only count things in the sub-tree starting at the node.  If called on a leaf node, it should count itself.

Hint: I *strongly* recommend that you start by implementing a DFS or BFS helper method.

This method should run in `O(n)`, where `n` is the size of the affected subtree.


### Q3 : node.find_by_localpart(target_name)

This method should return a list of nodes that have the name property matching the `target_name` parameter, in the subtree starting at the node on which the method is called.

1. Return a list of every matching node
2. The things in the list should be the nodes that match (not just filenames, or some other property)
3. Which ones should be in the answer list?  Any file whose `.name` property matches `target_name`
4. Only return file-nodes in the sub-tree starting at the node.  If appropriate (i.e. its name matches), it should include itself in the list of found files.
5. *Any order* of files in the returned array is fine
6. Of course, because it returns "all the matches", if there are *no* matches, that means return an empty array.

Hint: As with Q2, I recommend a BFS or DFS helper method.  Can you reuse that DFS-or-BFS helper code from Q2?

This method should run in `O(n)`, where `n` is the size of the affected subtree.


### Q4 : node.format_tree_string(sort=False)

This is basically a pretty-printer for the whole (sub-) tree (maybe sorted).

Your function should return a list of strings, such that if I printed them one after another, I'd get a nice print-out of the nested directory structure, like this:

```
alpha
    beta
        gamma
        delta
            epsilon
    foo
    bar
    baz
        glurp
        blort
```

Note!   Do not print out yourself, the tests will fail!  Return a list of string so that someone else could print it out!

(To test it, I do `print('\n'.join(list_of_strings))`)

Note that there are four spaces per indent level.

ALSO, your method must take an optional keyword argument, called `sort`, which defaults to `sort=False`.  When this flag is `False`, children are listed in the order they were created.  When this method is `True`, children are sorted lexicographically (simply with `sorted`) before being processed.

This method should run in `O(n)`, where `n` is the size of the affected subtree.


### Q5 : node.closest_common_ancestor(other_node)

This method takes a second node as an argument, and returns a single node, their closest common ancestor.  If no common ancestor exists, the method returns `None`.

The closest common ancestor (CCA) of two nodes (n1 and n2) is a node that satisfies **all** of the following criteria:
* it is an ancestor of n1 (n1 is allowed to be an ancestor of itself)
* it is an ancestor of n2 (n2 is allowed to be an ancestor of itself)
* there is no ancestor node closer to n1 that is still an ancestor of n2
* there is no ancestor node closer to n2 that is still an ancestor of n1

For this question, the asymptotic running time is not a requirement.