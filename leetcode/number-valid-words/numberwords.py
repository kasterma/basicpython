# 1178. Number of Valid Words for Each Puzzle
# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

from typing import List
import string
from collections import defaultdict
from itertools import chain, combinations


class Solution1:
    """using hint to look at bitmasks"""
    @staticmethod
    def str2bm(s):
        return int("".join('1' if l in s else '0' for l in string.ascii_lowercase), 2)

    @staticmethod
    def subsbm(a, b):
        """a is subset of b seen as bitmask"""
        return not(a & ~ b)

    @staticmethod
    def _diff(w, p):
        """separate out for profiling"""
        return w.difference(p)

    @staticmethod
    def _word_puzzle(word: set, puzzle_first: str, puzzle: set) -> bool:
        return puzzle_first in word and word.issubset(puzzle)

    @staticmethod
    def _all_sets(words):
        return [set(w) for w in words]

    @staticmethod
    def _ww(wordsets, puzzle):
        return [Solution._word_puzzle(w, puzzle[0], set(puzzle)) for w in wordsets]

    @staticmethod
    def _prepare(words, puzzles):
        return [Solution.str2bm(w) for w in words], [(Solution.str2bm(p[0]), Solution.str2bm(p)) for p in puzzles]

    @staticmethod
    def _counts(wordbm, puzzlebm):
        return [
            sum(True for w in wordbm if l & w and Solution.subsbm(w, p))
            for l, p in puzzlebm
        ]

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # word prep   #words
        # puzzle prep    #puzzle
        # mix and match  #words * # puzzle
        wordbm, puzzbml = Solution._prepare(words, puzzles)
        return Solution._counts(wordbm, puzzbml)

class Solution:
    """using the idea that was used with bitmasks, but without the bitmasks"""
    @staticmethod
    def normalize(s):
        """standard order, every letter only once"""
        return "".join(l for l in string.ascii_lowercase if l in s)

    @staticmethod
    def _prepare(words):
        d = defaultdict(int)
        for w in words:
            d[Solution.normalize(w)] += 1
        return d

    @staticmethod
    def powerset_withfirst(puzzle):
        "from itertools recipe adjusted"
        f = puzzle[0]
        s = list(set(puzzle))
        return [Solution.normalize("".join(p))
                for p in chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
                if f in p]

    @staticmethod
    def _counts(wordcts, puzzle):
        return sum(wordcts.get(nw, 0) for nw in Solution.powerset_withfirst(puzzle))

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        wordcts = Solution._prepare(words)
        return [Solution._counts(wordcts, puzzle) for puzzle in puzzles]



# noinspection PyProtectedMember
# def test_word_puzzle():
#     assert Solution._word_puzzle(set("test"), "e", set("set"))
#     assert not Solution._word_puzzle(set("test"), "a", set("set"))
#     assert not Solution._word_puzzle(set("test"), "e", set("et"))
#     assert Solution._word_puzzle(
#         set("test"), "s", set("sdlfjaslfdjdlhgkdsahfkefdjksjsteettt")
#     )


def test_find_example():
    words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
    puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
    answers = [1, 1, 3, 2, 4, 0]

    computed = Solution().findNumOfValidWords(words=words, puzzles=puzzles)
    assert answers == computed


def test_speed1(benchmark):
    from slowtestcase import slow_puzzles, slow_words
    print((len(slow_puzzles), len(slow_words)))

    def solution_for(ct):
        Solution().findNumOfValidWords(slow_words[:ct], slow_puzzles[:ct])

    result = benchmark(solution_for, 10000)


def iterate_masks(x):
    """key ingredient for bitmask solution from a discussion on leetcode"""
    y = x
    while y:
        print(f"{y:b}")
        y = (y - 1) & x


def iterate2(p):
    """second iteration from a solution on leetcode"""
    n = ord('a')
    a = [1 << (ord(p[0]) - n)]
    for c in p[1:]:
        t = 1 << (ord(c) - n)
        a += [x | t for x in a]
    return a


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        count = collections.Counter(frozenset(w) for w in words)
        # print (count)
        res = []
        for p in puzzles:
            cur = 0
            for k in range(7):
                for c in itertools.combinations(p[1:], k):
                    cur += count[frozenset(tuple(p[0]) + c)]

            res.append(cur)
        return res


# for profiling, run without the test stuff around it
if __name__ == "__main__":
    from slowtestcase import slow_puzzles, slow_words

    def solution_for(ct):
        Solution().findNumOfValidWords(slow_words[:ct], slow_puzzles[:ct])

    solution_for(100000)
