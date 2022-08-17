import unittest

from tree import SimpleTree, SimpleTreeNode

class Test(unittest.TestCase):

    def check_subtree(self, root, pattern):
        self.assertIs(root, pattern[0])
        self.assertEqual(len(root.Children), len(pattern[1]))
        for p in pattern[1]:
            self.assertTrue(p[0] in root.Children)
            self.assertIs(p[0].Parent, root)
            self.check_subtree(p[0], p)

    def check_tree(self, tree, pattern):
        if pattern == ():
            self.assertIsNone(tree.Root)
        else:
            self.assertIsNone(tree.Root.Parent)
            self.check_subtree(tree.Root, pattern)


    def test_add(self):
        t = SimpleTree(None)
        self.check_tree(t, ())

        n1 = SimpleTreeNode(1, None)
        t.AddChild(None, n1)
        self.check_tree(t, (n1, []))

        n2 = SimpleTreeNode(2, None)
        t.AddChild(n1, n2)
        self.check_tree(t, (n1, [(n2, [])]))

        n3 = SimpleTreeNode(3, None)
        t.AddChild(n2, n3)
        self.check_tree(t, (n1, [(n2, [(n3, [])])]))

        n4 = SimpleTreeNode(3, None)
        t.AddChild(n1, n4)
        self.check_tree(t, (n1, [(n2, [(n3, [])]), (n4, [])]))


    def test_delete(self):
        n1 = SimpleTreeNode(1, None)
        t = SimpleTree(n1)
        n2 = SimpleTreeNode(2, None)
        t.AddChild(n1, n2)
        n3 = SimpleTreeNode(3, None)
        t.AddChild(n1, n3)
        n4 = SimpleTreeNode(4, None)
        t.AddChild(n2, n4)
        n5 = SimpleTreeNode(5, None)
        t.AddChild(n2, n5)
        n6 = SimpleTreeNode(6, None)
        t.AddChild(n1, n6)
        n7 = SimpleTreeNode(7, None)
        t.AddChild(n1, n7)
        n8 = SimpleTreeNode(8, None)
        t.AddChild(n7, n8)
        n9 = SimpleTreeNode(9, None)
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
        t = SimpleTree(None)
        self.assertEqual(t.GetAllNodes(), [])
        
        n1 = SimpleTreeNode(1, None)
        t = SimpleTree(n1)
        n2 = SimpleTreeNode(2, None)
        t.AddChild(n1, n2)
        n3 = SimpleTreeNode(3, None)
        t.AddChild(n1, n3)
        n4 = SimpleTreeNode(4, None)
        t.AddChild(n2, n4)
        n5 = SimpleTreeNode(5, None)
        t.AddChild(n2, n5)
        n6 = SimpleTreeNode(6, None)
        t.AddChild(n1, n6)
        n7 = SimpleTreeNode(7, None)
        t.AddChild(n1, n7)
        n8 = SimpleTreeNode(8, None)
        t.AddChild(n7, n8)
        n9 = SimpleTreeNode(9, None)
        t.AddChild(n7, n9)
        
        self.assertEqual(
            set(t.GetAllNodes()),
            set([n1, n2, n3, n4, n5, n6, n7, n8, n9]))


    def test_find(self):
        n1 = SimpleTreeNode(1, None)
        t = SimpleTree(n1)
        n2 = SimpleTreeNode(2, None)
        t.AddChild(n1, n2)
        n3 = SimpleTreeNode(42, None)
        t.AddChild(n1, n3)
        n4 = SimpleTreeNode(4, None)
        t.AddChild(n2, n4)
        n5 = SimpleTreeNode(42, None)
        t.AddChild(n2, n5)
        n6 = SimpleTreeNode(6, None)
        t.AddChild(n1, n6)
        n7 = SimpleTreeNode(42, None)
        t.AddChild(n1, n7)
        n8 = SimpleTreeNode(8, None)
        t.AddChild(n7, n8)
        n9 = SimpleTreeNode(42, None)
        t.AddChild(n7, n9)
        
        self.assertEqual(
            t.FindNodesByValue(0),
            [])
        self.assertEqual(
            set(t.FindNodesByValue(42)),
            set([n3, n5, n7, n9]))


    def test_move(self):
        n1 = SimpleTreeNode(1, None)
        t = SimpleTree(n1)
        n2 = SimpleTreeNode(2, None)
        t.AddChild(n1, n2)
        n3 = SimpleTreeNode(3, None)
        t.AddChild(n1, n3)
        n4 = SimpleTreeNode(4, None)
        t.AddChild(n2, n4)
        n5 = SimpleTreeNode(5, None)
        t.AddChild(n2, n5)
        n6 = SimpleTreeNode(6, None)
        t.AddChild(n1, n6)
        n7 = SimpleTreeNode(7, None)
        t.AddChild(n1, n7)
        n8 = SimpleTreeNode(8, None)
        t.AddChild(n7, n8)
        n9 = SimpleTreeNode(9, None)
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
        t = SimpleTree(None)
        self.assertEqual(t.Count(), 0)
        self.assertEqual(t.LeafCount(), 0)

        n1 = SimpleTreeNode(1, None)
        t.AddChild(None, n1)
        self.assertEqual(t.Count(), 1)
        self.assertEqual(t.LeafCount(), 1)

        n2 = SimpleTreeNode(2, None)
        t.AddChild(n1, n2)
        self.assertEqual(t.Count(), 2)
        self.assertEqual(t.LeafCount(), 1)

        n3 = SimpleTreeNode(3, None)
        t.AddChild(n1, n3)
        self.assertEqual(t.Count(), 3)
        self.assertEqual(t.LeafCount(), 2)

        n4 = SimpleTreeNode(4, None)
        t.AddChild(n2, n4)
        self.assertEqual(t.Count(), 4)
        self.assertEqual(t.LeafCount(), 2)

        n5 = SimpleTreeNode(5, None)
        t.AddChild(n2, n5)
        self.assertEqual(t.Count(), 5)
        self.assertEqual(t.LeafCount(), 3)

        n6 = SimpleTreeNode(6, None)
        t.AddChild(n1, n6)
        self.assertEqual(t.Count(), 6)
        self.assertEqual(t.LeafCount(), 4)

        n7 = SimpleTreeNode(7, None)
        t.AddChild(n1, n7)
        self.assertEqual(t.Count(), 7)
        self.assertEqual(t.LeafCount(), 5)

        n8 = SimpleTreeNode(8, None)
        t.AddChild(n7, n8)
        self.assertEqual(t.Count(), 8)
        self.assertEqual(t.LeafCount(), 5)

        n9 = SimpleTreeNode(9, None)
        t.AddChild(n7, n9)
        self.assertEqual(t.Count(), 9)
        self.assertEqual(t.LeafCount(), 6)


if __name__ == "__main__":
    unittest.main()
