import unittest

from balanced_bst import BalancedBST, BSTNode


class Test(unittest.TestCase):

    def check_tree(self, tree, pattern):
        self.check_subtree(None, tree.Root, 0, pattern)

    def check_subtree(self, parent, node, level, pattern):
        if pattern is None:
            self.assertIsNone(node)
            return
        self.assertIsNotNone(node)
        self.assertEqual(node.NodeKey, pattern[0])
        self.assertEqual(node.Parent, parent)
        self.assertEqual(node.Level, level)
        self.check_subtree(node, node.LeftChild, level + 1, pattern[1])
        self.check_subtree(node, node.RightChild, level + 1, pattern[2])

    def make_tree(self, pattern):
        root = self.make_subtree(None, 0, pattern)
        self.check_subtree(None, root, 0, pattern)
        return root

    def make_subtree(self, parent, level, pattern):
        if pattern is None:
            return None
        node = BSTNode(pattern[0], parent)
        node.Level = level
        node.LeftChild = self.make_subtree(node, level + 1, pattern[1])
        node.RightChild = self.make_subtree(node, level + 1, pattern[2])
        return node


    def test_generate(self):
        bst = BalancedBST()
        self.check_tree(bst, None)

        bst.GenerateTree([])
        self.check_tree(bst, None)

        bst.GenerateTree([20])
        self.check_tree(bst, (20, None, None))

        bst.GenerateTree([20, 10, 30, 5, 15, 25, 7, 17, 22])
        self.check_tree(bst, 
            (17,
                (10,
                    (7,
                        (5, None, None),
                        None,
                    ),
                    (15, None, None),
                ),
                (25,
                    (22,
                        (20, None, None),
                        None,
                    ),
                    (30, None, None),
                ),
            )
        )

    
    def test_is_balanced(self):
        bst = BalancedBST()
        
        self.assertTrue(bst.IsBalanced(self.make_tree(None)))
        
        self.assertTrue(bst.IsBalanced(self.make_tree((20, None, None))))

        self.assertTrue(bst.IsBalanced(self.make_tree(
            (17,
                (10,
                    (7,
                        (5, None, None),
                        None,
                    ),
                    (15, None, None),
                ),
                (25,
                    (22,
                        (20, None, None),
                        None,
                    ),
                    (30, None, None),
                ),
            )
        )))

        self.assertTrue(bst.IsBalanced(self.make_tree(
            (17,
                (10,
                    (7,
                        (5, None, None),
                        (8, None, None),
                    ),
                    (15, None, None),
                ),
                (25,
                    (22,
                        (20, None, None),
                        (23, None, None),
                    ),
                    (30, None, None),
                ),
            )
        )))

        self.assertFalse(bst.IsBalanced(self.make_tree(
            (17,
                (10,
                    (7,
                        (5, None, None),
                        None,
                    ),
                    None,
                ),
                (25,
                    (22,
                        (20, None, None),
                        None,
                    ),
                    (30, None, None),
                ),
            )
        )))

        self.assertFalse(bst.IsBalanced(self.make_tree(
            (17,
                (10,
                    (7,
                        (5, None, None),
                        None,
                    ),
                    (15, None, None),
                ),
                (25,
                    (22,
                        (20, None, None),
                        None,
                    ),
                    None,
                ),
            )
        )))


if __name__ == "__main__":
    unittest.main()
