class E1(Exception):
    def __init__(self, message):
        self.message = message


def f(m: str):
    raise E1(m)


def g():
    try:
        f("from g")
    except TimeoutError as e:
        pass
        # I know this doesn't happen
    finally:
        print("finally here")
        # raise E1("from finally")
        return
    # check if there was still an exception pending, then continue with it.
    print("not this")
    return


g()


def h():
    try:
        g()
        print("yes this")
    except E1 as e:
        print("this")


def i():
    try:
        print("this")
        raise Exception()
        return 5
    finally:
        print("that'")


i()
