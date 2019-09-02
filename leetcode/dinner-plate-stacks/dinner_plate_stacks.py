import time

from heapq import heappush, heappop


class DinnerPlates1:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []

    def push(self, val: int) -> None:
        idx = 0
        while idx < len(self.stacks) and len(self.stacks[idx]) == self.capacity:
            idx += 1
        if idx == len(self.stacks):
            # add new stack
            self.stacks.append([val])
        else:
            self.stacks[idx].append(val)

    def _clean_stacks(self):
        # clean up tail of empty stacks
        while len(self.stacks) > 0 and len(self.stacks[-1]) == 0:
            self.stacks.pop()

    def pop(self) -> int:
        if len(self.stacks) == 0:
            return -1
        rv = self.stacks[-1].pop()
        self._clean_stacks()
        return rv

    def popAtStack(self, index: int) -> int:
        if index < len(self.stacks) and len(self.stacks[index]) > 0:
            rv = self.stacks[index].pop()
            self._clean_stacks()
            return rv
        else:
            return -1

    def __repr__(self):
        return f"DinnerPlates({self.capacity}, [" + ", ".join(str(s) for s in self.stacks) + "])"


def test_many_push():
    """Check that the profiling finds the search taking a long time"""

    class DinnerPlates1_pf:

        def __init__(self, capacity: int):
            self.capacity = capacity
            self.stacks = []

        def _insertpt(self):
            idx = 0
            while idx < len(self.stacks) and len(self.stacks[idx]) == self.capacity:
                idx += 1
            return idx

        def push(self, val: int) -> None:
            idx = self._insertpt()
            if idx == len(self.stacks):
                # add new stack
                self.stacks.append([val])
            else:
                self.stacks[idx].append(val)
    dp = DinnerPlates1_pf(10)
    for i in range(10_000):
        dp.push(i)
    assert len(dp.stacks) == 1000


class DinnerPlates:
    # speed up ideas:
    # 1) allocate full stacks at once  NOT ENOUGH
    # 2) don't delete once allocated, so don't have to reallocate the memory  NOT ENOUGH
    # 3) add lots of new stacks at the same time MADE SLOWER
    # 4) keep list of nonfull stacks  HARD TO GET RIGHT (off by 1 errors)
    #      use heap, and invariant to simplify.  Remove all other ideas to simplify as well

    def __init__(self, capacity: int, check_invariant=False):
        self.check_invariant = check_invariant  # bool indicating if we are computing the debugging invariant
        self.capacity = capacity
        self.stacks = []
        self.non_full_stack_indices = []  # heap of stacks indices for smaller stacks where room was made
        # the invariant shows that when we add an index and then by popping the length of stacks shrinks we don't
        # get any problems b/c we can easily detect and then empty the heap, see (**)
        self._invariant()

    def _invariant(self):
        if self.check_invariant:
            for idx in self.non_full_stack_indices:
                assert idx >= len(self.stacks) or len(self.stacks[idx]) < self.capacity
            for idx, stack in enumerate(self.stacks):
                if idx < len(self.stacks) - 1 and len(stack) < self.capacity:
                    assert idx in self.non_full_stack_indices

    def push(self, val: int) -> None:
        # noinspection PyBroadException
        try:
            idx = heappop(self.non_full_stack_indices)
        except Exception as e:
            if self.stacks and len(self.stacks[-1]) == self.capacity:
                self.stacks.append([val])
            else:
                if self.stacks:
                    self.stacks[-1].append(val)
                else:
                    self.stacks.append([val])
        else:
            if idx >= len(self.stacks):
                self.non_full_stack_indices = []  # (**)
                self.stacks.append([val])
        finally:
            self._invariant()

    def _clean_stacks(self):
        # clean up tail of empty stacks
        while self.stacks and len(self.stacks[-1]) == 0:
            self.stacks.pop()

    def pop(self) -> int:
        # noinspection PyBroadException
        try:
            return self.stacks[-1].pop()
        except Exception as e:
            return -1
        finally:
            self._clean_stacks()
            self._invariant()

    def popAtStack(self, index: int) -> int:
        # noinspection PyBroadException
        try:
            rv = self.stacks[index].pop()
        except Exception as e:
            return -1
        else:
            heappush(self.non_full_stack_indices, index)
            return rv
        finally:
            self._clean_stacks()
            self._invariant()

    def __repr__(self):
        return f"DinnerPlates({self.capacity}, [" + \
               ", ".join([str(s) for s in self.stacks]) + "])"


class DinnerPlates3:
    # with only the optimization to keep track of next insertion point

    def __init__(self, capacity: int, check_invariant=False):
        self.capacity = capacity
        self.stacks = []
        self.next_insertion = 0

    def _search_for_next_insertion(self):
        """When add element, next insertion point could become larger search for the right point"""
        while self.next_insertion < len(self.stacks) and len(self.stacks[self.next_insertion]) == self.capacity:
            self.next_insertion += 1

    def push(self, val: int) -> None:
        if self.next_insertion == len(self.stacks):
            # add new stack
            self.stacks.append([val])
        else:
            self.stacks[self.next_insertion].append(val)

        self._search_for_next_insertion()

    def _clean_stacks(self):
        # clean up tail of empty stacks
        while len(self.stacks) > 0 and len(self.stacks[-1]) == 0:
            self.stacks.pop()

    def pop(self) -> int:
        if len(self.stacks) == 0:
            return -1
        rv = self.stacks[-1].pop()
        if self.next_insertion == len(self.stacks):
            self.next_insertion -= 1
        self._clean_stacks()
        return rv

    def popAtStack(self, index: int) -> int:
        if index < len(self.stacks) and len(self.stacks[index]) > 0:
            rv = self.stacks[index].pop()
            if self.next_insertion > index:
                self.next_insertion = index
            self._clean_stacks()
            return rv
        else:
            return -1

    def __repr__(self):
        return f"DinnerPlates({self.capacity}, [" + ", ".join(str(s) for s in self.stacks) + "])"



# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


def test_dp1():
    dp = DinnerPlates(2, True)
    dp.push(1)
    assert repr(dp) == "DinnerPlates(2, [[1]])"
    dp.push(2)
    assert repr(dp) == "DinnerPlates(2, [[1, 2]])"
    dp.push(3)
    assert repr(dp) == "DinnerPlates(2, [[1, 2], [3]])"
    dp.push(4)
    assert repr(dp) == "DinnerPlates(2, [[1, 2], [3, 4]])"
    dp.push(5)
    assert repr(dp) == "DinnerPlates(2, [[1, 2], [3, 4], [5]])"

    assert dp.pop() == 5
    assert repr(dp) == "DinnerPlates(2, [[1, 2], [3, 4]])"

    assert dp.pop() == 4
    assert repr(dp) == "DinnerPlates(2, [[1, 2], [3]])"
    assert dp.popAtStack(0) == 2
    assert repr(dp) == "DinnerPlates(2, [[1], [3]])"
    assert dp.popAtStack(0) == 1
    assert repr(dp) == "DinnerPlates(2, [[], [3]])"
    assert dp.pop() == 3
    assert repr(dp) == "DinnerPlates(2, [])"


def test_dp2():
    dp = DinnerPlates(2, True)
    dp.push(1)
    assert repr(dp) == "DinnerPlates(2, [[1]])"
    dp.push(2)
    assert repr(dp) == "DinnerPlates(2, [[1, 2]])"
    dp.push(3)
    assert repr(dp) == "DinnerPlates(2, [[1, 2], [3]])"
    assert dp.popAtStack(0) == 2
    assert repr(dp) == "DinnerPlates(2, [[1], [3]])"

    assert dp.pop() == 3
    assert repr(dp) == "DinnerPlates(2, [[1]])"

    assert dp.pop() == 1
    assert repr(dp) == "DinnerPlates(2, [])"


def test_dp3():
    dp = DinnerPlates(1, True)
    dp.push(1)
    assert repr(dp) == "DinnerPlates(1, [[1]])"
    dp.push(2)
    assert repr(dp) == "DinnerPlates(1, [[1], [2]])"
    dp.push(3)
    assert repr(dp) == "DinnerPlates(1, [[1], [2], [3]])"
    assert dp.popAtStack(1) == 2
    assert repr(dp) == "DinnerPlates(1, [[1], [], [3]])"

    assert dp.pop() == 3
    assert repr(dp) == "DinnerPlates(1, [[1]])"

    assert dp.pop() == 1
    assert repr(dp) == "DinnerPlates(1, [])"


def test_dp4():
    cmds = ["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack", "popAtStack",
     "pop", "pop", "pop", "pop", "pop"]
    args = [[2], [1], [2], [3], [4], [7], [8], [20], [21], [0], [2], [], [], [], [], []]

    dp = None
    for cmd, arg in zip(cmds, args):
        print(f"Executing {cmd} {arg} with {dp}")
        if cmd == "DinnerPlates":
            dp = DinnerPlates(arg[0])
        elif cmd == "push":
            dp.push(arg[0])
        elif cmd == "popAtStack":
            r = dp.popAtStack(arg[0])
            print(f"   result: {r}")
        elif cmd == "pop":
            r = dp.pop()
            print(f"   result: {r}")
        else:
            print(f"   Error {cmd} {arg}")


class Timer:
    def __enter__(self):
        self.start = time.monotonic()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(f"Took {time.monotonic() - self.start}")


def time_test1():
    l = list(range(1_000_000))
    with Timer():
        for _ in range(100_000):
            x = l.pop()


def time_test2(s=1000):
    l = list(range(1_000_000))
    with Timer():
        for idx in range(100_000):
            l.remove(s + idx)

def time_test3():
    l = list(range(1_000_000))
    with Timer():
        for idx in range(100_000):
            l.remove(idx)


def time_test4(t=1):
    l = []

    def step1(new_len, ct):
        l.extend([[None for _ in range(new_len)] for _ in range(ct)])

    def step2(new_len, ct):
        for _ in range(ct):
            l.append([None for _ in range(new_len)])

    step = step1 if t == 1 else step2

    with Timer():
        for _ in range(1000):
            step(1000, 100)

#### todo 5 : try VS if ####################

class InsertStacks:
    """Quick stacks implementation for the two different versions of insert (if / try)"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
        self.cur_stack = 0

    def insert_if(self, val):
        if self.cur_stack < len(self.stacks):
            if len(self.stacks[self.cur_stack]) < self.capacity:
                self.stacks[self.cur_stack].append(val)
            else:
                self.stacks.append([val])
                self.cur_stack += 1
        else:
            self.stacks.append([val])

    def insert_try(self, val):
        try:
            if len(self.stacks[self.cur_stack]) < self.capacity:
                self.stacks[self.cur_stack].append(val)
            else:
                self.stacks.append([val])
                self.cur_stack += 1
        except IndexError as e:
            self.stacks.append([val])


def inserts_with_if():
    stacks = InsertStacks(5)
    for idx in range(10000):
        stacks.insert_if(idx)
    return stacks


def inserts_with_try():
    stacks = InsertStacks(5)
    for idx in range(10000):
        stacks.insert_try(idx)
    return stacks


def test_if_versus_try_if(benchmark):
    if_stacks = benchmark(inserts_with_if)
    assert len(if_stacks.stacks) == 2000


def test_if_versus_try_try(benchmark):
    try_stacks = benchmark(inserts_with_if)
    assert len(try_stacks.stacks) == 2000
