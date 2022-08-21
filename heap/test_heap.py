import unittest

from heap import Heap


class Test(unittest.TestCase):

    def test_make(self):
        h = Heap()
        self.assertEqual(h.HeapArray, [])

        h.MakeHeap([], 0)
        self.assertEqual(h.HeapArray, [None])
        h.MakeHeap([], 1)
        self.assertEqual(h.HeapArray, [None] * 3)
        h.MakeHeap([], 2)
        self.assertEqual(h.HeapArray, [None] * 7)
        h.MakeHeap([], 3)
        self.assertEqual(h.HeapArray, [None] * 15)

        h.MakeHeap([20], 3)
        self.assertEqual(h.HeapArray, [20] + [None] * 14)

        h.MakeHeap([20, 10], 3)
        self.assertEqual(h.HeapArray, [
            20,
            10, None,
            ] + [None] * 12)

        h.MakeHeap([20, 10, 30], 3)
        self.assertEqual(h.HeapArray, [
            30,
            10, 20,
            ] + [None] * 12)

        h.MakeHeap([20, 10, 30, 5], 3)
        self.assertEqual(h.HeapArray, [
            30,
            10, 20,
            5, None, None, None
            ] + [None] * 8)

        h.MakeHeap([20, 10, 30, 5, 15], 3)
        self.assertEqual(h.HeapArray, [
            30,
            15, 20,
            5, 10, None, None,
            ] + [None] * 8)

        h.MakeHeap([20, 10, 30, 5, 15, 25], 3)
        self.assertEqual(h.HeapArray, [
            30,
            15, 25,
            5, 10, 20, None,
            ] + [None] * 8)

        h.MakeHeap([20, 10, 30, 5, 15, 25, 7], 3)
        self.assertEqual(h.HeapArray, [
            30,
            15, 25,
            5, 10, 20, 7,
            ] + [None] * 8)

        h.MakeHeap([20, 10, 30, 5, 15, 25, 7, 17], 3)
        self.assertEqual(h.HeapArray, [
            30,
            17, 25,
            15, 10, 20, 7,
            5, None, None, None, None, None, None, None,
            ])

        h.MakeHeap([20, 10, 30, 5, 15, 25, 7, 17, 22], 3)
        self.assertEqual(h.HeapArray, [
            30,
            22, 25,
            17, 10, 20, 7,
            5, 15, None, None, None, None, None, None,
            ])

        h.MakeHeap([20, 10, 30, 5, 15, 25, 7, 17, 22, 35], 3)
        self.assertEqual(h.HeapArray, [
            35,
            30, 25,
            17, 22, 20, 7,
            5, 15, 10, None, None, None, None, None
            ])

        h.MakeHeap([20, 10, 30, 5, 15, 25, 7, 17, 22, 35, 33], 3)
        self.assertEqual(h.HeapArray, [
            35,
            33, 25,
            17, 30, 20, 7,
            5, 15, 10, 22, None, None, None, None
            ])

        h.MakeHeap([20, 10, 30, 5, 15, 25, 7, 17, 22, 35, 33, 31], 3)
        self.assertEqual(h.HeapArray, [
            35,
            33, 31,
            17, 30, 25, 7,
            5, 15, 10, 22, 20, None, None, None
            ])

        h.MakeHeap([20, 10, 30, 5, 15, 25, 7, 17, 22, 35, 33, 31, 37], 3)
        self.assertEqual(h.HeapArray, [
            37,
            33, 35,
            17, 30, 31, 7,
            5, 15, 10, 22, 20, 25, None, None
            ])

        h.MakeHeap([20, 10, 30, 5, 15, 25, 7, 17, 22, 35, 33, 31, 37, 1], 3)
        self.assertEqual(h.HeapArray, [
            37,
            33, 35,
            17, 30, 31, 7,
            5, 15, 10, 22, 20, 25, 1, None
            ])

        h.MakeHeap([20, 10, 30, 5, 15, 25, 7, 17, 22, 35, 33, 31, 37, 1, 40], 3)
        self.assertEqual(h.HeapArray, [
            40,
            33, 37,
            17, 30, 31, 35,
            5, 15, 10, 22, 20, 25, 1, 7
            ])


    def test_add(self):
        h = Heap()
        self.assertFalse(h.Add(20))
        h.MakeHeap([], 0)
        self.assertTrue(h.Add(20))
        self.assertEqual(h.HeapArray, [20])
        
        h.MakeHeap([], 3)
        self.assertTrue(h.Add(20))
        self.assertEqual(h.HeapArray, [20] + [None] * 14)
        self.assertTrue(h.Add(10))
        self.assertEqual(h.HeapArray, [
            20,
            10, None,
            ] + [None] * 12)
        self.assertTrue(h.Add(30))
        self.assertEqual(h.HeapArray, [
            30,
            10, 20,
            ] + [None] * 12)
        self.assertTrue(h.Add(5))
        self.assertEqual(h.HeapArray, [
            30,
            10, 20,
            5, None, None, None
            ] + [None] * 8)
        self.assertTrue(h.Add(15))
        self.assertEqual(h.HeapArray, [
            30,
            15, 20,
            5, 10, None, None,
            ] + [None] * 8)
        self.assertTrue(h.Add(25))
        self.assertEqual(h.HeapArray, [
            30,
            15, 25,
            5, 10, 20, None,
            ] + [None] * 8)
        self.assertTrue(h.Add(7))
        self.assertEqual(h.HeapArray, [
            30,
            15, 25,
            5, 10, 20, 7,
            ] + [None] * 8)
        self.assertTrue(h.Add(17))
        self.assertEqual(h.HeapArray, [
            30,
            17, 25,
            15, 10, 20, 7,
            5, None, None, None, None, None, None, None,
            ])
        self.assertTrue(h.Add(22))
        self.assertEqual(h.HeapArray, [
            30,
            22, 25,
            17, 10, 20, 7,
            5, 15, None, None, None, None, None, None,
            ])
        self.assertTrue(h.Add(35))
        self.assertEqual(h.HeapArray, [
            35,
            30, 25,
            17, 22, 20, 7,
            5, 15, 10, None, None, None, None, None
            ])
        self.assertTrue(h.Add(33))
        self.assertEqual(h.HeapArray, [
            35,
            33, 25,
            17, 30, 20, 7,
            5, 15, 10, 22, None, None, None, None
            ])
        self.assertTrue(h.Add(31))
        self.assertEqual(h.HeapArray, [
            35,
            33, 31,
            17, 30, 25, 7,
            5, 15, 10, 22, 20, None, None, None
            ])
        self.assertTrue(h.Add(37))
        self.assertEqual(h.HeapArray, [
            37,
            33, 35,
            17, 30, 31, 7,
            5, 15, 10, 22, 20, 25, None, None
            ])
        self.assertTrue(h.Add(1))
        self.assertEqual(h.HeapArray, [
            37,
            33, 35,
            17, 30, 31, 7,
            5, 15, 10, 22, 20, 25, 1, None
            ])
        self.assertTrue(h.Add(40))
        self.assertEqual(h.HeapArray, [
            40,
            33, 37,
            17, 30, 31, 35,
            5, 15, 10, 22, 20, 25, 1, 7
            ])
        self.assertFalse(h.Add(2))


    def test_get(self):
        h = Heap()
        self.assertEqual(h.GetMax(), -1)
        self.assertEqual(h.HeapArray, [])
        
        h.MakeHeap([], 0)
        self.assertEqual(h.GetMax(), -1)
        self.assertEqual(h.HeapArray, [None])
        
        h.Add(20)
        self.assertEqual(h.GetMax(), 20)
        self.assertEqual(h.HeapArray, [None])

        h.MakeHeap([20], 3)
        self.assertEqual(h.GetMax(), 20)
        self.assertEqual(h.HeapArray, [None] * 15)

        h.MakeHeap([20, 10, 30, 5, 15, 25, 7, 17, 22, 35, 33, 31, 37, 1, 40], 3)
        self.assertEqual(h.HeapArray, [
            40,
            33, 37,
            17, 30, 31, 35,
            5, 15, 10, 22, 20, 25, 1, 7
            ])
        self.assertEqual(h.GetMax(), 40)
        self.assertEqual(h.HeapArray, [
            37,
            33, 35,
            17, 30, 31, 7,
            5, 15, 10, 22, 20, 25, 1, None
            ])
        self.assertEqual(h.GetMax(), 37)
        self.assertEqual(h.HeapArray, [
            35,
            33, 31,
            17, 30, 25, 7,
            5, 15, 10, 22, 20, 1, None, None
            ])
        self.assertEqual(h.GetMax(), 35)
        self.assertEqual(h.HeapArray, [
            33,
            30, 31,
            17, 22, 25, 7,
            5, 15, 10, 1, 20, None, None, None
            ])
        self.assertEqual(h.GetMax(), 33)
        self.assertEqual(h.HeapArray, [
            31,
            30, 25,
            17, 22, 20, 7,
            5, 15, 10, 1, None, None, None, None
            ])
        self.assertEqual(h.GetMax(), 31)
        self.assertEqual(h.HeapArray, [
            30,
            22, 25,
            17, 10, 20, 7,
            5, 15, 1, None, None, None, None, None
            ])
        self.assertEqual(h.GetMax(), 30)
        self.assertEqual(h.HeapArray, [
            25,
            22, 20,
            17, 10, 1, 7,
            5, 15, None, None, None, None, None, None
            ])
        self.assertEqual(h.GetMax(), 25)
        self.assertEqual(h.HeapArray, [
            22,
            17, 20,
            15, 10, 1, 7,
            5, None, None, None, None, None, None, None
            ])
        self.assertEqual(h.GetMax(), 22)
        self.assertEqual(h.HeapArray, [
            20,
            17, 7,
            15, 10, 1, 5,
            ] + [None] * 8)
        self.assertEqual(h.GetMax(), 20)
        self.assertEqual(h.HeapArray, [
            17,
            15, 7,
            5, 10, 1, None,
            ] + [None] * 8)
        self.assertEqual(h.GetMax(), 17)
        self.assertEqual(h.HeapArray, [
            15,
            10, 7,
            5, 1, None, None,
            ] + [None] * 8)
        self.assertEqual(h.GetMax(), 15)
        self.assertEqual(h.HeapArray, [
            10,
            5, 7,
            1, None, None, None,
            ] + [None] * 8)
        self.assertEqual(h.GetMax(), 10)
        self.assertEqual(h.HeapArray, [
            7,
            5, 1,
            ] + [None] * 12)
        self.assertEqual(h.GetMax(), 7)
        self.assertEqual(h.HeapArray, [
            5,
            1, None,
            ] + [None] * 12)
        self.assertEqual(h.GetMax(), 5)
        self.assertEqual(h.HeapArray, [1] + [None] * 14)
        self.assertEqual(h.GetMax(), 1)
        self.assertEqual(h.HeapArray, [None] * 15)
        self.assertEqual(h.GetMax(), -1)
        self.assertEqual(h.HeapArray, [None] * 15)
        

if __name__ == "__main__":
    unittest.main()
