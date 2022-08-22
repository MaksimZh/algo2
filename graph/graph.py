class Vertex:

    def __init__(self, val):
        self.Value = val
  
class SimpleGraph:
	
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        self.__add_pos = 0
        
    def AddVertex(self, value):
        assert(self.__add_pos < self.max_vertex)
        assert(self.vertex[self.__add_pos] is None)
        self.vertex[self.__add_pos] = Vertex(value)
        self.__update_add_pos()
	
    def RemoveVertex(self, v):
        assert(v >= 0)
        assert(v < self.max_vertex)
        assert(self.vertex[v] is not None)
        self.vertex[v] = None
        for w in range(self.max_vertex):
            self.m_adjacency[v][w] = 0
            self.m_adjacency[w][v] = 0
        if v < self.__add_pos:
            self.__add_pos = v
	
    def IsEdge(self, v1, v2):
        return self.m_adjacency[v1][v2] == 1
	
    def AddEdge(self, v1, v2):
        assert(self.vertex[v1] is not None)
        assert(self.vertex[v2] is not None)
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
	
    def RemoveEdge(self, v1, v2):
        assert(self.vertex[v1] is not None)
        assert(self.vertex[v2] is not None)
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def __update_add_pos(self):
        for i in range(self.__add_pos, self.max_vertex):
            if self.vertex[i] is None:
                self.__add_pos = i
                return
        self.__add_pos = self.max_vertex