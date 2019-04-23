"""How to mock"""

from unittest import mock

from unittest.mock import _Call

m = mock.Mock(name="mockthis")

m()
m()
m(1,2,3)
assert m.call_count == 3
assert m.call_args == ((1, 2, 3), {})

m.reset_mock()
assert m.call_count == 0

def f(x):
    return x + 2

m.f = f

class A:
    def __init__(self, val):
        self.val = val

a = A(11)
print(a.val)
with mock.patch.object("A", 'val', 99):
    print(a.val)
print(a.val)
