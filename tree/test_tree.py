import unittest


class Test(unittest.TestCase):

    def check_node(self, node, parent):
        self.assertTrue(node in parent.Children)
        self.assertIs(node.Parent, parent)

    def check_root(self, root):
        self.assertIsNone(root.Parent)

    def check_subtree(self, root, pattern):
        self.assertIs(root, pattern[0])
        self.assertEqual(len(root.Children), len(pattern[1]))
        for p in pattern[1]:
            self.check_node(p[0], root)
            self.check_subtree(p[0], p)

    def check_tree(self, tree, pattern):
        if pattern == ():
            self.assertIsNone(tree.Root)
        else:
            self.check_root(tree.Root)
            self.check_subtree(tree.Root, pattern)


    def test_add(self):
        t = self.Tree(None)
        self.check_tree(t, ())

        n1 = self.TreeNode(1, None)
        t.AddChild(None, n1)
        self.check_tree(t, (n1, []))

        n2 = self.TreeNode(2, None)
        t.AddChild(n1, n2)
        self.check_tree(t, (n1, [(n2, [])]))

        n3 = self.TreeNode(3, None)
        t.AddChild(n2, n3)
        self.check_tree(t, (n1, [(n2, [(n3, [])])]))

        n4 = self.TreeNode(3, None)
        t.AddChild(n1, n4)
        self.check_tree(t, (n1, [(n2, [(n3, [])]), (n4, [])]))


    def test_delete(self):
        n1 = self.TreeNode(1, None)
        t = self.Tree(n1)
        n2 = self.TreeNode(2, None)
        t.AddChild(n1, n2)
        n3 = self.TreeNode(3, None)
        t.AddChild(n1, n3)
        n4 = self.TreeNode(4, None)
        t.AddChild(n2, n4)
        n5 = self.TreeNode(5, None)
        t.AddChild(n2, n5)
        n6 = self.TreeNode(6, None)
        t.AddChild(n1, n6)
        n7 = self.TreeNode(7, None)
        t.AddChild(n1, n7)
        n8 = self.TreeNode(8, None)
        t.AddChild(n7, n8)
        n9 = self.TreeNode(9, None)
        t.AddChild(n7, n9)
        self.check_tree(t, (n1, [
            (n2, [
                (n4, []),
                (n5, []),
            ]),
            (n3, []),
            (n6, []),
            (n7, [
                (n8, []),
                (n9, []),
            ]),
        ]))
        
        t.DeleteNode(n6)
        self.assertIsNone(n6.Parent)
        self.check_tree(t, (n1, [
            (n2, [
                (n4, []),
                (n5, []),
            ]),
            (n3, []),
            (n7, [
                (n8, []),
                (n9, []),
            ]),
        ]))

        t.DeleteNode(n7)
        self.assertIsNone(n7.Parent)
        self.check_tree(t, (n1, [
            (n2, [
                (n4, []),
                (n5, []),
            ]),
            (n3, []),
        ]))


    def test_get(self):
        t = self.Tree(None)
        self.assertEqual(t.GetAllNodes(), [])
        
        n1 = self.TreeNode(1, None)
        t = self.Tree(n1)
        n2 = self.TreeNode(2, None)
        t.AddChild(n1, n2)
        n3 = self.TreeNode(3, None)
        t.AddChild(n1, n3)
        n4 = self.TreeNode(4, None)
        t.AddChild(n2, n4)
        n5 = self.TreeNode(5, None)
        t.AddChild(n2, n5)
        n6 = self.TreeNode(6, None)
        t.AddChild(n1, n6)
        n7 = self.TreeNode(7, None)
        t.AddChild(n1, n7)
        n8 = self.TreeNode(8, None)
        t.AddChild(n7, n8)
        n9 = self.TreeNode(9, None)
        t.AddChild(n7, n9)
        
        self.assertEqual(
            set(t.GetAllNodes()),
            set([n1, n2, n3, n4, n5, n6, n7, n8, n9]))


    def test_find(self):
        n1 = self.TreeNode(1, None)
        t = self.Tree(n1)
        n2 = self.TreeNode(2, None)
        t.AddChild(n1, n2)
        n3 = self.TreeNode(42, None)
        t.AddChild(n1, n3)
        n4 = self.TreeNode(4, None)
        t.AddChild(n2, n4)
        n5 = self.TreeNode(42, None)
        t.AddChild(n2, n5)
        n6 = self.TreeNode(6, None)
        t.AddChild(n1, n6)
        n7 = self.TreeNode(42, None)
        t.AddChild(n1, n7)
        n8 = self.TreeNode(8, None)
        t.AddChild(n7, n8)
        n9 = self.TreeNode(42, None)
        t.AddChild(n7, n9)
        
        self.assertEqual(
            t.FindNodesByValue(0),
            [])
        self.assertEqual(
            set(t.FindNodesByValue(42)),
            set([n3, n5, n7, n9]))


    def test_move(self):
        n1 = self.TreeNode(1, None)
        t = self.Tree(n1)
        n2 = self.TreeNode(2, None)
        t.AddChild(n1, n2)
        n3 = self.TreeNode(3, None)
        t.AddChild(n1, n3)
        n4 = self.TreeNode(4, None)
        t.AddChild(n2, n4)
        n5 = self.TreeNode(5, None)
        t.AddChild(n2, n5)
        n6 = self.TreeNode(6, None)
        t.AddChild(n1, n6)
        n7 = self.TreeNode(7, None)
        t.AddChild(n1, n7)
        n8 = self.TreeNode(8, None)
        t.AddChild(n7, n8)
        n9 = self.TreeNode(9, None)
        t.AddChild(n7, n9)
        self.check_tree(t, (n1, [
            (n2, [
                (n4, []),
                (n5, []),
            ]),
            (n3, []),
            (n6, []),
            (n7, [
                (n8, []),
                (n9, []),
            ]),
        ]))

        t.MoveNode(n6, n7)
        self.check_tree(t, (n1, [
            (n2, [
                (n4, []),
                (n5, []),
            ]),
            (n3, []),
            (n7, [
                (n6, []),
                (n8, []),
                (n9, []),
            ]),
        ]))

        t.MoveNode(n7, n5)
        self.check_tree(t, (n1, [
            (n2, [
                (n4, []),
                (n5, [
                    (n7, [
                        (n6, []),
                        (n8, []),
                        (n9, []),
                    ]),
                ]),
            ]),
            (n3, []),
        ]))

        t.MoveNode(n5, n1)
        self.check_tree(t, (n1, [
            (n2, [
                (n4, []),
            ]),
            (n3, []),
            (n5, [
                (n7, [
                    (n6, []),
                    (n8, []),
                    (n9, []),
                ]),
            ]),
        ]))

    
    def test_count(self):
        t = self.Tree(None)
        self.assertEqual(t.Count(), 0)
        self.assertEqual(t.LeafCount(), 0)

        n1 = self.TreeNode(1, None)
        t.AddChild(None, n1)
        self.assertEqual(t.Count(), 1)
        self.assertEqual(t.LeafCount(), 1)

        n2 = self.TreeNode(2, None)
        t.AddChild(n1, n2)
        self.assertEqual(t.Count(), 2)
        self.assertEqual(t.LeafCount(), 1)

        n3 = self.TreeNode(3, None)
        t.AddChild(n1, n3)
        self.assertEqual(t.Count(), 3)
        self.assertEqual(t.LeafCount(), 2)

        n4 = self.TreeNode(4, None)
        t.AddChild(n2, n4)
        self.assertEqual(t.Count(), 4)
        self.assertEqual(t.LeafCount(), 2)

        n5 = self.TreeNode(5, None)
        t.AddChild(n2, n5)
        self.assertEqual(t.Count(), 5)
        self.assertEqual(t.LeafCount(), 3)

        n6 = self.TreeNode(6, None)
        t.AddChild(n1, n6)
        self.assertEqual(t.Count(), 6)
        self.assertEqual(t.LeafCount(), 4)

        n7 = self.TreeNode(7, None)
        t.AddChild(n1, n7)
        self.assertEqual(t.Count(), 7)
        self.assertEqual(t.LeafCount(), 5)

        n8 = self.TreeNode(8, None)
        t.AddChild(n7, n8)
        self.assertEqual(t.Count(), 8)
        self.assertEqual(t.LeafCount(), 5)

        n9 = self.TreeNode(9, None)
        t.AddChild(n7, n9)
        self.assertEqual(t.Count(), 9)
        self.assertEqual(t.LeafCount(), 6)


