# https://leetcode.com/problems/maximum-equal-frequency/

from collections import Counter
from typing import List


# def sol2(self, c: Counter) -> bool:
#     val_set = set(c.values())
#     if len(val_set) == 2:
#         a, b = list(val_set)
#         if abs(a - b) == 1:
#             ct_a = len([v for v in c.values() if v == a])
#             ct_tot = len(c)
#             if a + 1 == b and ct_a + 1 == ct_tot:
#                 return True
#             elif b + 1 == a and ct_a == 1:
#                 return True
#
#     return False

class Solution:
    def __init__(self, debug=False):
        self.debug = debug

    def sol(self, c: Counter) -> bool:
        if self.debug:
            print(f"counter {c}")
        c_vals = Counter(c.values())
        if self.debug:
            print(f"c_vals {c_vals}")
        if len(c_vals) == 2:
            a, b = c_vals.keys()
            if a > b:
                a, b = b, a
            if self.debug:
                print(f"a,b {a} {b}")
            if (a + 1 == b and c_vals[b] == 1) or (a == 1 and c_vals[a] == 1):
                if self.debug:
                    print("True")
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

