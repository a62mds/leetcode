from typing import List
import unittest

from solution_0001 import Solution


class TestSolution0001(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_indices_of_numbers_that_add_to_9_in_2_7_11_15_are_0_1(self):
        inputs: List[int] = [2, 7, 11, 15]
        target: int = 9
        outputs: List[int] = [0, 1]

        self.assertEqual(self.solution.twoSum(inputs, target), outputs)

    def test_indices_of_numbers_that_add_to_6_in_3_2_4_are_1_2(self):
        inputs: List[int] = [3, 2, 4]
        target: int = 6
        outputs: List[int] = [1, 2]

        self.assertEqual(self.solution.twoSum(inputs, target), outputs)

    def test_indices_of_numbers_that_add_to_6_in_3_3_are_0_1(self):
        inputs: List[int] = [3, 3]
        target: int = 6
        outputs: List[int] = [0, 1]

        self.assertEqual(self.solution.twoSum(inputs, target), outputs)


if __name__ == "__main__":
    unittest.main()
