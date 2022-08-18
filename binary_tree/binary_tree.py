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
        if self.Root is None:
            self.Root = BSTNode(key, val, None)
            return True
        else:
            return _add(self.Root, key, val)

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

def _add(node, key, val):
    if key == node.NodeKey:
        return False
    elif key < node.NodeKey:
        return _add_left(node, key, val)
    else:
        return _add_right(node, key, val)

def _add_left(node, key, val):
    if node.LeftChild is None:
        node.LeftChild = BSTNode(key, val, node)
        return True
    else:
        return _add(node.LeftChild, key, val)

def _add_right(node, key, val):
    if node.RightChild is None:
        node.RightChild = BSTNode(key, val, node)
        return True
    else:
        return _add(node.RightChild, key, val)
