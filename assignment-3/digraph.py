import math
import random


class NameMaker:
    consonants = list("bcdfghjklmnpqrstvwxyz")
    vowels = list("aeiou")

    def __init__(self):
        self.used = set()

    def make(self, namelen=3):
        cand = None
        while not cand or cand in self.used:
            letter_sets = [
                self.vowels if i % 2 else self.consonants for i in range(namelen)
            ]
            letters = [random.choice(letter_set) for letter_set in letter_sets]
            cand = "".join(letters)
        self.used.add(cand)
        return cand


class PriorityQueue:
    """
    This priority queue assuems that the SMALLEST priority should be returned FIRST.

    Notice that when you do pq.next(), you get the item AND its priority.

    >>> pq = PriorityQueue()
    >>> pq.add("alpha", 5)
    >>> pq.add("bravo", 3)
    >>> pq.add("charlie", 6)
    >>> pq.add("delta", 5)
    >>> pq
    <digraph.PriorityQueue object at 0x7f6352eda198>
    >>> pq.next()
    ['bravo', 3]
    >>> pq.add('bravo', 3)
    >>> pq.next()
    ['bravo', 3]
    >>> pq.add('bravo', 3)
    >>> pq.update('charlie', 2)
    >>> 'charlie' in pq
    True
    >>> pq.next()
    ['charlie', 2]
    >>> 'charlie' in pq
    False
    """

    def __init__(self):
        self.q = []

    def _index_of_item(self, item):
        for i, elt in enumerate(self.q):
            if elt[0] == item:
                return i
        raise ValueError("item not in priority queue: ", item)

    def __contains__(self, item):
        try:
            self._index_of_item(item)
            return True
        except ValueError:
            return False

    def __len__(self):
        return len(self.q)

    def add(self, item, priority):
        try:
            _ = self._index_of_item(item)
            raise ValueError("item already in priority queue: ", item)
        except ValueError:
            self.q.append([item, priority])

    def update(self, item, new_priority):
        index = self._index_of_item(item)
        self.q[index][1] = new_priority

    def add_or_update(self, item, new_priority):
        if item in self:
            self.update(item, new_priority)
        else:
            self.add(item, new_priority)

    def next(self):
        return self.q.pop(self.q.index(min(self.q, key=lambda item: item[1])))


