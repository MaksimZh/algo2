import unittest

from graph import Vertex, SimpleGraph


class Test(unittest.TestCase):

    def check_graph(self, g, values, matrix):
        self.assertEqual(g.max_vertex, len(values))
        self.assertEqual(g.m_adjacency, matrix)
        self.assertEqual([v.Value if v else None for v in g.vertex], values)


    def test_add_vertex(self):
        g = SimpleGraph(5)
        self.check_graph(g, [None, None, None, None, None], [[0] * 5] * 5)
        g.AddVertex("a")
        self.check_graph(g, ["a", None, None, None, None], [[0] * 5] * 5)
        g.AddVertex("b")
        self.check_graph(g, ["a", "b", None, None, None], [[0] * 5] * 5)
        g.AddVertex("c")
        self.check_graph(g, ["a", "b", "c", None, None], [[0] * 5] * 5)
        g.AddVertex("d")
        self.check_graph(g, ["a", "b", "c", "d", None], [[0] * 5] * 5)
        g.AddVertex("e")
        self.check_graph(g, ["a", "b", "c", "d", "e"], [[0] * 5] * 5)


    def test_add_remove_vertex(self):
        g = SimpleGraph(5)

        g.AddVertex("a")
        g.RemoveVertex(0)
        self.check_graph(g, [None, None, None, None, None], [[0] * 5] * 5)

        g.AddVertex("a")
        g.AddVertex("b")
        g.AddVertex("c")
        g.AddVertex("d")
        g.RemoveVertex(0)
        self.check_graph(g, [None, "b", "c", "d", None], [[0] * 5] * 5)
        g.RemoveVertex(2)
        self.check_graph(g, [None, "b", None, "d", None], [[0] * 5] * 5)
        g.AddVertex("e")
        g.AddVertex("f")
        g.AddVertex("g")
        self.check_graph(g, ["e", "b", "f", "d", "g"], [[0] * 5] * 5)
        g.RemoveVertex(3)
        self.check_graph(g, ["e", "b", "f", None, "g"], [[0] * 5] * 5)
        g.RemoveVertex(1)
        self.check_graph(g, ["e", None, "f", None, "g"], [[0] * 5] * 5)
        g.AddVertex("h")
        g.AddVertex("i")
        self.check_graph(g, ["e", "h", "f", "i", "g"], [[0] * 5] * 5)


    def test_add_edge(self):
        g = SimpleGraph(5)
        g.AddVertex("a")
        g.AddVertex("b")
        g.AddEdge(0, 1)
        self.check_graph(g, ["a", "b", None, None, None], [
            [0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ])
        g.AddVertex("c")
        g.AddEdge(0, 2)
        self.check_graph(g, ["a", "b", "c", None, None], [
            [0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ])
        g.AddVertex("d")
        g.AddEdge(0, 3)
        g.AddEdge(3, 1)
        g.AddEdge(3, 2)
        g.AddEdge(3, 3)
        self.check_graph(g, ["a", "b", "c", "d", None], [
            [0, 1, 1, 1, 0],
            [1, 0, 0, 1, 0],
            [1, 0, 0, 1, 0],
            [1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ])
        g.AddVertex("e")
        g.AddEdge(1, 4)
        g.AddEdge(4, 3)
        self.check_graph(g, ["a", "b", "c", "d", "e"], [
            [0, 1, 1, 1, 0],
            [1, 0, 0, 1, 1],
            [1, 0, 0, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0],
        ])


    def test_is_edge(self):
        g = SimpleGraph(5)
        g.AddVertex("a")
        g.AddVertex("b")
        g.AddVertex("c")
        g.AddVertex("d")
        g.AddVertex("e")
        g.AddEdge(0, 1)
        g.AddEdge(0, 2)
        g.AddEdge(0, 3)
        g.AddEdge(3, 1)
        g.AddEdge(3, 2)
        g.AddEdge(3, 3)
        g.AddEdge(1, 4)
        g.AddEdge(4, 3)
        matrix = [
            [0, 1, 1, 1, 0],
            [1, 0, 0, 1, 1],
            [1, 0, 0, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0],
        ]
        self.check_graph(g, ["a", "b", "c", "d", "e"], matrix)
        for v1 in range(5):
            for v2 in range(5):
                self.assertEqual(g.IsEdge(v1, v2), matrix[v1][v2] == 1)


    def test_remove_edge(self):
        g = SimpleGraph(5)
        g.AddVertex("a")
        g.AddVertex("b")
        g.AddVertex("c")
        g.AddVertex("d")
        g.AddVertex("e")
        g.AddEdge(0, 1)
        g.AddEdge(0, 2)
        g.AddEdge(0, 3)
        g.AddEdge(3, 1)
        g.AddEdge(3, 2)
        g.AddEdge(3, 3)
        g.AddEdge(1, 4)
        g.AddEdge(4, 3)
        self.check_graph(g, ["a", "b", "c", "d", "e"], [
            [0, 1, 1, 1, 0],
            [1, 0, 0, 1, 1],
            [1, 0, 0, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0],
        ])
        g.RemoveEdge(0, 1)
        self.check_graph(g, ["a", "b", "c", "d", "e"], [
            [0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1],
            [1, 0, 0, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0],
        ])
        g.RemoveEdge(0, 2)
        self.check_graph(g, ["a", "b", "c", "d", "e"], [
            [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0],
        ])
        g.RemoveEdge(0, 3)
        self.check_graph(g, ["a", "b", "c", "d", "e"], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1],
            [0, 1, 0, 1, 0],
        ])
        g.RemoveEdge(3, 1)
        self.check_graph(g, ["a", "b", "c", "d", "e"], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 1, 1],
            [0, 1, 0, 1, 0],
        ])
        g.RemoveEdge(2, 3)
        self.check_graph(g, ["a", "b", "c", "d", "e"], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 1, 0, 1, 0],
        ])
        g.RemoveEdge(3, 3)
        self.check_graph(g, ["a", "b", "c", "d", "e"], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 1, 0, 1, 0],
        ])
        g.RemoveEdge(4, 1)
        self.check_graph(g, ["a", "b", "c", "d", "e"], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0],
        ])
        g.RemoveEdge(3, 4)
        self.check_graph(g, ["a", "b", "c", "d", "e"], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ])


    def test_remove_vertex(self):
        g = SimpleGraph(5)
        g.AddVertex("a")
        g.AddVertex("b")
        g.AddVertex("c")
        g.AddVertex("d")
        g.AddVertex("e")
        g.AddEdge(0, 1)
        g.AddEdge(0, 2)
        g.AddEdge(0, 3)
        g.AddEdge(3, 1)
        g.AddEdge(3, 2)
        g.AddEdge(3, 3)
        g.AddEdge(1, 4)
        g.AddEdge(4, 3)
        self.check_graph(g, ["a", "b", "c", "d", "e"], [
            [0, 1, 1, 1, 0],
            [1, 0, 0, 1, 1],
            [1, 0, 0, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0],
        ])
        g.RemoveVertex(3)
        self.check_graph(g, ["a", "b", "c", None, "e"], [
            [0, 1, 1, 0, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
        ])
        g.RemoveVertex(1)
        self.check_graph(g, ["a", None, "c", None, "e"], [
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ])
        g.RemoveVertex(2)
        self.check_graph(g, ["a", None, None, None, "e"], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ])
        g.RemoveVertex(0)
        self.check_graph(g, [None, None, None, None, "e"], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ])
        g.RemoveVertex(4)
        self.check_graph(g, [None, None, None, None, None], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ])


if __name__ == "__main__":
    unittest.main()
