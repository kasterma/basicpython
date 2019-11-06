import random
import time


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_idx = []
        remove_idx = []
        ct = 0
        for idx, c in enumerate(s):
            if c == "(":
                open_idx.append(idx)
                ct += 1
            if c == ")":
                if ct == 0:
                    remove_idx.append(idx)
                else:
                    ct -= 1

        if ct > 0:
            remove_idx.extend(open_idx[-ct:])

        return "".join(c for idx, c in enumerate(s) if not idx in remove_idx)

    def minRemoveToMakeValid_others(self, s: str) -> str:
        # NOT MY SOLUTION; copied here to compare timings
        # Use a array to save empty
        a = list(s)
        b = []
        for i, c in enumerate(s):
            if c == '(':
                b.append(i)
            elif c == ')':
                if b:
                    b.pop()
                else:
                    a[i] = ''

        while b:
            a[b.pop()] = ''

        return ''.join(a)

def valid(s):
    ct = 0
    for c in s:
        if c == "(":
            ct += 1
        if c == ")":
            if ct == 0:
                return False
            else:
                ct -= 1

    return ct == 0

def test_valid():
    assert valid("")
    assert valid("()")
    assert valid("asdf(sdsds(dssds(sd)dss(sds)dsds)dsds)dsds")
    assert not valid("((")
    assert not valid("(()))")


def test1():
    s = "lee(t(c)o)de)"
    sol = Solution().minRemoveToMakeValid(s)
    assert valid(sol)
    assert len(sol) == len("lee(t(c)o)de")

def test2():
    s = "a)b(c)d"
    sol = Solution().minRemoveToMakeValid(s)
    assert valid(sol)
    assert len(sol) == len("ab(c)d")

def test3():
    s = "))(("
    sol = Solution().minRemoveToMakeValid(s)
    assert valid(sol)
    assert len(sol) == 0

def test4():
    s = "(a(b(c)d)"
    sol = Solution().minRemoveToMakeValid(s)
    assert valid(sol)
    assert len(sol) == len("a(b(c)d)")

class Timer:
    def __enter__(self):
        self.start = time.monotonic()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(f"Took {time.monotonic() - self.start}")

if __name__ == "__main__":
    s = random.choices(["a", "b", "c", "(", ")"], k=10000)

    with Timer():
        Solution().minRemoveToMakeValid(s)

    with Timer():
        Solution().minRemoveToMakeValid_others(s)