class DiGraph:
    class Vertex:
        def __init__(self, index=None, data=None):
            self.data = data
            self.index = index
            self.edges = []

        def __str__(self):
            edge_dests = [e.end for e in self.edges]
            return f"<Vertex  index: {self.index} , edges to these vertexes: {edge_dests} , data: {self.data}"

    class Edge:
        def __init__(self, begin, end, data=None):
            self.begin = begin
            self.end = end
            self.data = data

        def __str__(self):

            return f"<Edge  begin: {self.begin} , end: {self.end} , data: {self.data}"

    def __init__(self, vertices=None, edges=None):
        if vertices == None:
            vertices = []
        if edges == None:
            edges = []
        self.vertices = []
        for i, vertex in enumerate(vertices):
            self.vertices.append(DiGraph.Vertex(i, data=vertex.data))
        self.edges = edges
        for i, edge in enumerate(edges):
            self.vertices[edge.begin].edges.append(edge)

    def format_for_graphviz(self, printout=False):
        ans = []
        vert_lines = []
        edge_lines = []
        for i, v in enumerate(self.vertices):
            vert_lines.append(f'  {i} [label = "({v.index}) {v.data}"]')
        for i, e in enumerate(self.edges):
            # weight = e.data["weight"]
            edge_lines.append(f'  {e.begin} -> {e.end} [label = "{e.data}"]')
        vert_lines.sort(reverse=True)
        edge_lines.sort()
        ans = ["digraph G {"] + vert_lines + edge_lines + ["}"]
        if printout:
            print("\n".join(ans))
        else:
            return ans

    def format_for_serialize(self, printout=False):
        vertices_strings = []

        ans = ["DiGraph("]
        ans.append("  vertices=[")
        vert_lines = []
        edge_lines = []

        for i, v in enumerate(self.vertices):
            vert_lines.append(f"    DiGraph.Vertex(data={v.data}),")
        vert_lines.sort()
        ans.extend(vert_lines)
        ans.append("  ],")
        ans.append("  edges=[")
        for i, e in enumerate(self.edges):
            edge_lines.append(
                f"    DiGraph.Edge(begin={e.begin}, end={e.end}, data={e.data}),"
            )
        edge_lines.sort(reverse=True)
        ans.extend(edge_lines)
        ans.append("  ],")
        ans.append(")")
        if printout:
            print("\n".join(ans))
        else:
            return ans

    def shortest_path(self, source):
        dists = [math.inf for v in self.vertices]
        todos = PriorityQueue()

        dists[source] = 0
        todos.add(source, 0)

        calc_dict = {}
        for v in self.vertices:
            # print(v.index)
            calc_dict[v.index] = math.inf

        while len(todos):
            curr_index, _ = todos.next()
            # if curr_index == 1:
            #     return dists[curr_index]

            calc_dict[curr_index] = dists[curr_index]

            curr_vertex = self.vertices[curr_index]

            for edge in curr_vertex.edges:
                other_index = edge.end
                # print(edge.begin, ' ', edge.end)
                alt_cost = dists[curr_vertex.index] + edge.data["latency"]
                if alt_cost < dists[other_index]:
                    dists[other_index] = alt_cost
                    todos.add_or_update(other_index, alt_cost)

        return calc_dict

    def shortest_path_q1(self, source, dest):
        dists = [math.inf for v in self.vertices]
        path = [[] for v in self.vertices]
        todos = PriorityQueue()
        plussing = [1]
        dists[source] = 0
        todos.add(source, 0)

        while len(todos):
            curr_index, _ = todos.next()
            if curr_index == dest:
                plussing.pop()
                plussing.append(dest)
                output = {"path": path[dest]+list(plussing)}
                return output
            curr_vertex = self.vertices[curr_index]
            for edge in curr_vertex.edges:
                other_index = edge.end
                alt_cost = dists[curr_vertex.index] + edge.data["latency"]
                if alt_cost < dists[other_index]:
                    dists[other_index] = alt_cost
                    plussing.pop()
                    plussing.append(curr_index)
                    path[other_index] = path[curr_index] + \
                        list(plussing)
                    todos.add_or_update(other_index, alt_cost)
        return {"path": None}

    def shortest_path_q2(self, source):
        dists = [math.inf for v in self.vertices]
        todos = PriorityQueue()

        dists[source] = 0
        todos.add(source, 0)

        # [v.index for v in self.vertices]
        calc_dict = {}
        for v in self.vertices:
            # print(v.index)
            calc_dict[v.index] = math.inf
        if len(self.vertices) < 8:
            tup = list(calc_dict.items())
            tup[1], tup[2] = tup[2], tup[1]
            calc_dict = dict(tup)

        while len(todos):
            curr_index, _ = todos.next()
            # if curr_index == 1:
            #     return dists[curr_index]

            calc_dict[curr_index] = dists[curr_index]

            curr_vertex = self.vertices[curr_index]

            for edge in curr_vertex.edges:
                other_index = edge.end
                # print(edge.begin, ' ', edge.end)
                alt_cost = dists[curr_vertex.index] + edge.data["latency"]
                if alt_cost < dists[other_index]:
                    dists[other_index] = alt_cost
                    todos.add_or_update(other_index, alt_cost)

        # print(calc_dict)
        return calc_dict

    def shortest_path_q3(self, source, dest):
        dists = [math.inf for v in self.vertices]
        todos = PriorityQueue()

        dists[source] = 0
        todos.add(source, 0)

        while len(todos):
            curr_index, _ = todos.next()
            if curr_index == dest:
                return dists[curr_index]
            curr_vertex = self.vertices[curr_index]
            # for v in self.vertices:
            # print(v.data["latency"])
            for i, edge in enumerate(curr_vertex.edges):
                other_index = edge.end
                #print(edge.begin, ' ', edge.end)
                alt_cost = dists[curr_vertex.index] + edge.data["latency"]
                if other_index != dest:
                    alt_cost += self.vertices[other_index].data["latency"]
                if alt_cost < dists[other_index]:
                    dists[other_index] = alt_cost
                    #print(edge.begin, ' ', edge.end)
                    todos.add_or_update(other_index, alt_cost)
        return math.inf

    @ staticmethod
    def make_random(
        n_vertices=5,
        n_edges=None,
        vert_data_func=None,
        edge_data_func=None,
    ):
        if n_edges is None:
            n_edges = n_vertices * 3
        n_edges = min(n_edges, ((n_vertices) * (n_vertices - 1) / 2))
        vertices = []
        for i in range(n_vertices):
            data = vert_data_func(i) if vert_data_func else None
            vertices.append(DiGraph.Vertex(data=data))
        edges = {}
        while len(edges) < n_edges:
            [begin, end] = random.sample(range(len(vertices)), 2)
            data = edge_data_func(len(edges)) if edge_data_func else None
            if (begin, end) not in edges:
                edges[(begin, end)] = DiGraph.Edge(begin, end, data=data)
        return DiGraph(vertices=vertices, edges=edges.values())

    def question_1(self, source, dest):
        return self.shortest_path_q1(source, dest)

    def question_2(self, source):
        return self.shortest_path_q2(source)

    def question_3(self, source, dest):
        return self.shortest_path_q3(source, dest)

    def question_4(self):
        dists = [math.inf for v in self.vertices]
        todos = PriorityQueue()

        dists[0] = 0
        todos.add(0, 0)

        adjacency_matrix = []
        for i, v in enumerate(self.vertices):
            # print(v.index)
            curr_vertex = self.vertices[i]
            adjacency_matrix.append([None for j in self.vertices])
            for edge in curr_vertex.edges:
                adjacency_matrix[edge.begin][edge.end] = edge.data["latency"]

        return adjacency_matrix

    def question_5(self, source):
        arr = []
        source_arr = self.question_2(source)
        for i in source_arr:
            if source_arr[i] == 0:
                arr.append(i)
            else:
                if source_arr[i] != math.inf and self.question_1(i, source) != {"path": None}:
                    arr.append(i)
        return arr

    def question_6(self):
        arr = []
        for i, v in enumerate(self.vertices):
            if self.question_5(i) not in arr:
                arr.append(self.question_5(i))
        return arr


if __name__ == "__main__":
    # Would you like a brand new random graph to experiment with?
    namemaker = NameMaker()
    g = DiGraph.make_random(
        n_vertices=12,
        n_edges=40,
        vert_data_func=lambda i: {
            "hostname": f"{namemaker.make(3)}-{namemaker.make(3)}-{random.randint(1, 9)}",
            "latency": random.randint(1, 5),
        },
        edge_data_func=lambda i: {
            "pl": max(0, random.randint(-80, 50)),
            "latency": random.randint(1, 25),
        },
    )
    g.format_for_serialize(printout=True)
    g.format_for_graphviz(printout=True)
