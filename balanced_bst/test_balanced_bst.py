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


if __name__ == "__main__":
    unittest.main()
