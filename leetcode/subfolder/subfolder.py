from typing import List
from collections import defaultdict


class Solution:
    TOK = "666"

    def build(self, folder):
        def defd():
            return defaultdict(defd)

        dd = defd()

        for f in folder:
            fp = f.split("/")[1:]
            d = dd
            for k in fp[:-1]:
                d = d[k]
                if d == self.TOK:
                    break
            else:
                d[fp[-1]] = self.TOK

        return dd

    def folders(self, fs, prefix=""):
        l = []
        for k in fs.keys():
            if fs[k] == self.TOK:
                l.append(prefix + "/" + k)
            else:
                l.extend(self.folders(fs[k], prefix=prefix+"/"+k))
        return l

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        fs = self.build(folder)
        print(fs)
        return self.folders(fs)


def test1():
    folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
    assert Solution().removeSubfolders(folder) == ["/a", "/c/d", "/c/f"]

def test2():
    folder = ["/a", "/a/b/c", "/a/b/d"]
    assert Solution().removeSubfolders(folder) == ["/a"]

def test3():
    folder = ["/a/b/c", "/a/b/ca", "/a/b/d"]
    assert Solution().removeSubfolders(folder) == ["/a/b/c", "/a/b/ca", "/a/b/d"]
