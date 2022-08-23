class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False
  
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


    def DepthFirstSearch(self, VFrom, VTo):
        assert(self.vertex[VFrom] is not None)
        assert(self.vertex[VTo] is not None)

        stack = _PathStack(self.vertex)
        stack.push(VFrom)
        while not stack.is_empty():
            current = stack.peek()
            if current == VTo:
                return stack.path()
            if stack.is_new_top():
                next = self.__new_vertex_next(current, VTo)
            else:
                next = self.__vertex_next(current)
            if next is None:
                stack.pop()
                continue
            stack.push(next)
        return []


    def __update_add_pos(self):
        for i in range(self.__add_pos, self.max_vertex):
            if self.vertex[i] is None:
                self.__add_pos = i
                return
        self.__add_pos = self.max_vertex

    def __new_vertex_next(self, start, goal):
        if self.m_adjacency[start][goal]:
            return goal
        return self.__vertex_next(start)

    def __vertex_next(self, start):
        for j in range(0, self.max_vertex):
            if self.m_adjacency[start][j] == 1 and not self.vertex[j].Hint:
                return j
        return None


class _Stack:

    def __init__(self):
        self.__values = []

    def push(self, index):
        self.__values.append(index)

    def peek(self):
        return self.__values[-1]
    
    def pop(self):
        return self.__values.pop()

    def size(self):
        return len(self.__values)

    def values(self):
        return self.__values


class _PathStack:

    def __init__(self, vertex):
        self.__stack = _Stack()
        self.__vertex = vertex
        self.__is_new_top = False
        for v in self.__vertex:
            if v is not None:
                v.Hint = False

    def push(self, index):
        self.__stack.push(index)
        self.__vertex[index].Hint = True
        self.__is_new_top = True

    def peek(self):
        return self.__stack.peek()

    def pop(self):
        self.__is_new_top = False
        self.__stack.pop()

    def is_new_top(self):
        return self.__is_new_top

    def is_empty(self):
        return self.__stack.size() == 0

    def path(self):
        return [self.__vertex[i] for i in self.__stack.values()]
