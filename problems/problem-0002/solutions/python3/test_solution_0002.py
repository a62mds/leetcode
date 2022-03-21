import unittest

from solution_0002 import ListNode, Solution


class TestSolution0002(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_sum_of_243_and_564(self):
        input1: ListNode = ListNode.from_list([2, 4, 3])
        input2: ListNode = ListNode.from_list([5, 6, 4])
        output: ListNode = ListNode.from_list([7, 0, 8])

        self.assertEqual(self.solution.addTwoNumbers(input1, input2), output)

    def test_sum_of_0_and_0(self):
        input1: ListNode = ListNode.from_list([0])
        input2: ListNode = ListNode.from_list([0])
        output: ListNode = ListNode.from_list([0])

        self.assertEqual(self.solution.addTwoNumbers(input1, input2), output)

    def test_sum_of_9999999_and_9999(self):
        input1: ListNode = ListNode.from_list([9, 9, 9, 9, 9, 9, 9])
        input2: ListNode = ListNode.from_list([9, 9, 9, 9])
        output: ListNode = ListNode.from_list([8, 9, 9, 9, 0, 0, 0, 1])

        self.assertEqual(self.solution.addTwoNumbers(input1, input2), output)


if __name__ == "__main__":
    unittest.main()
