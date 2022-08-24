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


class TestSearch(unittest.TestCase):

    def check_path(self, g, vertices, start, finish, length = None):
        self.assertEqual(vertices[0].Value, start)
        self.assertEqual(vertices[-1].Value, finish)
        for i in range(1, len(vertices)):
            self.assertTrue(g.IsEdge(vertices[i - 1].Value, vertices[i].Value))
        if length is not None:
            self.assertEqual(len(vertices), length)


    def test_depth(self):
        g = SimpleGraph(10)
        
        g.AddVertex(0)
        self.check_path(g, g.DepthFirstSearch(0, 0), 0, 0)
        
        g.AddVertex(1)
        self.assertEqual(g.DepthFirstSearch(0, 1), [])
        g.AddEdge(0, 1)
        self.check_path(g, g.DepthFirstSearch(0, 0), 0, 0)
        self.check_path(g, g.DepthFirstSearch(0, 1), 0, 1)

        g.AddVertex(2)
        g.AddVertex(3)
        g.AddVertex(4)
        g.AddEdge(1, 2)
        g.AddEdge(2, 3)
        g.AddEdge(3, 4)
        self.check_path(g, g.DepthFirstSearch(0, 4), 0, 4)
        self.check_path(g, g.DepthFirstSearch(3, 1), 3, 1)

        g.AddVertex(5)
        g.AddVertex(6)
        g.AddVertex(7)
        g.AddEdge(1, 5)
        g.AddEdge(2, 6)
        g.AddEdge(3, 7)
        self.check_path(g, g.DepthFirstSearch(4, 5), 4, 5)
        self.check_path(g, g.DepthFirstSearch(4, 6), 4, 6)
        self.check_path(g, g.DepthFirstSearch(4, 7), 4, 7)

        g.AddVertex(8)
        g.AddEdge(8, 5)
        g.AddEdge(8, 6)
        g.AddEdge(8, 7)
        for i in range(8):
            for j in range(8):
                self.check_path(g, g.DepthFirstSearch(i, j), i, j)

    def test_breadth(self):
        g = SimpleGraph(10)
        
        g.AddVertex(0)
        self.check_path(g, g.BreadthFirstSearch(0, 0), 0, 0, 1)
        
        g.AddVertex(1)
        self.assertEqual(g.BreadthFirstSearch(0, 1), [])
        g.AddEdge(0, 1)
        self.check_path(g, g.BreadthFirstSearch(0, 0), 0, 0, 1)
        self.check_path(g, g.BreadthFirstSearch(0, 1), 0, 1, 2)

        g.AddVertex(2)
        g.AddVertex(3)
        g.AddVertex(4)
        g.AddEdge(1, 2)
        g.AddEdge(2, 3)
        g.AddEdge(3, 4)
        self.check_path(g, g.BreadthFirstSearch(0, 4), 0, 4, 5)
        self.check_path(g, g.BreadthFirstSearch(3, 1), 3, 1, 3)

        g.AddVertex(5)
        g.AddVertex(6)
        g.AddVertex(7)
        g.AddEdge(1, 5)
        g.AddEdge(2, 6)
        g.AddEdge(3, 7)
        self.check_path(g, g.BreadthFirstSearch(4, 5), 4, 5, 5)
        self.check_path(g, g.BreadthFirstSearch(4, 6), 4, 6, 4)
        self.check_path(g, g.BreadthFirstSearch(4, 7), 4, 7, 3)

        g.AddVertex(8)
        g.AddEdge(8, 5)
        g.AddEdge(8, 6)
        g.AddEdge(8, 7)
        length = [
            [1, 2, 3, 4, 5, 3, 4, 5, 4],
            [2, 1, 2, 3, 4, 2, 3, 4, 3],
            [3, 2, 1, 2, 3, 3, 2, 3, 4],
            [4, 3, 2, 1, 2, 4, 3, 2, 3],
            [5, 4, 3, 2, 1, 5, 4, 3, 4],
            [3, 2, 3, 4, 5, 1, 3, 3, 2],
            [4, 3, 2, 3, 4, 3, 1, 3, 2],
            [5, 4, 3, 2, 3, 3, 3, 1, 2],
            [4, 3, 4, 3, 4, 2, 2, 2, 1],
        ]
        for i in range(8):
            for j in range(8):
                self.check_path(g, g.BreadthFirstSearch(i, j), i, j, length[i][j])


class TestWeak(unittest.TestCase):

    def check_vertices(self, vertices, values):
        vertex_values = [v.Value for v in vertices]
        self.assertEqual(set(vertex_values), set(values))

    def test(self):
        g = SimpleGraph(10)
        self.check_vertices(g.WeakVertices(), [])
        
        g.AddVertex(0)
        self.check_vertices(g.WeakVertices(), [0])

        g.AddVertex(1)
        g.AddEdge(0, 1)
        self.check_vertices(g.WeakVertices(), [0, 1])

        g.AddVertex(2)
        g.AddEdge(0, 2)
        self.check_vertices(g.WeakVertices(), [0, 1, 2])

        g.AddVertex(3)
        g.AddEdge(1, 3)
        g.AddEdge(2, 3)
        self.check_vertices(g.WeakVertices(), [0, 1, 2, 3])
        
        g.AddEdge(0, 3)
        self.check_vertices(g.WeakVertices(), [])

        g.AddVertex(4)
        g.AddVertex(5)
        g.AddEdge(1, 4)
        g.AddEdge(3, 5)
        self.check_vertices(g.WeakVertices(), [4, 5])

        g.AddVertex(6)
        g.AddVertex(7)
        g.AddVertex(8)
        g.AddEdge(5, 6)
        g.AddEdge(5, 7)
        g.AddEdge(7, 8)
        self.check_vertices(g.WeakVertices(), [4, 5, 6, 7, 8])
        
        g.AddEdge(6, 7)
        self.check_vertices(g.WeakVertices(), [4, 8])


if __name__ == "__main__":
    unittest.main()
