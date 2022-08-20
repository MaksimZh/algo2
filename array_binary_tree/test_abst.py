import unittest

from abst import aBST


class Test(unittest.TestCase):

    def test_add(self):
        t = aBST(4)
        self.assertEqual(t.Tree, [
            None,
            None, None,
            None, None, None, None,
            None, None, None, None, None, None, None, None])

        self.assertEqual(t.AddKey(20), 0)
        self.assertEqual(t.Tree, [
            20,
            None, None,
            None, None, None, None,
            None, None, None, None, None, None, None, None])

        self.assertEqual(t.AddKey(10), 1)
        self.assertEqual(t.Tree, [
            20,
            10, None,
            None, None, None, None,
            None, None, None, None, None, None, None, None])
        
        self.assertEqual(t.AddKey(30), 2)
        self.assertEqual(t.Tree, [
            20,
            10, 30,
            None, None, None, None,
            None, None, None, None, None, None, None, None])

        self.assertEqual(t.AddKey(15), 4)
        self.assertEqual(t.Tree, [
            20,
            10, 30,
            None, 15, None, None,
            None, None, None, None, None, None, None, None])

        self.assertEqual(t.AddKey(17), 10)
        self.assertEqual(t.Tree, [
            20,
            10, 30,
            None, 15, None, None,
            None, None, None, 17, None, None, None, None])

        self.assertEqual(t.AddKey(25), 5)
        self.assertEqual(t.Tree, [
            20,
            10, 30,
            None, 15, 25, None,
            None, None, None, 17, None, None, None, None])

        self.assertEqual(t.AddKey(22), 11)
        self.assertEqual(t.Tree, [
            20,
            10, 30,
            None, 15, 25, None,
            None, None, None, 17, 22, None, None, None])

        self.assertEqual(t.AddKey(5), 3)
        self.assertEqual(t.Tree, [
            20,
            10, 30,
            5, 15, 25, None,
            None, None, None, 17, 22, None, None, None])

        self.assertEqual(t.AddKey(7), 8)
        self.assertEqual(t.Tree, [
            20,
            10, 30,
            5, 15, 25, None,
            None, 7, None, 17, 22, None, None, None])

        self.assertEqual(t.AddKey(6), -1)
        self.assertEqual(t.AddKey(8), -1)
        self.assertEqual(t.AddKey(16), -1)
        self.assertEqual(t.AddKey(18), -1)
        self.assertEqual(t.AddKey(21), -1)
        self.assertEqual(t.AddKey(23), -1)
        self.assertEqual(t.Tree, [
            20,
            10, 30,
            5, 15, 25, None,
            None, 7, None, 17, 22, None, None, None])

    
    def test_find(self):
        t = aBST(4)
        t.AddKey(20)
        t.AddKey(10)
        t.AddKey(30)
        t.AddKey(15)
        t.AddKey(17)
        t.AddKey(25)
        t.AddKey(22)
        t.AddKey(5)
        t.AddKey(7)
        self.assertEqual(t.Tree, [
            20,
            10, 30,
            5, 15, 25, None,
            None, 7, None, 17, 22, None, None, None])
        
        self.assertIsNone(t.FindKeyIndex(6))
        self.assertIsNone(t.FindKeyIndex(8))
        self.assertIsNone(t.FindKeyIndex(16))
        self.assertIsNone(t.FindKeyIndex(18))
        self.assertIsNone(t.FindKeyIndex(21))
        self.assertIsNone(t.FindKeyIndex(23))

        self.assertEqual(t.FindKeyIndex(20), 0)
        self.assertEqual(t.FindKeyIndex(10), 1)
        self.assertEqual(t.FindKeyIndex(30), 2)
        self.assertEqual(t.FindKeyIndex(5), 3)
        self.assertEqual(t.FindKeyIndex(15), 4)
        self.assertEqual(t.FindKeyIndex(25), 5)
        self.assertEqual(t.FindKeyIndex(7), 8)
        self.assertEqual(t.FindKeyIndex(17), 10)
        self.assertEqual(t.FindKeyIndex(22), 11)

        self.assertEqual(t.FindKeyIndex(31), -6)
        self.assertEqual(t.FindKeyIndex(4), -7)
        self.assertEqual(t.FindKeyIndex(14), -9)
        self.assertEqual(t.FindKeyIndex(26), -12)


if __name__ == "__main__":
    unittest.main()
