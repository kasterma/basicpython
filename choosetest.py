import collections
import random
import pandas as pd


class C1:
    def __init__(self, xs):
        self._xs = xs

    def __len__(self):
        return len(self._xs)

    def __getitem__(self, item):
        return self._xs[item]


c1 = C1([11, 22, 33])

cs = [random.choice(c1) for _ in range(1000)]
pd.Series(cs).value_counts()
collections.Counter(cs)

collections.UserDict
