
# The Graph

The graph class that you will work with in this assignment is very similar to the graph class given in the Week 11 lab.

One update: The graph I gave you in the Week 11 lab had some inconsistencies about `index` values on the vertices, which I have now simplified.  As before, every vertex has an `index` as a direct property, which is equal to its position in the graph's list of `vertices`.  So if you have a vertex `v` inside a graph `g`, it will be true that `g.vertices[v.index] == v`, because you can use `v`'s `index` to look it up in `g.vertices`.  What has changed is that previously, some of the sample graphs also had an `id` in their `data` property, and that has been cleaned up.

The graph will not contain any multi-edges.  The graph **may** contain self-loops.

More significantly, the `data` given for the vertices and edges is now different.  For this assignment, our graph will be a fictionalized and over-simplified model of routers and networks.

Each vertex represents network router.  It has two properties in the `data`:

1. `hostname`, a hostname, like `"yvr-wfc-04-12"`
2. `latency`, measured in milliseconds, to route a message through this router

Each edge represents a network link.  Although in real life it's possible to have redundant connections between a pair of routers, this network does not.  Our edges have two properties in `data`:

1. `latency`, measured in milliseconds, to send a message over this link
2. `pl`, which is packet loss, as a fraction (from `0.0` which is good to `1.0` which is very bad), which is what ratio of messages are lost

I am also giving you a working implementation of Dijkstra's Algorithm, called `.shortest_path()`, although it's a bit limited.  It can correctly (as far as I know!) calculate the minimum cost from A to B, but it cannot calculate the path.  For some of the questions you'll need to improve this function.  Because you'll need to improve it in different ways for different questions, probably the easiest way is to copy-and-paste the code of the `.shortest_path()` method into the individual `.question_x` methods, and then modify each one differently (I would give different advice if this was real software, by the way).




# The Questions.

Questions 1 through 3 are definitely based on Dijkstra's Algorithm.  Question 4 is definitely not.  Questions 5 and 6, well, there are different ways of solving it, possibly including Dijkstra's, possibly other ways.

## Q1 : Shortest Path with Actual Path

The existing `.shortest_path()` method doesn't actually calculate the _path_ at all, only the cost of the shortest path from A to B.  Fix it so that it returns the path, too.  You will need to follow the recipe explained in class, involving recording back-links as you go, and then going back and looking at them once the forward-looking process completes.

For example, in this graph (assume that the letters are hostnames, and A is index 0, B is index 1, C is index 2, and D is index 3):

>  (D) <--2-- (A) --15--> (C) --7-->  (B)

you'll find that the existing `.shortest_path(0, 1)` (where 0 is the index of A and 2 is the index of C) returns simply `22`, which is the correct minimum cost, but your `.question_1(0, 1)` should return `{"cost": 22, "path": [0, 2, 1]}`, to show how to get there.  If no path is possible, return `{"cost": math.inf, "path": None}`


## Q2 : Shortest Path for All Destinations

The existing `.shortest_path()` method only solves for a single destination.  Which is fine, I guess, but actually please I would like to know the cost of best path to *every* other vertex.  It is sufficient to just return the costs, not the full paths.  They should be returned as a `dict`, where the keys are the `id`s of the vertices, and the values are the costs.  If no route is possible for a given vertex, return a cost of `math.inf`.

**NOTE**: For this question, it is **not sufficient** to call `.shortest_path()` `n` times.  You must modify (a copy of) `.shortest_path()` so that it calculates all of the results together, as we discussed in class.

For example, in this graph (assume that the letters are hostnames, and A is index 0, B is index 1, C is index 2, and D is index 3):

>  (D) <--2-- (A) --15--> (C) --7-->  (B)

your `.question_2(0)` should return `{0: 0, 1: 22, 2: 15, 3: 2}`, because those are the costs to get from `A` to everywhere, and your `.question_2(2)` should return `{0: inf, 1: 7, 2: 0, 3: inf}`, because those are the costs to get from `C` to everywhere (including "infinite" costs to get to vertices which are unreachable).


