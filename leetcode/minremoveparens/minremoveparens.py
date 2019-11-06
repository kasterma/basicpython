class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        pass

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

