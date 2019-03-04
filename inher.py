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

    @classmethod
    def ff(cls):
        # super().ff()
        print("ff from A")
        print(f"class name {cls.__name__}")
        x = cls(3)
        x.label()


class B:
    def __init__(self, x):
        print(f"init B({x})")
        self.x = x

    def label(self):
        print("B")

    def f(self):
        # super().f()
        print("f from B")

    @classmethod
    def ff(cls):
        # super().ff()
        print("ff from B")
        print(f"class name {cls.__name__}")
        x = cls(3)
        x.label()


class C(A, B):
    def __init__(self, x):
        print(f"init C({x})")
        self.x = x

    def label(self):
        print("C")

    def f(self):
        super().f()
        print("f from C")

    @classmethod
    def ff(cls):
        super().ff()
        print("ff from C")
        print(f"class name {cls.__name__}")
        x = cls(3)
        x.label()
        return x


c = C(22)
c.f()
print("now ff")
x = c.ff()
print(type(x))
