class A:
    def __init__(self, x):
        print(f"init A({x})")
        self.x = x

    def label(self):
        print("A")

    def f(self):
        super().f()
        print("f from A")
        print(f"class name {self.__class__.__name__}")
        x = self.__class__(3)
        x.label()


class B:
    def __init__(self, x):
        print(f"init B({x})")
        self.x = x

    def label(self):
        print("B")

    def f(self):
        print("f from B")


class C(A, B):
    def __init__(self, x):
        print(f"init C({x})")
        self.x = x

    def label(self):
        print("C")

    def f(self):
        super().f()
        print("f from C")


c = C(22)
c.f()
