from typing import List, Dict, FrozenSet


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        d = {frozenset(): 0}
        for idx in range(len(arr)):
            current_letters = set(arr[idx])
            current_len = len(arr[idx])
            if len(current_letters) == current_len:
                for sw, l in list(d.items()):
                    if not current_letters.intersection(sw):
                        k = frozenset(sw.union(current_letters))
                        d[k] = max(l + current_len, d[k]) if k in d else l + current_len

        return max(d.values())

def test1():
    arr = ["un","iq","ue"]
    assert Solution().maxLength(arr) == 4

def test2():
    arr = ["cha","r","act","ers"]
    assert Solution().maxLength(arr) == 6

def test3():
    arr = ["abcdefghijklmnopqrstuvwxyz"]
    assert Solution().maxLength(arr) == 26