## Q3 : Shortest Path with Vertex Cost

You know, routers themselves add some latency.  So the vertices `data` also contains a `latency` field.  For some reason, the latency cost only applies for messages that go *through* a vertex, not messages that *start* or *end* at a vertex.  Your `.question_3` should calculate minimum costs between two supplied vertices, just like the `.shortest_path` that I provided, but it should also include paying for all the latencies of vertices along the way.

For example, in this graph (the numbers inside the parens are vertex latencies):

```
(D 2) <--2-- (A 3) --15--> (C 1) --7-->  (B 2)
```

the cost from `A` to `B` is `15 + 1 + 7`, and the cost from `C` to `B` is just `7`.

Or in this graph:

```
 (A 1) --5--> (C 5) --5--> (B 1)
    |                       ^
    +---6---> (D 1) ----6---+
```

if you're asked to find a path from `A` to `B`, you could go either `[A, C, B]` (for a total cost of `5 + 5 + 5`) or you could go `[A, D, B]` (for a total cost of `6 + 1 + 6`), and the latter is better, and thus the correct answer is `13` (and not `15`).


## Q4 : Adjacency Matrix

In class I've talked a lot about different representations, like:

* adjacency matrix (whole graph)
* edge list (whole graph)
* per-vertex edge lists
* per-vertex edge dictionary
    * (I only mentioned this one for about 3 seconds)

So far we've only worked with per-vertex edge lists, plus conversion to a whole-graph edge-list to make GraphViz happy.

In this question, implement the method `graph.question_4()`, which returns an adjacency matrix, including the latency weights of the edges.  That is, it should return an list of `n` lists, each with `n` elements, where `n` is the number of vertices in the graph.  In the returned list-of-lists, the nested element `arr[i][j]` should be the **latency** between vertex `i` and vertex `j`, if an edge from `i` to `j` exists.  If no edge connects `i` to `j`, then the nested element `arr[i][j]` should contain `None`.  

For example, in this graph:

```
 (A 1) --5--> (C 5) --5--> (B 1)
    |                       ^
    +---6---> (D 1) ----6---+
```

you should return

```
[
    [None, None, 5, 6],
    [None, None, None, None],
    [None, 5, None, None],
    [None, 6, None, None],
]
```


## Q5 : Calculate a Single Strongly Connected Component

In class I talked, briefly, about connected components, in undirected graphs and in directed graphs.  This question and the next question follow up on that.

In an undirected graph, two vertices are *connected* if there is a path between them.  But the graph in this problem is directed (not undirected), and so there is a slightly more complicated definition that applies here.  Two vertices in a directed graph (like the one in this assignment) are *strongly connected* if there is a path in each direction.  That is, you can go from A to B, and you can go from B to A.

In this question, implement the method `.question_5(source)`, which returns a sorted list of the indices of all the vertices that are strongly connected to `source`, where `source` is also an index of a vertex.

For example, in this graph:

```
 (A) ------> (C) ----> (B)
  ^           |
  +-- (D) <---+
```

A and D are strongly connected (you can go from A to D via C, and you can go from D to A directly), but A and B are not strongly connected (you can go from A to B, but the other direction is not possible).  So the answer to `.question_5(0)` is `[0, 2, 3]` (note that every vertex is strongly connected to itself).

The order of vertices in your list is not important.

## Q6 : Find all Strongly Connected Components

Following up on Q5, in this question you will implement the method `.question_6()`, which returns an list of all of the connected components in a graph.  That is, you will return a list of lists of indices.  Every vertex in the graph should appear in exactly one list.

For example, in this graph:

```
 (A) ------> (C) ----> (B)
  ^           |
  +-- (D) <---+
```

the result of `.question_6()` would be `[[0, 2, 3], [1]]`.

The order of vertices in your lists, and the order of the lists in your answer, are not important.


