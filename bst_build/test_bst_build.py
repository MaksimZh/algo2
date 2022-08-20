import unittest

from bst_build import GenerateBBSTArray


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(GenerateBBSTArray([]), [])
        
        self.assertEqual(GenerateBBSTArray([20]), [20])

        self.assertEqual(GenerateBBSTArray([20, 10]), [
            20,
            10, None
        ])
        
        self.assertEqual(GenerateBBSTArray([20, 10, 30]), [
            20,
            10, 30
        ])

        self.assertEqual(GenerateBBSTArray([20, 10, 30, 5]), [
            20,
            10, 30,
            5, None, None, None
        ])

        self.assertEqual(GenerateBBSTArray([20, 10, 30, 5, 15]), [
            15,
            10, 30,
            5, None, 20, None
        ])

        self.assertEqual(GenerateBBSTArray([20, 10, 30, 5, 15, 25]), [
            20,
            10, 30,
            5, 15, 25, None
        ])

        self.assertEqual(GenerateBBSTArray([20, 10, 30, 5, 15, 25, 7]), [
            15,
            7, 25,
            5, 10, 20, 30
        ])

        self.assertEqual(GenerateBBSTArray([20, 10, 30, 5, 15, 25, 7, 17]), [
            17,
            10, 25,
            7, 15, 20, 30,
            5, None, None, None, None, None, None, None,
        ])

        self.assertEqual(GenerateBBSTArray([20, 10, 30, 5, 15, 25, 7, 17, 22]), [
            17,
            10, 25,
            7, 15, 22, 30,
            5, None, None, None, 20, None, None, None,
        ])


if __name__ == "__main__":
    unittest.main()
