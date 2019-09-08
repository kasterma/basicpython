import heapq
import time
from collections import defaultdict


class LFUCache1:
    # submission results
    # 1. silly bug
    # 2. didn't thinkg of capacity == 0
    # 3. assumption about put not counting towards when used was false

    def __init__(self, capacity: int, verbose=False):
        self.verbose = verbose
        self.capacity = capacity
        self.d = {}
        self.cts = []  # heap [ct, last_used, key, valid], valid boolean if has already been invalidated
        self.ct_refs = {}  # dict key -> valid item on heap for that key
        self.counter = 0  # avoid having to get real time, every operation increases this by one

    def _print(self, x):
        if self.verbose:
            print(x)

    def _update_key_data(self, key):
        ct = self.ct_refs.get(key, [0, None, key, None])  # last_used and valid will be reset below before use
        ct_new = ct.copy()
        ct[3] = False  # invalidate old copy
        ct_new[0] += 1
        ct_new[1] = self.counter
        heapq.heappush(self.cts, ct_new)
        self.ct_refs[key] = ct_new

    def get(self, key: int) -> int:
        self.counter += 1
        if key in self.d.keys():
            self._update_key_data(key)
            return self.d[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.counter += 1
        if key in self.d.keys():
            self.d[key] = value
            self._update_key_data(key)
            return
        elif len(self.d) == self.capacity:  # need to evict
            # search for valid item in queue
            ct = [None, None, None, False]
            while self.cts and not ct[3]:
                #self._print(f"cts{self}")
                ct = heapq.heappop(self.cts)
            if ct[3]:
                del self.d[ct[2]]
                del self.ct_refs[ct[2]]
                #self._print(f"evict {ct[2]}")

        if len(self.d) < self.capacity:
            ct_new = [1, self.counter, key, True]
            self.ct_refs[key] = ct_new
            #self._print(self.cts)
            heapq.heappush(self.cts, ct_new)
            self.d[key] = value
        #self._print(f"after put {self}")

    def __repr__(self):
        return f"LFUCache({self.d}, {self.cts})"

class LFUCache:
    def __init__(self, capacity: int, verbose=False):
        self.verbose = verbose
        self.capacity = capacity
        self.d = {} # map key -> [val, ct, node]
        self.cts = defaultdict(DLL)  # map ct -> dll of items with that freq

    def _print(self, x):
        if self.verbose:
            print(x)

    def _update_key_data(self, key):
        _, ct, node = self.d[key]
        self.cts[ct].remove(node)
        ct += 1
        self.cts[ct].add_end(node)
        self.d[key][1] = ct

    def get(self, key: int) -> int:
        if key in self.d.keys():
            self._update_key_data(key)
            return self.d[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d.keys():
            self.d[key][0] = value
            self._update_key_data(key)
            return
        elif len(self.d) == self.capacity and self.capacity > 0:  # need to evict, works only when there is data in the cache
            # search for valid item in queue
            ct = 1
            while self.cts[ct].empty():
                ct += 1
            #self._print(f"count {ct}")
            node = self.cts[ct].pop()
            del self.d[node.key]
            #self._print(f"evict {node.key}")

        if len(self.d) < self.capacity:
            node = DLL.new_node(key, value)
            self.cts[1].add_end(node)
            self.d[key] = [value, 1, node]
        #self._print(f"after put {self}")

    def __repr__(self):
        return f"LFUCache({self.d}, {self.cts})"

class DLL:
    """Doubly linked list"""
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    @staticmethod
    def new_node(key, val):
        return DLL.Node(key, val)

    def add_end(self, node):
        """New nodes are added at the end"""
        if node.next or node.prev:
            print("probably error node has next or prev")
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:  #empty list
            self.head = self.tail = node

    def remove(self, node):
        if node.prev and node.next:
            node.prev.next, node.next.prev = node.next, node.prev
        elif node.prev:
            node.prev.next = None
            self.tail = node.prev
        elif node.next:
            node.next.prev = None
            self.head = node.next
        else:
            self.head = self.tail = None # now empty

        node.next = node.prev = None # no dangling pointers

    def empty(self):
        return self.head is None and self.tail is None

    def pop(self):
        if self.head:
            rv = self.head
            if self.head and self.head is not self.tail:
                self.head.next.prev = None
                self.head = self.head.next
                rv.next = None
                assert rv.prev is None
            else:  # now empty
                self.head = None
                self.tail = None
            return rv

        assert False
        return None

    def __len__(self):
        if self.head is None:
            return 0

        ct = 1
        cur = self.head
        while cur.next:
            ct += 1
            cur = cur.next
        return ct

    def __iter__(self):
        rv = []
        cur = self.head
        while cur:
            rv.append([cur.key, cur.val])
            cur = cur.next
        return iter(rv)

    def __repr__(self):
        return str(list(self))


def test_dll():
    d1 = DLL()
    assert 0 == len(d1)
    n1 = DLL.new_node(1, 2)
    d1.add_end(n1)
    assert 1 == len(d1)
    n2 = DLL.new_node(1, 3)
    d1.add_end(n2)
    assert 2 == len(d1)
    d1.remove(n1)
    assert 1 == len(d1)
    d1.add_end(n1)
    assert 2 == len(d1)
    n3 = DLL.new_node(1, 4)
    d1.add_end(n3)
    assert 3 == len(d1)
    d1.remove(n1)
    assert 2 == len(d1)
    assert [[1, 3], [1,4]] == list(d1)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def test_lfu1():
    cache = LFUCache(2, True)

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.d)
    assert 1 == cache.get(1)
    cache.put(3, 3)  # evicts key 2
    assert -1 == cache.get(2)
    assert 3 == cache.get(3)
    print(f"CAHCE {cache}")
    cache.put(4, 4)  # evicts key 1.
    assert -1 == cache.get(1)
    assert cache.get(3) == 3
    assert cache.get(4) == 4

def test_lfu2():
    ops = ["LFUCache", "put", "put", "get", "get", "get", "put", "put", "get", "get", "get", "get"]
    args = [[3], [2, 2], [1, 1], [2], [1], [2], [3, 3], [4, 4], [3], [2], [1], [4]]

    for op, arg in zip(ops, args):
        if op == "LFUCache":
            c = LFUCache(*arg)
        elif op == "put":
            c.put(*arg)
        elif op == "get":
            c.get(*arg)

def test_lfu3():
    ops = ["LFUCache", "put", "get"]
    args = [[0], [0, 0], [0]]

    for op, arg in zip(ops, args):
        if op == "LFUCache":
            c = LFUCache(*arg)
        elif op == "put":
            c.put(*arg)
        elif op == "get":
            c.get(*arg)


def run_test(ops, args, expected=None, verbose=True, which_flu=0):
    for idx, (op, arg) in enumerate(zip(ops, args)):
        if verbose:
            print("  instruction:", op, arg, expected[idx] if expected else None)
        if op == "LFUCache":
            c = LFUCache(*arg) if which_flu == 0 else LFUCache1(*arg)
        elif op == "put":
            c.put(*arg)
        elif op == "get":
            if expected:
                assert expected[idx] == c.get(*arg)
            else:
                c.get(*arg)
        if verbose:
            print(c)


def test_lfu4():
    run_test(["LFUCache", "put", "put", "put", "put", "get", "get"],
             [[2, True], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]],
             [None, None, None, None, None, -1, 3])


def test_lfu_0(benchmark):
    """test the speed of submitted with DLL"""
    from slow_testcase import ops, args

    benchmark(run_test, ops, args, None, False)

def test_lfu_1(benchmark):
    """test the speed of submitted with DLL"""
    from slow_testcase import ops, args

    benchmark(run_test, ops, args, None, False, 1)



class Timer:
    def __enter__(self):
        self.start = time.monotonic()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Timing {time.monotonic() - self.start}")

if __name__ == "__main__":
    from slow_testcase import ops, args
    print(len(ops), len(args))

    with Timer():
        run_test(ops, args, None, False)
