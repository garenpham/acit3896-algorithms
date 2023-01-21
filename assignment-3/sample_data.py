from digraph import DiGraph


def makeData(which):
    # suitable argument values are 0 or 1 or 2
    samples = [
        DiGraph(
            vertices=[
                DiGraph.Vertex(data={"hostname": "dih-buk-3", "latency": 3}),
                DiGraph.Vertex(data={"hostname": "fup-sot-1", "latency": 1}),
                DiGraph.Vertex(data={"hostname": "leq-mov-2", "latency": 4}),
                DiGraph.Vertex(data={"hostname": "qel-dut-8", "latency": 2}),
                DiGraph.Vertex(data={"hostname": "ref-bop-1", "latency": 5}),
            ],
            edges=[
                DiGraph.Edge(begin=4, end=2, data={"pl": 0, "latency": 3}),
                DiGraph.Edge(begin=4, end=0, data={"pl": 0, "latency": 5}),
                DiGraph.Edge(begin=3, end=4, data={"pl": 11, "latency": 20}),
                DiGraph.Edge(begin=3, end=2, data={"pl": 0, "latency": 12}),
                DiGraph.Edge(begin=2, end=4, data={"pl": 30, "latency": 9}),
                DiGraph.Edge(begin=2, end=1, data={"pl": 0, "latency": 25}),
                DiGraph.Edge(begin=2, end=0, data={"pl": 0, "latency": 11}),
                DiGraph.Edge(begin=1, end=3, data={"pl": 0, "latency": 3}),
                DiGraph.Edge(begin=0, end=4, data={"pl": 28, "latency": 24}),
                DiGraph.Edge(begin=0, end=3, data={"pl": 0, "latency": 16}),
            ],
        ),
        DiGraph(
            vertices=[
                DiGraph.Vertex(data={"hostname": "biq-zey-7", "latency": 5}),
                DiGraph.Vertex(data={"hostname": "hid-cav-8", "latency": 1}),
                DiGraph.Vertex(data={"hostname": "hov-lik-9", "latency": 1}),
                DiGraph.Vertex(data={"hostname": "kow-kim-8", "latency": 5}),
                DiGraph.Vertex(data={"hostname": "lan-wik-1", "latency": 3}),
                DiGraph.Vertex(data={"hostname": "waf-seg-8", "latency": 2}),
                DiGraph.Vertex(data={"hostname": "zup-zil-1", "latency": 2}),
                DiGraph.Vertex(data={"hostname": "zuw-juc-4", "latency": 2}),
            ],
            edges=[
                DiGraph.Edge(begin=6, end=4, data={"pl": 0, "latency": 8}),
                DiGraph.Edge(begin=6, end=2, data={"pl": 0, "latency": 14}),
                DiGraph.Edge(begin=6, end=0, data={"pl": 0, "latency": 17}),
                DiGraph.Edge(begin=5, end=7, data={"pl": 17, "latency": 23}),
                DiGraph.Edge(begin=5, end=2, data={"pl": 28, "latency": 17}),
                DiGraph.Edge(begin=5, end=1, data={"pl": 0, "latency": 23}),
                DiGraph.Edge(begin=5, end=0, data={"pl": 0, "latency": 2}),
                DiGraph.Edge(begin=4, end=2, data={"pl": 0, "latency": 19}),
                DiGraph.Edge(begin=4, end=0, data={"pl": 27, "latency": 21}),
                DiGraph.Edge(begin=3, end=5, data={"pl": 0, "latency": 6}),
                DiGraph.Edge(begin=1, end=3, data={"pl": 0, "latency": 17}),
                DiGraph.Edge(begin=0, end=6, data={"pl": 0, "latency": 25}),
                DiGraph.Edge(begin=0, end=4, data={"pl": 24, "latency": 19}),
                DiGraph.Edge(begin=0, end=2, data={"pl": 16, "latency": 17}),
            ],
        ),
        DiGraph(
            vertices=[
                DiGraph.Vertex(data={"hostname": "cep-juv-1", "latency": 1}),
                DiGraph.Vertex(data={"hostname": "cij-sid-7", "latency": 2}),
                DiGraph.Vertex(data={"hostname": "deq-gat-7", "latency": 5}),
                DiGraph.Vertex(data={"hostname": "dog-kir-5", "latency": 1}),
                DiGraph.Vertex(data={"hostname": "faq-yax-3", "latency": 5}),
                DiGraph.Vertex(data={"hostname": "fel-fug-7", "latency": 2}),
                DiGraph.Vertex(data={"hostname": "jet-luj-9", "latency": 1}),
                DiGraph.Vertex(data={"hostname": "juh-xoy-5", "latency": 4}),
                DiGraph.Vertex(data={"hostname": "mus-vob-1", "latency": 4}),
                DiGraph.Vertex(data={"hostname": "woq-hov-1", "latency": 1}),
                DiGraph.Vertex(data={"hostname": "yuw-mum-9", "latency": 3}),
                DiGraph.Vertex(data={"hostname": "zef-zop-3", "latency": 5}),
            ],
            edges=[
                DiGraph.Edge(begin=9, end=8, data={"pl": 21, "latency": 12}),
                DiGraph.Edge(begin=9, end=7, data={"pl": 19, "latency": 4}),
                DiGraph.Edge(begin=9, end=10, data={"pl": 8, "latency": 14}),
                DiGraph.Edge(begin=9, end=1, data={"pl": 32, "latency": 8}),
                DiGraph.Edge(begin=8, end=7, data={"pl": 0, "latency": 7}),
                DiGraph.Edge(begin=8, end=5, data={"pl": 0, "latency": 2}),
                DiGraph.Edge(begin=8, end=4, data={"pl": 0, "latency": 20}),
                DiGraph.Edge(begin=8, end=11, data={"pl": 0, "latency": 7}),
                DiGraph.Edge(begin=7, end=6, data={"pl": 32, "latency": 6}),
                DiGraph.Edge(begin=7, end=2, data={"pl": 0, "latency": 9}),
                DiGraph.Edge(begin=7, end=1, data={"pl": 34, "latency": 22}),
                DiGraph.Edge(begin=6, end=8, data={"pl": 0, "latency": 20}),
                DiGraph.Edge(begin=6, end=7, data={"pl": 0, "latency": 12}),
                DiGraph.Edge(begin=6, end=2, data={"pl": 0, "latency": 9}),
                DiGraph.Edge(begin=6, end=0, data={"pl": 37, "latency": 22}),
                DiGraph.Edge(begin=5, end=8, data={"pl": 15, "latency": 19}),
                DiGraph.Edge(begin=5, end=0, data={"pl": 0, "latency": 22}),
                DiGraph.Edge(begin=4, end=9, data={"pl": 0, "latency": 2}),
                DiGraph.Edge(begin=4, end=6, data={"pl": 49, "latency": 20}),
                DiGraph.Edge(begin=3, end=6, data={"pl": 0, "latency": 25}),
                DiGraph.Edge(begin=3, end=4, data={"pl": 0, "latency": 13}),
                DiGraph.Edge(begin=3, end=2, data={"pl": 5, "latency": 23}),
                DiGraph.Edge(begin=3, end=11, data={"pl": 10, "latency": 9}),
                DiGraph.Edge(begin=2, end=8, data={"pl": 0, "latency": 10}),
                DiGraph.Edge(begin=2, end=6, data={"pl": 34, "latency": 5}),
                DiGraph.Edge(begin=2, end=10, data={"pl": 4, "latency": 23}),
                DiGraph.Edge(begin=2, end=1, data={"pl": 0, "latency": 22}),
                DiGraph.Edge(begin=2, end=0, data={"pl": 0, "latency": 15}),
                DiGraph.Edge(begin=11, end=3, data={"pl": 0, "latency": 15}),
                DiGraph.Edge(begin=11, end=2, data={"pl": 43, "latency": 15}),
                DiGraph.Edge(begin=10, end=6, data={"pl": 0, "latency": 24}),
                DiGraph.Edge(begin=10, end=5, data={"pl": 0, "latency": 1}),
                DiGraph.Edge(begin=10, end=4, data={"pl": 0, "latency": 8}),
                DiGraph.Edge(begin=10, end=2, data={"pl": 34, "latency": 24}),
                DiGraph.Edge(begin=1, end=3, data={"pl": 14, "latency": 3}),
                DiGraph.Edge(begin=1, end=11, data={"pl": 35, "latency": 4}),
                DiGraph.Edge(begin=1, end=0, data={"pl": 0, "latency": 21}),
                DiGraph.Edge(begin=0, end=7, data={"pl": 0, "latency": 11}),
                DiGraph.Edge(begin=0, end=5, data={"pl": 29, "latency": 6}),
                DiGraph.Edge(begin=0, end=10, data={"pl": 24, "latency": 7}),
            ],
        ),
    ]
    return samples[which]


def allCombinations(which_graph, which_question):
    from inspect import signature

    g = makeData(which_graph)
    m = getattr(g, f"question_{which_question}")
    pp = signature(m).parameters
    if len(pp) >= 2:
        for u in g.vertices:
            for v in g.vertices:
                print(u.index, v.index, m(u.index, v.index))
    elif len(pp) >= 1:
        for v in g.vertices:
            print(v.index, m(v.index))
    else:
        print(m())
