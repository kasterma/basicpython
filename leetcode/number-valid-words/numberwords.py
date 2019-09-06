# 1178. Number of Valid Words for Each Puzzle
# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

from typing import List


class Solution:

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

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        wordsets = Solution._all_sets(words)
        return [
            sum(Solution._ww(wordsets, puzzle))
            for puzzle in puzzles
        ]


# noinspection PyProtectedMember
def test_word_puzzle():
    assert Solution._word_puzzle(set("test"), "e", set("set"))
    assert not Solution._word_puzzle(set("test"), "a", set("set"))
    assert not Solution._word_puzzle(set("test"), "e", set("et"))
    assert Solution._word_puzzle(
        set("test"), "s", set("sdlfjaslfdjdlhgkdsahfkefdjksjsteettt")
    )


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

    result = benchmark(solution_for, 1000)
