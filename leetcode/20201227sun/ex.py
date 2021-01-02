import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import logging
import sys

log = logging.getLogger()
log.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
log.addHandler(handler)

vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def alike(s1, s2):
    def count_in(s, special=vow):
        return sum(c in special for c in s)

    return count_in(s1) == count_in(s2)


def test_alike():
    assert alike("aa", "AA")
    assert alike("abcabc", "cbacba")


class Solution0:
    def halvesAreAlike(self, s: str) -> bool:
        return alike(s[:len(s) // 2], s[len(s) // 2:])


def test_sol():
    s = Solution0()
    assert s.halvesAreAlike("book")


from typing import List
import heapq


class Solution1:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        ct = 0
        day = 0
        apple_tree = []

        day_pair = lambda day: [day + days[day] - 1, apples[day]]
        add_day_pair = lambda day: heapq.heappush(apple_tree, day_pair(day)) if apples[day] > 0 else None

        add_day_pair(day)
        while day < n or apple_tree:
            print(day, apple_tree)
            if apple_tree:
                ct += 1
                if apple_tree[0][1] == 1:
                    heapq.heappop(apple_tree)
                else:
                    apple_tree[0][1] -= 1
                while apple_tree and apple_tree[0][0] <= day:
                    heapq.heappop(apple_tree)
            print(ct)
            day += 1
            if day < n and apples[day] > 0:
                add_day_pair(day)

        return ct


def test_apples():
    s = Solution1()
    assert s.eatenApples([1, 2, 3, 5, 2], [3, 2, 1, 4, 2]) == 7
    assert s.eatenApples([3, 0, 0, 0, 0, 2], [3, 0, 0, 0, 0, 2]) == 5
    assert s.eatenApples([3, 1, 1, 0, 0, 2], [3, 1, 1, 0, 0, 2]) == 5
    assert s.eatenApples(
        [0, 19, 19, 19, 11, 14, 33, 0, 28, 7, 0, 28, 7, 0, 21, 16, 0, 22, 0, 13, 8, 0, 19, 0, 0, 2, 26, 2, 22, 0, 8, 0,
         0, 27, 19, 16, 24, 0, 20, 26, 20, 7, 0, 0, 29, 0, 0, 16, 19, 0, 0, 0, 29, 30, 17, 0, 23, 0, 0, 26, 24, 13, 3,
         0, 21, 0, 18, 0],
        [0, 5, 1, 16, 7, 10, 54, 0, 40, 2, 0, 23, 4, 0, 20, 18, 0, 40, 0, 22, 8, 0, 35, 0, 0, 3, 24, 1, 8, 0, 10, 0, 0,
         2, 38, 8, 4, 0, 36, 33, 14, 9, 0, 0, 56, 0, 0, 21, 27, 0, 0, 0, 14, 20, 18, 0, 42, 0, 0, 44, 3, 8, 3, 0, 10, 0,
         27, 0]) == 102


class Solution2:
    # stuck is determined on the same level hit a one followed by a -1 [1, -1]
    # or hit a -1 preceded by a -1
    # or 1 in rightmost
    # or -1 in leftmost
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        cur_loc = list(range(m))
        next_loc = [0] * m

        for row_idx in range(n):
            print(cur_loc)
            row = grid[row_idx]
            for bal_idx in range(m):
                col_idx = cur_loc[bal_idx]
                if (col_idx == -1 or
                    (col_idx == 0 and row[col_idx] == -1) or
                    (col_idx == m - 1 and row[col_idx] == 1) or
                    (col_idx < m - 1 and row[col_idx] == 1 and row[col_idx + 1] == -1) or
                    (0 < col_idx and row[col_idx] == -1 and row[col_idx - 1] == 1)):
                    next_loc[bal_idx] = -1
                elif row[col_idx] == 1:
                    next_loc[bal_idx] = cur_loc[bal_idx] + 1
                else:
                    next_loc[bal_idx] = cur_loc[bal_idx] - 1
            # setup for next round
            cur_loc = next_loc
            next_loc = [0] * m
        print(cur_loc)
        return cur_loc


def test_ball():
    s = Solution2()
    assert s.findBall(
        [[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]) == [1, -1,
                                                                                                                -1, -1,
                                                                                                                -1]
    assert s.findBall([[-1]]) == [-1]
    assert s.findBall([[1]]) == [-1]
    assert s.findBall(
        [[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]]) == [0, 1, 2, 3, 4,
                                                                                                          -1]
    assert s.findBall(
        [[1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1,
          -1, 1, -1, 1, 1, -1, -1, -1, -1, -1, 1],
         [-1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, -1, -1, 1,
          -1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1],
         [1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1,
          1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1]]) \
           == [-1, -1, 1, -1, -1, -1, -1, 10, 11, -1, -1, 12, 13, -1, -1, -1, -1, -1, 17, -1, -1, 20, -1, -1, -1, -1,
               -1, -1, -1, -1, 27, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

from typing import Union


class BinTree:
    def __init__(self, one=None, zero=None, len=0):
        self._one: Union[BinTree, None] = one
        self._zero: Union[BinTree, None] = zero
        self._len = len

    def is_empty(self) -> bool:
        return self._one is None and self._zero is None and self._len == 0

    def merge(self, other: Union["BinTree", None]) -> "BinTree":
        """Merge the two trees together"""
        # Note: extending an empty tree adds zero, so check for this special case
        if other is None or other.is_empty():
            return self
        if self.is_empty():
            return other
        merge_len = max(self._len, other._len)
        a = self.extend(merge_len)
        b = other.extend(merge_len)
        return BinTree(one=a._one.merge(b._one) if a._one else b._one,
                       zero=a._zero.merge(b._zero) if a._zero else b._zero,
                       len=merge_len)

    @staticmethod
    def from_int(n: int) -> "BinTree":
        n_str = bin(n)[2:]
        n_len = len(n_str)
        rv = BinTree()
        cur = rv
        for idx, digit in enumerate(n_str):
            cur._len = n_len - idx
            log.debug(cur._len)
            if digit == "0":
                log.debug("zero")
                cur._zero = cur = BinTree()
            else:
                log.debug("one")
                cur._one = cur = BinTree()
        return rv

    def add(self, n) -> "BinTree":
        return self.merge(BinTree.from_int(n))

    def extend(self, len: int) -> "BinTree":
        """Extend the depth of the tree with leading zeros (if needed)."""
        if len <= self._len:
            return self

        rv = self
        for i in range(1, len - self._len + 1):
            new_root = BinTree()
            new_root._zero = rv
            new_root._len = new_root._zero._len + 1
            if new_root._len != self._len + i:
                raise Exception(f"{new_root._len} != {self._len + i} , i={i}")
            rv = new_root
        return rv

    def __repr__(self):
        return f"<{repr(self._zero)}, {repr(self._one)}>"


def test_bintree():
    assert repr(BinTree().extend(2)) == "<<<None, None>, None>, None>"
    assert repr(BinTree().from_int(0)) == "<<None, None>, None>"
    assert repr(BinTree().from_int(1)) == "<None, <None, None>>"
    assert repr(BinTree().from_int(3)) == "<None, <None, <None, None>>>"
    assert repr(BinTree().from_int(4)) == "<None, <<<None, None>, None>, None>>"
    assert repr(BinTree().add(4)) == "<None, <<<None, None>, None>, None>>"
    assert repr(BinTree().add(0)) == "<<None, None>, None>"
    assert repr(BinTree().add(0).add(1)) == "<<None, None>, <None, None>>"
    assert repr(BinTree().add(3)) == "<None, <None, <None, None>>>"
    assert repr(BinTree().add(3).add(2)) == "<None, <<None, None>, <None, None>>>"


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums = sorted(set(nums))
        next_num_idx = 0
        queries = sorted(enumerate(queries), key=lambda p: p[1][1])
        rv = [0] * len(queries)
        bt = BinTree()
        for idx, query in queries:
            while next_num_idx < len(nums) and nums[next_num_idx] <= query[1]:
                bt = bt.add(nums[next_num_idx])
                next_num_idx += 1
            if bt.is_empty():
                rv[idx] = -1
            else:
                q_t = BinTree.from_int(query[0])
                merge_len = max(q_t._len, bt._len)
                q_t = q_t.extend(merge_len)
                btt = bt.extend(merge_len)
                # now are the same length, q_t contains single path, search with btt for max differences and recreate m
                m = 0
                while q_t._len != 0:
                    m *= 2
                    if q_t._one and btt._zero:
                        q_t=q_t._one
                        btt = btt._zero
                    elif q_t._zero and btt._one:
                        m += 1
                        q_t = q_t._zero
                        btt = btt._one
                    elif q_t._one:
                        m += 1
                        q_t = q_t._one
                        btt = btt._one
                    elif q_t._zero:
                        q_t = q_t._zero
                        btt = btt._zero
                rv[idx] = query[0]^m
        return rv


def test_maxxor():
    s = Solution()
    assert s.maximizeXor(nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]) == [3, 3, 7]
    assert s.maximizeXor(nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]) == [15, -1, 5]

import time


class Timer:
    def __init__(self):
        self._start = None
        self._end = None

    def start(self):
        self._start = time.monotonic()

    def stop(self):
        self._end = time.monotonic()

    def duration(self):
        return self._end - self._start

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()


import gc

if __name__ == "__main__":
    print("Running some different timings related to 4th problem (b/c too slow and not certain where the time goes)")
    # also practicing some matplotlib
    xs = range(1, 20_000_000_000, 10_000_000)
    N = 10_000
    dat = np.zeros((len(xs), N))
    t = Timer()
    gc.set_debug(gc.DEBUG_STATS)
    gc.disable()
    print(gc.get_count())
    with Timer() as tt:
        for x_idx, x in enumerate(xs):
            lts = []
            for idx in range(N):
                with t:
                    BinTree.from_int(x)
                dat[x_idx, idx] = t.duration()
    print(gc.get_count())
    gc.collect()
    plt.plot(xs, dat.mean(axis=1))
    plt.plot(xs, np.median(dat, axis=1))
    plt.plot(xs, np.min(dat, axis=1))



