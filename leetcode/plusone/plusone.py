from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return self.plusOne_helper(digits, carry=1, idx=len(digits)-1)

    def plusOne_helper(self, digits, carry, idx):
        val = digits[idx] + carry
        new_digit = val % 10
        new_carry = val // 10

        digits[idx] = new_digit
        if idx == 0:
            if new_carry == 0:
                return digits
            else:
                return [new_carry] + digits
        else:
            if new_carry == 0:
                return digits
            else:
                return self.plusOne_helper(digits, new_carry, idx-1)


def test1():
    Input = [1, 2, 3]
    Output = [1, 2, 4]
    assert Solution().plusOne(Input) == Output

def test2():
    Input = [4, 3, 2, 1]
    Output = [4, 3, 2, 2]
    assert Solution().plusOne(Input) == Output

def test3():
    Input = [9, 9, 9, 9]
    Output = [1, 0, 0, 0, 0]
    assert Solution().plusOne(Input) == Output
