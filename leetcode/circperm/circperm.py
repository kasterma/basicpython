import time
from typing import List
from itertools import cycle, islice, repeat, chain


class Solution:
    def row(self, n, i):
        seqs = 2**(n - i)
        seq_len = 2**i
        ls = [[j] * seq_len for j in islice(cycle([1, 0, 0, 1]), seqs)]
        return [i for l in ls for i in l]

    def genMatrix(self, n: int) -> List[List[int]]:
        return [self.row(n, i) for i in range(n)]

    def c2n(self, c):
        b = 1
        r = 0
        for i in range(len(c)):
            if c[i] == 1:
                r += b
            b *= 2
        return r

    def m2n(self, m, n):
        r = []
        for i in range(2**n):
            c = [m[j][i] for j in range(n)]
            r.append(self.c2n(c))
        return r

    def circularPermutation(self, n: int, start: int) -> List[int]:
        m = self.genMatrix(n)
        p = self.m2n(m, n)
        i = p.index(start)
        return p[i:] + p[:i]


def test1():
    s = Solution()
    assert s.row(4, 3) == [1]*8 + [0]*8

def test2():
    s = Solution()
    assert s.genMatrix(2) == [[1,0,0,1], [1,1,0,0]]
    assert s.genMatrix(3) == [[1,0,0,1,1,0,0,1],[1,1,0,0,0,0,1,1],[1,1,1,1,0,0,0,0]]

def test3():
    s = Solution()
    assert s.circularPermutation(2, 3) == [3, 2, 0, 1]
    assert s.circularPermutation(3, 7) == [7, 6, 4, 5, 1, 0, 2, 3]
    assert s.circularPermutation(3, 5) == [5, 1, 0, 2, 3, 7, 6, 4]

class Timer:
    def __enter__(self):
        self.start = time.monotonic()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(f"Took {time.monotonic() - self.start}")

