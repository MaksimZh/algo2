class BSTNode:
    
    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0
        
class BalancedBST:
        
    def __init__(self):
        self.Root = None

    def GenerateTree(self, a):
        sorted_array = sorted(a)
        self.Root = _build_tree(sorted_array, None, 0)

    def IsBalanced(self, root_node):
        return False

def _build_tree(sorted_array, parent, level):
    if len(sorted_array) == 0:
        return None
    mid = len(sorted_array) // 2
    node = BSTNode(sorted_array[mid], parent)
    node.Level = level
    node.LeftChild = _build_tree(sorted_array[:mid], node, level + 1)
    node.RightChild = _build_tree(sorted_array[mid + 1 :], node, level + 1)
    return node
