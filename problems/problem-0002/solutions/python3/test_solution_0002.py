import unittest

import linkedlist

from solution_0002 import Solution


class TestSolution0002(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_sum_of_243_and_564(self):
        input1: ListNode = linkedlist.create([2, 4, 3])
        input2: ListNode = linkedlist.create([5, 6, 4])
        output: ListNode = linkedlist.create([7, 0, 8])

        self.assertTrue(linkedlist.are_equal(self.solution.addTwoNumbers(input1, input2), output))

    def test_sum_of_0_and_0(self):
        input1: ListNode = linkedlist.create([0])
        input2: ListNode = linkedlist.create([0])
        output: ListNode = linkedlist.create([0])

        self.assertTrue(linkedlist.are_equal(self.solution.addTwoNumbers(input1, input2), output))

    def test_sum_of_9999999_and_9999(self):
        input1: ListNode = linkedlist.create([9, 9, 9, 9, 9, 9, 9])
        input2: ListNode = linkedlist.create([9, 9, 9, 9])
        output: ListNode = linkedlist.create([8, 9, 9, 9, 0, 0, 0, 1])

        self.assertTrue(linkedlist.are_equal(self.solution.addTwoNumbers(input1, input2), output))


if __name__ == "__main__":
    unittest.main()
