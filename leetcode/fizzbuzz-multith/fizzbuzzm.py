import threading
from typing import Callable


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.cur = 1
        self.lock = threading.Lock()

    # printFizz() outputs "fizz"
    def fizz(self, _print: 'Callable[[], None]') -> None:
        while True:
            with self.lock:
                if self.cur > self.n:
                    break
                if self.cur % 3 == 0 and self.cur % 5 != 0:
                    _print()
                    self.cur += 1

    # printBuzz() outputs "buzz"
    def buzz(self, _print: 'Callable[[], None]') -> None:
        while True:
            with self.lock:
                if self.cur > self.n:
                    break
                if self.cur % 3 != 0 and self.cur % 5 == 0:
                    _print()
                    self.cur += 1

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, _print: 'Callable[[], None]') -> None:
        while True:
            with self.lock:
                if self.cur > self.n:
                    break
                if self.cur % 3 == 0 and self.cur % 5 == 0:
                    _print()
                    self.cur += 1

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, _print: 'Callable[[int], None]') -> None:
        while True:
            with self.lock:
                if self.cur > self.n:
                    break
                if self.cur % 3 != 0 and self.cur % 5 != 0:
                    _print(self.cur)
                    self.cur += 1

def run():
    fb = FizzBuzz(15)
    t1 = threading.Thread(target=lambda: fb.buzz(lambda: print("buzz")))
    t2 = threading.Thread(target=lambda: fb.fizz(lambda: print("fizz")))
    t3 = threading.Thread(target=lambda: fb.fizzbuzz(lambda: print("fizzbuzz")))
    t4 = threading.Thread(target=lambda: fb.number(lambda n: print(n)))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()

if __name__ == "__main__":
    run()
