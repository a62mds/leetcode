from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited: Dict[int, int] = {}
        for index in range(len(nums)):
            if target - nums[index] in visited:
                return [visited[target - nums[index]], index]
            else:
                visited[nums[index]] = index
        return []