import tree
class TestTree(Test):
    Tree = tree.SimpleTree
    TreeNode = tree.SimpleTreeNode

    def test_even_trees(self):
        t = self.Tree(None)
        self.assertEqual(t.EvenTrees(), [])

        n1 = self.TreeNode(1, None)
        t.AddChild(None, n1)
        self.assertEqual(t.EvenTrees(), [])

        n2 = self.TreeNode(2, None)
        t.AddChild(n1, n2)
        self.assertEqual(t.EvenTrees(), [])

        n3 = self.TreeNode(3, None)
        t.AddChild(n1, n3)
        self.assertEqual(t.EvenTrees(), [])

        n4 = self.TreeNode(4, None)
        t.AddChild(n3, n4)
        self.assertEqual(t.EvenTrees(), [n1, n3])

        n5 = self.TreeNode(5, None)
        t.AddChild(n2, n5)
        self.assertEqual(t.EvenTrees(), [])

        n6 = self.TreeNode(6, None)
        t.AddChild(n1, n6)
        et = t.EvenTrees()
        self.assertEqual(set(zip(et[0::2], et[1::2])), set([
            (n1, n2),
            (n1, n3),
        ]))

        n7 = self.TreeNode(7, None)
        t.AddChild(n2, n7)
        self.assertEqual(t.EvenTrees(), [])
        
        n8 = self.TreeNode(8, None)
        t.AddChild(n6, n8)
        et = t.EvenTrees()
        self.assertEqual(set(zip(et[0::2], et[1::2])), set([
            (n1, n3),
            (n1, n6),
        ]))

        n9 = self.TreeNode(9, None)
        t.AddChild(n8, n9)
        self.assertEqual(t.EvenTrees(), [])

        n10 = self.TreeNode(10, None)
        t.AddChild(n8, n10)
        et = t.EvenTrees()
        self.assertEqual(set(zip(et[0::2], et[1::2])), set([
            (n1, n3),
            (n1, n6),
        ]))

        n11 = self.TreeNode(11, None)
        t.AddChild(n4, n11)
        self.assertEqual(t.EvenTrees(), [])

        n12 = self.TreeNode(12, None)
        t.AddChild(n7, n12)
        et = t.EvenTrees()
        self.assertEqual(set(zip(et[0::2], et[1::2])), set([
            (n2, n7),
            (n3, n4),
            (n1, n2),
            (n1, n6),
        ]))


import tree_x
class TestTreeX(Test):
    Tree = tree_x.SimpleTree
    TreeNode = tree_x.SimpleTreeNode

    def check_node(self, node, parent):
        super().check_node(node, parent)
        self.assertEqual(node.level, parent.level + 1)

    def check_root(self, root):
        super().check_root(root)
        self.assertEqual(root.level, 0)

del Test


if __name__ == "__main__":
    unittest.main()
