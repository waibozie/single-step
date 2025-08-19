#!/bin/env python3

# question reference: https://leetcode.com/problems/two-sum/

from typing import List

import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


class TestSolution(unittest.TestCase):
    def test_twoSum(self):
        self.assertTrue(Solution().twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertTrue(Solution().twoSum([3, 2, 4], 6), [1, 2])
        self.assertTrue(Solution().twoSum([3, 3], 6), [0, 1])


if __name__ == "__main__":
    unittest.main()
