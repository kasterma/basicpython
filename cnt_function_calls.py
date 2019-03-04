# count number of times a function has been called

from functools import wraps
import logging

logging.basicConfig(level=logging.INFO)

def cnt_closure(f):
    log = logging.getLogger(f"logger_{f.__name__}")
    cnt = 0
    #@wraps(f)
    def wrap(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        log.info(f"Called {cnt} times")
        return f(*args, **kwargs)
    return wrap

@cnt_closure
def f(x):
    return 2*x

def cnt(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        pass

from collections import defaultdict
import weakref

class KeepRefs(object):
    __refs__ = defaultdict(list)

    def __init__(self):
        self.__refs__[self.__class__].append(weakref.ref(self))

    @classmethod
    def get_instances(cls):
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if inst is not None:
                yield inst

class X(KeepRefs):
    def __init__(self, name):
        super(X, self).__init__()
        self.name = name

x = X("x")
y = X("y")
for r in X.get_instances():
    print(r.name)
del y
for r in X.get_instances():
    print(r.name)
print("done")
