class B:
    def f(self):
        return 5

class X(B):
    def f(self):
        return 2 * super().f()
