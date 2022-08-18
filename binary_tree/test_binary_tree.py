import unittest

from binary_tree import BST, BSTNode, BSTFind


class Test(unittest.TestCase):

    def check_subtree(self, node, pattern):
        self.assertEqual(node.NodeKey, pattern[0])
        self.assertEqual(node.NodeValue, pattern[1])
        for pat, child in zip(pattern[2:], (node.LeftChild, node.RightChild)):
            if pat is None:
                self.assertIsNone(child)
            else:
                self.assertIs(child.Parent, node)
                self.check_subtree(child, pat)
    
    def check_tree(self, tree, pattern):
        if pattern is None:
            self.assertIsNone(tree.Root)
        else:
            self.assertIs(tree.Root.Parent, None)
            self.check_subtree(tree.Root, pattern)

    def check_found(self, f, key):
        self.assertIsNotNone(f.Node)
        self.assertEqual(f.Node.NodeKey, key)
        self.assertTrue(f.NodeHasKey)
        self.assertFalse(f.ToLeft)

    def check_found_left(self, f, parent_key):
        self.assertIsNotNone(f.Node)
        self.assertEqual(f.Node.NodeKey, parent_key)
        self.assertFalse(f.NodeHasKey)
        self.assertTrue(f.ToLeft)

    def check_found_right(self, f, parent_key):
        self.assertIsNotNone(f.Node)
        self.assertEqual(f.Node.NodeKey, parent_key)
        self.assertFalse(f.NodeHasKey)
        self.assertFalse(f.ToLeft)

    def test_add(self):
        bst = BST(None)
        self.check_tree(bst, None)

        self.assertTrue(bst.AddKeyValue(10, "a"))
        self.check_tree(bst, (10, "a", None, None))

        self.assertFalse(bst.AddKeyValue(10, "aa"))
        self.check_tree(bst, (10, "a", None, None))

        self.assertTrue(bst.AddKeyValue(5, "b"))
        self.check_tree(bst,
            (10, "a",
                (5, "b", None, None),
                None,
            )
        )

        self.assertTrue(bst.AddKeyValue(7, "c"))
        self.check_tree(bst,
            (10, "a",
                (5, "b",
                    None,
                    (7, "c", None, None)
                ),
                None,
            )
        )

        self.assertTrue(bst.AddKeyValue(4, "d"))
        self.check_tree(bst,
            (10, "a",
                (5, "b",
                    (4, "d", None, None),
                    (7, "c", None, None)
                ),
                None,
            )
        )

        self.assertTrue(bst.AddKeyValue(15, "e"))
        self.check_tree(bst,
            (10, "a",
                (5, "b",
                    (4, "d", None, None),
                    (7, "c", None, None)
                ),
                (15, "e", None, None)
            ),
        )

        self.assertTrue(bst.AddKeyValue(13, "f"))
        self.check_tree(bst,
            (10, "a",
                (5, "b",
                    (4, "d", None, None),
                    (7, "c", None, None)
                ),
                (15, "e",
                    (13, "f", None, None),
                    None,
                )
            )
        )

        self.assertTrue(bst.AddKeyValue(11, "g"))
        self.check_tree(bst,
            (10, "a",
                (5, "b",
                    (4, "d", None, None),
                    (7, "c", None, None)
                ),
                (15, "e",
                    (13, "f",
                        (11, "g", None, None),
                        None,
                    ),
                    None,
                )
            )
        )
        
        self.assertTrue(bst.AddKeyValue(17, "h"))
        self.check_tree(bst,
            (10, "a",
                (5, "b",
                    (4, "d", None, None),
                    (7, "c", None, None)
                ),
                (15, "e",
                    (13, "f",
                        (11, "g", None, None),
                        None,
                    ),
                    (17, "h", None, None),
                )
            )
        )

        self.assertFalse(bst.AddKeyValue(4, "aa"))
        self.assertFalse(bst.AddKeyValue(5, "aa"))
        self.assertFalse(bst.AddKeyValue(7, "aa"))
        self.assertFalse(bst.AddKeyValue(10, "aa"))
        self.assertFalse(bst.AddKeyValue(11, "aa"))
        self.assertFalse(bst.AddKeyValue(13, "aa"))
        self.assertFalse(bst.AddKeyValue(15, "aa"))
        self.assertFalse(bst.AddKeyValue(17, "aa"))
        self.check_tree(bst,
            (10, "a",
                (5, "b",
                    (4, "d", None, None),
                    (7, "c", None, None)
                ),
                (15, "e",
                    (13, "f",
                        (11, "g", None, None),
                        None,
                    ),
                    (17, "h", None, None),
                )
            )
        )

    
    def test_find(self):
        bst = BST(None)
        self.check_tree(bst, None)
        f = bst.FindNodeByKey(10)
        self.assertIsNone(f.Node)
        self.assertFalse(f.NodeHasKey)
        self.assertFalse(f.ToLeft)

        bst.AddKeyValue(10, "a")
        bst.AddKeyValue(5, "b")
        bst.AddKeyValue(7, "c")
        bst.AddKeyValue(4, "d")
        bst.AddKeyValue(15, "e")
        bst.AddKeyValue(13, "f")
        bst.AddKeyValue(11, "g")
        bst.AddKeyValue(17, "h")
        self.check_tree(bst,
            (10, "a",
                (5, "b",
                    (4, "d", None, None),
                    (7, "c", None, None)
                ),
                (15, "e",
                    (13, "f",
                        (11, "g", None, None),
                        None,
                    ),
                    (17, "h", None, None),
                )
            )
        )

        self.check_found_left(bst.FindNodeByKey(1), 4)
        self.check_found_left(bst.FindNodeByKey(2), 4)
        self.check_found_left(bst.FindNodeByKey(3), 4)
        self.check_found(bst.FindNodeByKey(4), 4)
        self.check_found(bst.FindNodeByKey(5), 5)
        self.check_found_left(bst.FindNodeByKey(6), 7)
        self.check_found(bst.FindNodeByKey(7), 7)
        self.check_found_right(bst.FindNodeByKey(8), 7)
        self.check_found_right(bst.FindNodeByKey(9), 7)
        self.check_found(bst.FindNodeByKey(10), 10)
        self.check_found(bst.FindNodeByKey(11), 11)
        self.check_found_right(bst.FindNodeByKey(12), 11)
        self.check_found(bst.FindNodeByKey(13), 13)
        self.check_found_right(bst.FindNodeByKey(14), 13)
        self.check_found(bst.FindNodeByKey(15), 15)
        self.check_found_left(bst.FindNodeByKey(16), 17)
        self.check_found(bst.FindNodeByKey(17), 17)
        self.check_found_right(bst.FindNodeByKey(18), 17)
        self.check_found_right(bst.FindNodeByKey(19), 17)
        self.check_found_right(bst.FindNodeByKey(20), 17)


if __name__ == "__main__":
    unittest.main()
