class AA:
    def __init__(self):
        print(f"start AA.__init__ {self.__dict__}")
        self.aa = True
        super().__init__()

    def ff(self):
        print("AA.ff")


class A(AA):
    def __init__(self):
        print(f"start A.__init__ {self.__dict__}")
        self.xx = 9
        super().__init__()
        super().ff()
        print(A.__mro__)

    def f(self):
        print("A.f")


class B(AA):
    def __init__(self):
        print(f"start B.__init__ {self.__dict__}")
        self.b = True
        super().__init__()

    def f(self):
        print("B.f")

    def ff(self):
        print("B.ff")


class C(A, B):
    def __init__(self):
        print(f"start C.__init__ {self.__dict__}")
        super().__init__()
        print(f"end C.__init__ {self.__dict__}")
        super().f()


C()


class A1:
    def f(self):
        print("A1.f")

    def g(self):
        print("A1.g")
        self.f()


class B1(A1):
    def f(self):
        print("B1.f")
        super().f()

b1 = B1()
b1.g()
