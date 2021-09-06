# I would like to make what I think is called a facade object.  Pass all calls except a selected one or two to the
# base object.

class A:
    def f(self):
        print("Af")
    def __getattr__(self, item):
        print(f"item={item}")

iter(A())

hasattr(A(), "__iter__")


class B:
    def f(self):
        print("f")

b = B()
b.f()

def g(f):
    def ff():
        print("ff-before")
        rv = f()
        print("ff-after")
        return rv
    return ff

b.f = g(b.f)

class C:
    def __init__(self, x):
        self._x = x

    def __getattr__(self, name):
        return getattr(self._x, name)

c = C(B())
c.f()


class D(A):
    def f(self):
        print("df")
        super().f()
        print("dfafer")
D().f()
