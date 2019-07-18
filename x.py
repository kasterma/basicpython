# some async code to test in mocking context

class X:
    def f(self):
        return 3

    async def g(self, x):
        return 4 + x

