from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        cts = Counter(s)
        cq, cw, ce, cr = cts['Q'], cts['W'], cts['E'], cts['R']
        if cq == cw == ce == cr:
            return 0
        best = len(s)
        ls = best
        scts = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        goal = ls / 4 # by assumption ls is divisible by 4

        def possible(scts):
            return cq - scts['Q'] <= goal and cw - scts['W'] <= goal and ce - scts['E'] <= goal and cr - scts['R'] <= goal

        def impossible(scts):
            return not possible(scts)

        i, j = 0, 0
        while True:
            while j < ls and impossible(scts):
                scts[s[j]] += 1
                j += 1
            while possible(scts):
                scts[s[i]] -= 1
                i += 1
            best = min(best, j - (i - 1))
            if j == ls:
                return best


def test1():
    s = "QWER"
    assert Solution().balancedString(s) == 0

def test2():
    s = "QQWE"
    assert Solution().balancedString(s) == 1

def test3():
    s = "QQQW"
    assert Solution().balancedString(s) == 2

def test4():
    s = "QQQQ"
    assert Solution().balancedString(s) == 3

def test5():
    s = "WWQQRRRRQRQQ"
    assert Solution().balancedString(s) == 4

def test6():
    s = "WQWRQQQW"
    assert Solution().balancedString(s) == 3
