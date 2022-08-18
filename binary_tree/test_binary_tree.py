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


    def test_min_max(self):
        bst = BST(None)
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

        n = bst.FinMinMax(bst.Root, False)
        self.assertEqual((n.NodeKey, n.NodeValue), (4, "d"))
        n = bst.FinMinMax(bst.Root, True)
        self.assertEqual((n.NodeKey, n.NodeValue), (17, "h"))
        
        start = bst.FindNodeByKey(15).Node
        n = bst.FinMinMax(start, False)
        self.assertEqual((n.NodeKey, n.NodeValue), (11, "g"))
        n = bst.FinMinMax(start, True)
        self.assertEqual((n.NodeKey, n.NodeValue), (17, "h"))

        start = bst.FindNodeByKey(7).Node
        n = bst.FinMinMax(start, False)
        self.assertEqual((n.NodeKey, n.NodeValue), (7, "c"))
        n = bst.FinMinMax(start, True)
        self.assertEqual((n.NodeKey, n.NodeValue), (7, "c"))


    def test_delete_only(self):
        bst = BST(None)
        self.assertFalse(bst.DeleteNodeByKey(10))
        
        bst.AddKeyValue(10, "a")
        self.assertTrue(bst.DeleteNodeByKey(10))
        self.check_tree(bst, None)

    def test_delete_left_leaf(self):
        bst = BST(None)
        bst.AddKeyValue(10, "a")
        bst.AddKeyValue(5, "b")
        bst.AddKeyValue(15, "c")
        
        self.assertTrue(bst.DeleteNodeByKey(5))
        self.check_tree(bst,
            (10, "a",
                None,
                (15, "c", None),
            )
        )

    def test_delete_right_leaf(self):
        bst = BST(None)
        bst.AddKeyValue(10, "a")
        bst.AddKeyValue(5, "b")
        bst.AddKeyValue(15, "c")
        
        self.assertTrue(bst.DeleteNodeByKey(15))
        self.check_tree(bst,
            (10, "a",
                (5, "b", None),
                None,
            )
        )

    def test_delete_root_left(self):
        bst = BST(None)
        bst.AddKeyValue(10, "a")
        bst.AddKeyValue(5, "b")
        bst.AddKeyValue(4, "c")
        bst.AddKeyValue(6, "d")
        
        self.assertTrue(bst.DeleteNodeByKey(10))
        self.check_tree(bst,
            (5, "b",
                (4, "c", None),
                (6, "d", None),
            )
        )

    def test_delete_root_right(self):
        bst = BST(None)
        bst.AddKeyValue(10, "a")
        bst.AddKeyValue(15, "b")
        bst.AddKeyValue(14, "c")
        bst.AddKeyValue(16, "d")
        
        self.assertTrue(bst.DeleteNodeByKey(10))
        self.check_tree(bst,
            (15, "b",
                (14, "c", None),
                (16, "d", None),
            )
        )

    def test_delete_root_next(self):
        bst = BST(None)
        bst.AddKeyValue(10, "a")
        bst.AddKeyValue(5, "b")
        bst.AddKeyValue(15, "c")
        bst.AddKeyValue(4, "d")
        bst.AddKeyValue(6, "e")
        bst.AddKeyValue(17, "f")
        bst.AddKeyValue(16, "g")
        bst.AddKeyValue(18, "h")
        self.check_tree(bst,
            (10, "a",
                (5, "b",
                    (4, "d", None, None),
                    (6, "e", None, None),
                ),
                (15, "c",
                    None,
                    (17, "f",
                        (16, "g", None, None),
                        (18, "h", None, None),
                    ),
                ),
            )
        )

        self.assertTrue(bst.DeleteNodeByKey(10))
        self.check_tree(bst,
            (15, "c",
                (5, "b",
                    (4, "d", None, None),
                    (6, "e", None, None),
                ),
                (17, "f",
                    (16, "g", None, None),
                    (18, "h", None, None),
                ),
            )
        )

    def test_delete_root(self):
        bst = BST(None)
        bst.AddKeyValue(10, "a")
        bst.AddKeyValue(5, "b")
        bst.AddKeyValue(15, "c")
        bst.AddKeyValue(4, "d")
        bst.AddKeyValue(6, "e")
        bst.AddKeyValue(13, "f")
        bst.AddKeyValue(17, "g")
        bst.AddKeyValue(12, "h")
        bst.AddKeyValue(14, "i")
        bst.AddKeyValue(16, "j")
        bst.AddKeyValue(18, "k")
        self.check_tree(bst,
            (10, "a",
                (5, "b",
                    (4, "d", None, None),
                    (6, "e", None, None),
                ),
                (15, "c",
                    (13, "f",
                        (12, "h", None, None),
                        (14, "i", None, None),
                    ),
                    (17, "g",
                        (16, "j", None, None),
                        (18, "k", None, None),
                    ),
                ),
            )
        )

        self.assertTrue(bst.DeleteNodeByKey(10))
        self.check_tree(bst,
            (12, "h",
                (5, "b",
                    (4, "d", None, None),
                    (6, "e", None, None),
                ),
                (15, "c",
                    (13, "f",
                        None,
                        (14, "i", None, None),
                    ),
                    (17, "g",
                        (16, "j", None, None),
                        (18, "k", None, None),
                    ),
                ),
            )
        )

    def test_delete_root_mid(self):
        bst = BST(None)
        bst.AddKeyValue(10, "a")
        bst.AddKeyValue(5, "b")
        bst.AddKeyValue(15, "c")
        bst.AddKeyValue(4, "d")
        bst.AddKeyValue(6, "e")
        bst.AddKeyValue(13, "f")
        bst.AddKeyValue(17, "g")
        bst.AddKeyValue(14, "i")
        bst.AddKeyValue(16, "j")
        bst.AddKeyValue(18, "k")
        self.check_tree(bst,
            (10, "a",
                (5, "b",
                    (4, "d", None, None),
                    (6, "e", None, None),
                ),
                (15, "c",
                    (13, "f",
                        None,
                        (14, "i", None, None),
                    ),
                    (17, "g",
                        (16, "j", None, None),
                        (18, "k", None, None),
                    ),
                ),
            )
        )

        self.assertTrue(bst.DeleteNodeByKey(10))
        self.check_tree(bst,
            (13, "f",
                (5, "b",
                    (4, "d", None, None),
                    (6, "e", None, None),
                ),
                (15, "c",
                    (14, "i", None, None),
                    (17, "g",
                        (16, "j", None, None),
                        (18, "k", None, None),
                    ),
                ),
            )
        )
        

    def test_delete_left_left(self):
        bst = BST(None)
        bst.AddKeyValue(10, "a")
        bst.AddKeyValue(5, "b")
        bst.AddKeyValue(15, "c")
        bst.AddKeyValue(3, "d")
        bst.AddKeyValue(2, "e")
        bst.AddKeyValue(4, "f")
        
        self.assertTrue(bst.DeleteNodeByKey(5))
        self.check_tree(bst,
            (10, "a",
                (3, "d",
                    (2, "e", None),
                    (4, "f", None),
                ),
                (15, "c", None),
            )
        )

    def test_delete_left_right(self):
        bst = BST(None)
        bst.AddKeyValue(10, "a")
        bst.AddKeyValue(5, "b")
        bst.AddKeyValue(15, "c")
        bst.AddKeyValue(7, "d")
        bst.AddKeyValue(6, "e")
        bst.AddKeyValue(8, "f")
        
        self.assertTrue(bst.DeleteNodeByKey(5))
        self.check_tree(bst,
            (10, "a",
                (7, "d",
                    (6, "e", None),
                    (8, "f", None),
                ),
                (15, "c", None),
            )
        )

    def test_delete_left_next(self):
        bst = BST(None)
        bst.AddKeyValue(10, "a")
        bst.AddKeyValue(4, "b")
        bst.AddKeyValue(15, "c")
        bst.AddKeyValue(2, "d")
        bst.AddKeyValue(5, "e")
        bst.AddKeyValue(1, "f")
        bst.AddKeyValue(3, "g")
        bst.AddKeyValue(7, "h")
        bst.AddKeyValue(6, "i")
        bst.AddKeyValue(8, "j")
        self.check_tree(bst,
            (10, "a",
                (4, "b",
                    (2, "d",
                        (1, "f", None, None),
                        (3, "g", None, None),
                    ),
                    (5, "e",
                        None,
                        (7, "h",
                            (6, "i", None, None),
                            (8, "j", None, None),
                        ),
                    ),
                ),
                (15, "c", None, None),
            )
        )
        
        self.assertTrue(bst.DeleteNodeByKey(4))
        self.check_tree(bst,
            (10, "a",
                (5, "e",
                    (2, "d",
                        (1, "f", None, None),
                        (3, "g", None, None),
                    ),
                    (7, "h",
                        (6, "i", None, None),
                        (8, "j", None, None),
                    ),
                ),
                (15, "c", None, None),
            )
        )

    def test_delete_left(self):
        bst = BST(None)
        bst.AddKeyValue(20, "a")
        bst.AddKeyValue(10, "b")
        bst.AddKeyValue(30, "c")
        bst.AddKeyValue(5, "d")
        bst.AddKeyValue(15, "e")
        bst.AddKeyValue(2, "f")
        bst.AddKeyValue(7, "g")
        bst.AddKeyValue(12, "h")
        bst.AddKeyValue(17, "i")
        self.check_tree(bst,
            (20, "a",
                (10, "b",
                    (5, "d",
                        (2, "f", None, None),
                        (7, "g", None, None),
                    ),
                    (15, "e",
                        (12, "h", None, None),
                        (17, "i", None, None),
                    ),
                ),
                (30, "c", None, None),
            )
        )

        self.assertTrue(bst.DeleteNodeByKey(10))
        self.check_tree(bst,
            (20, "a",
                (12, "h",
                    (5, "d",
                        (2, "f", None, None),
                        (7, "g", None, None),
                    ),
                    (15, "e",
                        None,
                        (17, "i", None, None),
                    ),
                ),
                (30, "c", None, None),
            )
        )

    def test_delete_left_mid(self):
        bst = BST(None)
        bst.AddKeyValue(20, "a")
        bst.AddKeyValue(10, "b")
        bst.AddKeyValue(30, "c")
        bst.AddKeyValue(5, "d")
        bst.AddKeyValue(15, "e")
        bst.AddKeyValue(2, "f")
        bst.AddKeyValue(7, "g")
        bst.AddKeyValue(12, "h")
        bst.AddKeyValue(17, "i")
        bst.AddKeyValue(14, "j")
        self.check_tree(bst,
            (20, "a",
                (10, "b",
                    (5, "d",
                        (2, "f", None, None),
                        (7, "g", None, None),
                    ),
                    (15, "e",
                        (12, "h",
                            None,
                            (14, "j", None, None),
                        ),
                        (17, "i", None, None),
                    ),
                ),
                (30, "c", None, None),
            )
        )

        self.assertTrue(bst.DeleteNodeByKey(10))
        self.check_tree(bst,
            (20, "a",
                (12, "h",
                    (5, "d",
                        (2, "f", None, None),
                        (7, "g", None, None),
                    ),
                    (15, "e",
                        (14, "j", None, None),
                        (17, "i", None, None),
                    ),
                ),
                (30, "c", None, None),
            )
        )

    def test_delete_right_left(self):
        bst = BST(None)
        bst.AddKeyValue(10, "a")
        bst.AddKeyValue(5, "b")
        bst.AddKeyValue(15, "c")
        bst.AddKeyValue(13, "d")
        bst.AddKeyValue(12, "e")
        bst.AddKeyValue(14, "f")
        
        self.assertTrue(bst.DeleteNodeByKey(15))
        self.check_tree(bst,
            (10, "a",
                (5, "b", None),
                (13, "d",
                    (12, "e", None),
                    (14, "f", None),
                ),
            )
        )

    def test_delete_right_right(self):
        bst = BST(None)
        bst.AddKeyValue(10, "a")
        bst.AddKeyValue(5, "b")
        bst.AddKeyValue(15, "c")
        bst.AddKeyValue(17, "d")
        bst.AddKeyValue(16, "e")
        bst.AddKeyValue(18, "f")
        
        self.assertTrue(bst.DeleteNodeByKey(15))
        self.check_tree(bst,
            (10, "a",
                (5, "b", None),
                (17, "d",
                    (16, "e", None),
                    (18, "f", None),
                ),
            )
        )

    def test_delete_right_next(self):
        bst = BST(None)
        bst.AddKeyValue(10, "a")
        bst.AddKeyValue(5, "b")
        bst.AddKeyValue(15, "c")
        bst.AddKeyValue(13, "d")
        bst.AddKeyValue(16, "e")
        bst.AddKeyValue(12, "f")
        bst.AddKeyValue(14, "g")
        bst.AddKeyValue(18, "h")
        bst.AddKeyValue(17, "i")
        bst.AddKeyValue(19, "j")
        self.check_tree(bst,
            (10, "a",
                (5, "b", None, None),
                (15, "c",
                    (13, "d",
                        (12, "f", None, None),
                        (14, "g", None, None),
                    ),
                    (16, "e",
                        None,
                        (18, "h",
                            (17, "i", None, None),
                            (19, "j", None, None),
                        ),
                    ),
                ),
            )
        )
        
        self.assertTrue(bst.DeleteNodeByKey(15))
        self.check_tree(bst,
            (10, "a",
                (5, "b", None, None),
                (16, "e",
                    (13, "d",
                        (12, "f", None, None),
                        (14, "g", None, None),
                    ),
                    (18, "h",
                        (17, "i", None, None),
                        (19, "j", None, None),
                    ),
                ),
            )
        )

    def test_delete_right(self):
        bst = BST(None)
        bst.AddKeyValue(10, "a")
        bst.AddKeyValue(5, "b")
        bst.AddKeyValue(15, "c")
        bst.AddKeyValue(13, "d")
        bst.AddKeyValue(17, "e")
        bst.AddKeyValue(12, "f")
        bst.AddKeyValue(14, "g")
        bst.AddKeyValue(16, "h")
        bst.AddKeyValue(18, "i")
        self.check_tree(bst,
            (10, "a",
                (5, "b", None, None),
                (15, "c",
                    (13, "d",
                        (12, "f", None, None),
                        (14, "g", None, None),
                    ),
                    (17, "e",
                        (16, "h", None, None),
                        (18, "i", None, None),
                    ),
                ),
            )
        )
        
        self.assertTrue(bst.DeleteNodeByKey(15))
        self.check_tree(bst,
            (10, "a",
                (5, "b", None, None),
                (16, "h",
                    (13, "d",
                        (12, "f", None, None),
                        (14, "g", None, None),
                    ),
                    (17, "e",
                        None,
                        (18, "i", None, None),
                    ),
                ),
            )
        )

    def test_delete_right_mid(self):
        bst = BST(None)
        bst.AddKeyValue(10, "a")
        bst.AddKeyValue(5, "b")
        bst.AddKeyValue(15, "c")
        bst.AddKeyValue(13, "d")
        bst.AddKeyValue(18, "e")
        bst.AddKeyValue(12, "f")
        bst.AddKeyValue(14, "g")
        bst.AddKeyValue(16, "h")
        bst.AddKeyValue(19, "i")
        bst.AddKeyValue(17, "j")
        self.check_tree(bst,
            (10, "a",
                (5, "b", None, None),
                (15, "c",
                    (13, "d",
                        (12, "f", None, None),
                        (14, "g", None, None),
                    ),
                    (18, "e",
                        (16, "h",
                            None,
                            (17, "j", None, None),
                        ),
                        (19, "i", None, None),
                    ),
                ),
            )
        )
        
        self.assertTrue(bst.DeleteNodeByKey(15))
        self.check_tree(bst,
            (10, "a",
                (5, "b", None, None),
                (16, "h",
                    (13, "d",
                        (12, "f", None, None),
                        (14, "g", None, None),
                    ),
                    (18, "e",
                        (17, "j", None, None),
                        (19, "i", None, None),
                    ),
                ),
            )
        )

    def test_count(self):
        bst = BST(None)
        self.assertEqual(bst.Count(), 0)
        
        bst.AddKeyValue(10, "a")
        self.assertEqual(bst.Count(), 1)
        
        bst.AddKeyValue(5, "b")
        self.assertEqual(bst.Count(), 2)
        
        bst.AddKeyValue(15, "c")
        self.assertEqual(bst.Count(), 3)
        
        bst.AddKeyValue(13, "d")
        self.assertEqual(bst.Count(), 4)
        
        bst.AddKeyValue(18, "e")
        self.assertEqual(bst.Count(), 5)
        
        bst.AddKeyValue(12, "f")
        self.assertEqual(bst.Count(), 6)
        
        bst.AddKeyValue(14, "g")
        self.assertEqual(bst.Count(), 7)
        
        bst.AddKeyValue(16, "h")
        self.assertEqual(bst.Count(), 8)
        
        bst.AddKeyValue(19, "i")
        self.assertEqual(bst.Count(), 9)
        
        bst.AddKeyValue(17, "j")
        self.assertEqual(bst.Count(), 10)
        

if __name__ == "__main__":
    unittest.main()
