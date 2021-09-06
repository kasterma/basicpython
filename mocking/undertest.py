class B:
    def f(self):
        return 5

    def h(self):
        return 99

class X(B):
    def f(self):
        return super().f()

x = X()

def calls():
    x.f()
    x.h()
