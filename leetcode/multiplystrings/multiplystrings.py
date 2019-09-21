import random

class Solution:
    def add(self, num1: str, num2: str):
        if num1 == "0":
            return num2
        elif num2 == "0":
            return num1

        num1 = list(num1)
        num1.reverse()
        num2 = list(num2)
        num2.reverse()
        carry = 0
        min_len = min(len(num1), len(num2))
        rv = []
        for idx in range(min_len):
            i, j = int(num1[idx]), int(num2[idx])
            v = i + j + carry
            rv.append(str(v % 10))
            carry = v // 10
        for idx in range(min_len, len(num1)):
            i = int(num1[idx])
            v = i + carry
            rv.append(str(v % 10))
            carry = v // 10
        for idx in range(min_len, len(num2)):
            i = int(num2[idx])
            v = i + carry
            rv.append(str(v % 10))
            carry = v // 10

        if carry > 0:
            rv.append(str(carry))
        rv.reverse()
        return "".join(rv)

    def muldigit(self, digit: int, num2: str):
        num2 = list(num2)
        num2.reverse()
        rv = []
        carry = 0
        for idx in range(len(num2)):
            v = digit * int(num2[idx]) + carry
            rv.append(str(v % 10))
            carry = v // 10
        if carry > 0:
            rv.append(str(carry))
        rv.reverse()
        return "".join(rv)

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        num1 = list(num1)
        num1.reverse()
        v = "0"
        for idx in range(len(num1)):
            m = self.muldigit(int(num1[idx]), num2) + "0" * idx
            v = self.add(v, m)
        return v

def test_add():
    for _ in range(100):
        i, j = random.randrange(0, 1000), random.randrange(0, 1000)
        assert Solution().add(str(i), str(j)) == str(i + j)


def test1():
    num1 = "2"
    num2 = "3"
    assert Solution().multiply(num1, num2) == "6"

def test2():
    num1 = "123"
    num2 = "456"
    assert Solution().multiply(num1, num2) == "56088"
