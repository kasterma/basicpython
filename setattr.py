class TestSetAttr:

    def __init__(self):
        self.x = 9

    def __setattr__(self, key, value):
        print("Setting {} to {}".format(key, value))
        object.__setattr__(self, key, value)


def test_set_attr():
    TestSetAttr()