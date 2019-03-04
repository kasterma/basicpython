class TestSetAttr:
    zz = 999

    def __init__(self):
        self.x = 9

    def __setattr__(self, key, value):
        print("Setting {} to {}".format(key, value))
        object.__setattr__(self, key, value)


def test_set_attr():
    TestSetAttr()


class A(TestSetAttr):
    xx = 9

A()