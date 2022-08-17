class SimpleTreeNode:
	
    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []
        self.level = 0


class SimpleTree:

    def __init__(self, root):
        self.Root = root


    def AddChild(self, ParentNode, NewChild):
        NewChild.Parent = ParentNode
        if ParentNode is None:
            self.Root = NewChild
            self.Root.level = 0
        else:
            ParentNode.Children.append(NewChild)
            NewChild.level = ParentNode.level + 1


    def DeleteNode(self, NodeToDelete):
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None


    def GetAllNodes(self):
        if self.Root is None:
            return []
        nodes = [self.Root]
        # breadth-first search is used intentionally instead of recursion
        i = 0
        while i < len(nodes):
            nodes += nodes[i].Children
            i += 1
        return nodes


    def FindNodesByValue(self, val):
        return [node for node in self.GetAllNodes() if node.NodeValue == val]


    def MoveNode(self, OriginalNode, NewParent):
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)
        _set_subtree_levels(OriginalNode, NewParent.level + 1)


    def Count(self):
        return len(self.GetAllNodes())


    def LeafCount(self):
        return len([node for node in self.GetAllNodes() if node.Children == []])

    def set_levels(self):
        if self.Root is not None:
            _set_subtree_levels(self.Root, 0)


def _set_subtree_levels(node, root_level):
    node.level = root_level
    for child in node.Children:
        _set_subtree_levels(child, root_level + 1)
