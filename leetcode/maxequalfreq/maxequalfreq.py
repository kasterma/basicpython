# https://leetcode.com/problems/maximum-equal-frequency/
from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        return -1

def test1():
    nums = [2, 2, 1, 1, 5, 3, 3, 5]

    assert Solution().maxEqualFreq(nums) == 7

def test2():
    nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]
    assert Solution().maxEqualFreq(nums) == 13

def test3():
    nums = [1, 1, 1, 2, 2, 2]
    assert Solution().maxEqualFreq(nums) == 5

def test4():
    nums = [10, 2, 8, 9, 3, 8, 1, 5, 2, 3, 7, 6]
    assert Solution().maxEqualFreq(nums) == 8

