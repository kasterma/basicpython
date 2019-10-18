# https://leetcode.com/problems/maximum-equal-frequency/
#
# Notes:
# 1. The number of resubmissions needed corresponds exactly to the number of special cases not considered

from collections import Counter
from typing import List

class Solution:
    def __init__(self, debug=False):
        self.debug = debug

    def sol(self, c: Counter) -> bool:
        if self.debug:
            print(f"counter {c}")
        c_vals = Counter(c.values())
        if self.debug:
            print(f"c_vals {c_vals}")
        if len(c_vals) == 2:  # standard case to look for, two different counts appear
            a, b = c_vals.keys()
            if a > b:
                a, b = b, a
            if self.debug:
                print(f"a,b {a} {b}")
            if (a + 1 == b and c_vals[b] == 1) or (a == 1 and c_vals[a] == 1):
                if self.debug:
                    print("True")
                return True
        elif len(c_vals) == 1 and list(c.values())[0] == 1:  # every number occurs once
            return True
        elif len(c) == 1:  # only one number appears
            return True

        if self.debug:
            print("False")
        return False

    def maxEqualFreq(self, nums: List[int]) -> int:
        c = Counter(nums)
        idx = len(nums)
        while idx > 1 and not self.sol(c):
            idx -= 1
            if c[nums[idx]] == 1:
                del c[nums[idx]]
            else:
                c[nums[idx]] -= 1
        return idx

def test1():
    nums = [2, 2, 1, 1, 5, 3, 3, 5]
    assert Solution(True).maxEqualFreq(nums) == 7

def test2():
    nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]
    assert Solution(True).maxEqualFreq(nums) == 13

def test3():
    nums = [1, 1, 1, 2, 2, 2]
    assert Solution().maxEqualFreq(nums) == 5

def test4():
    nums = [10, 2, 8, 9, 3, 8, 1, 5, 2, 3, 7, 6]
    assert Solution(True).maxEqualFreq(nums) == 8

def test5():
    # failed test on initial submission
    nums = [1,2]
    assert Solution(True).maxEqualFreq(nums) == 2

def test6():
    # failed test on second submission
    nums = [1,1]
    assert Solution(True).maxEqualFreq(nums) == 2

def test7():
    # failed test on third submission
    nums = [1,2,3,4,5,6,7,8,9]
    assert Solution(True).maxEqualFreq(nums) == 9
