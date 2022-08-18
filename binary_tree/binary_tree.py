class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:

    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key):
        if self.Root is None:
            return BSTFind()
        else:
            return _find(self.Root, key)

    def AddKeyValue(self, key, val):
        f = self.FindNodeByKey(key)
        if f.Node is None:
            self.Root = BSTNode(key, val, None)
            return True
        elif f.NodeHasKey:
            return False
        elif f.ToLeft:
            f.Node.LeftChild = BSTNode(key, val, f.Node)
            return True
        else:
            f.Node.RightChild = BSTNode(key, val, f.Node)
            return True

    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        return None

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        return False # если узел не найден

    def Count(self):
        return 0 # количество узлов в дереве


def _find(node, key):
    if key == node.NodeKey:
        f = BSTFind()
        f.Node = node
        f.NodeHasKey = True
        return f
    elif key < node.NodeKey:
        return _find_left(node, key)
    else:
        return _find_right(node, key)

def _find_left(node, key):
    if node.LeftChild is None:
        f = BSTFind()
        f.Node = node
        f.NodeHasKey = False
        f.ToLeft = True
        return f
    else:
        return _find(node.LeftChild, key)

def _find_right(node, key):
    if node.RightChild is None:
        f = BSTFind()
        f.Node = node
        f.NodeHasKey = False
        f.ToLeft = False
        return f
    else:
        return _find(node.RightChild, key)
