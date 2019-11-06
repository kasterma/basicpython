from collections import defaultdict, Counter
from typing import List


class Solution:
    def furthest(self, d, n):
        """Find node furthest from n"""
        dists = Counter()
        dists[n] = 0
        added = [n]
        next_added = []
        while added:
            for h in added:
                dh = dists[h]
                for t in d[h]:
                    if t not in dists.keys():
                        next_added.append(t)
                        dists[t] = dh + 1
            added = next_added
            next_added = []
        print(dists)
        return dists.most_common(1)[0]

    def treeDiameter(self, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for h, t in edges:
            d[h].append(t)
            d[t].append(h)
        print(d)
        # d now is lookup for nbds of node
        h, _ = self.furthest(d, edges[0][0])
        print(h)
        _, diam = self.furthest(d, h)
        return diam

def test1():
    edges = [[0, 1], [0, 2]]
    assert Solution().treeDiameter(edges) == 2

def test2():
    edges = [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]
    assert Solution().treeDiameter(edges) == 4

def test3():
    edges = [[0, 1], [0, 2], [1, 3], [0, 4], [1, 5], [2, 6], [1, 7]]
    assert Solution().treeDiameter(edges) == 4
