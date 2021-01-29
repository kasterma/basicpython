from undertest import X, B
import unittest.mock as mock
import builtins


def test_X():
    x = X()
    print(x.f())
    assert x.f() == 10


test_X()

def test_X_2():
    with mock.patch("builtins.super") as mock_super:
        x = X()
        mock_super().f = lambda: 3
        print(x.f())
        assert x.f() == 6

test_X_2()
