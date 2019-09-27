from typing import List
from collections import defaultdict
import time

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        def grp(idx):
            """The group of element idx; where if idx has group[idx] we assign it to group idx + m by itself"""
            g = group[idx]
            return g if g >= 0 else idx + m

        # collect the derived order on groups
        beforeGrps = defaultdict(set)
        for idx, before in enumerate(beforeItems):
            beforeGrps[grp(idx)] = beforeGrps[grp(idx)].union({grp(j) for j in before if grp(j) != grp(idx)})

        itemsLeft = {idx for idx in range(n)}
        grpsLeft = {grp(idx) for idx in range(n)}

        rv = []
        while itemsLeft:
            candidateGrps = [g for g in grpsLeft if not beforeGrps[g]]
            if not candidateGrps:
                return []
            minGrp = min(candidateGrps)
            grpsLeft.remove(minGrp)
            for g in beforeGrps.values():
                if minGrp in g:
                    g.remove(minGrp)
            grpItems = {i for i in itemsLeft if grp(i) == minGrp}
            while grpItems:
                candidateItems = [i for i in grpItems if not beforeItems[i]]
                if not candidateItems:
                    return []
                minItem = min(candidateItems)

                for l in beforeItems:
                    if minItem in l:
                        l.remove(minItem)
                rv.append(minItem)
                itemsLeft.remove(minItem)
                grpItems.remove(minItem)

        return rv

def test1():
    n = 8
    m = 2
    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]
    assert Solution().sortItems(n, m, group, beforeItems) == [6, 3, 4, 5, 2, 0, 1, 7]


def test2():
    n = 8
    m = 2
    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems = [[], [6], [5], [6], [3], [], [4], []]
    assert Solution().sortItems(n, m, group, beforeItems) == []

class Timer:
    def __enter__(self):
        self.start = time.monotonic()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"time {time.monotonic() - self.start}")

if __name__ == "__main__":
    from largetestcase import n, m, group, beforeItems

    # first run 127 seconds
    with Timer():
        Solution().sortItems(n, m, group, beforeItems)
