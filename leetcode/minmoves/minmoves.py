import time
from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        pass


class Timer:
    def __enter__(self):
        self.start = time.monotonic()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(f"Took {time.monotonic() - self.start}")


def test1():
    grid = [[0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 0]]
    assert Solution().minimumMoves(grid) == 11


def test2():
    grid = [[0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 1],
            [1, 1, 1, 0, 0, 1],
            [1, 1, 1, 0, 0, 0]]
    assert Solution().minimumMoves(grid) == 9
