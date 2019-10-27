import random
import numpy as np

from typing import List

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50

def solve(val: List[int], wt: List[int], W: int) -> int:
    # pick first element or not
    if not val:
        return 0

    v1 = (val[0] + solve(val[1:], wt[1:], W - wt[0])) if wt[0] <= W else 0

    v2 = solve(val[1:], wt[1:], W)

    return max(v1, v2)

solve(val, wt, W)

def genks(n):
    return (random.choices(range(1, 200), k=n), random.choices(range(1, 200), k=n), random.choice(range(10,500)))

p = genks(100)
solve(*p)

def solvedp(val: List[int], wt: List[int], w:int) -> int:
    m = np.zeros((len(val), (w+1)))
    for i in range(len(val)):
        for j in range(w+1):
            if i == 0: # first item
                m[i][j] = val[i] if wt[i] <= j else 0
            else:
                m[i][j] = max(m[i-1][j], m[i-1][j - wt[i]] + val[i]) if wt[i] <= j else m[i-1][j]
    return m[len(val)-1, w]

solvedp(val, wt, W)

for i in range(100):
    print(i)
    test_p = genks(20)
    assert solve(*p) == solvedp(*p)
