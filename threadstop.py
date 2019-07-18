# quick experiment in stopping threads
import time
from functools import wraps
from threading import Thread

import six


class Task(Thread):
    """
    The Threaded object returned by the @threaded decorator below
    """

    def __init__(self, method, *args, **kwargs):
        super(Task, self).__init__()
        self.method = method
        self.name = 'DEVaultThread'
        self.args = args
        self.kwargs = kwargs
        self._result = None
        self.__exc_info = None

    def run(self):
        try:
            self._result = self.method(*self.args, **self.kwargs)
        except:
            self.__exc_info = sys.exc_info()

    @property
    def result(self):
        self.join()
        if self.__exc_info is not None:
            six.reraise(*self.__exc_info)
        return self._result


def threaded(function=None, daemon=False):
    """Decorator for making a method call into a threaded background taks.

    Use this for e.g. a thread in the background that keeps checking on a configuration or secrets server to see if the
    configuration or secrets have been updated.
    """

    def wrapper_factory(func):
        @wraps(func)
        def get_thread(*args, **kwargs):
            t = Task(func, *args, **kwargs)
            if daemon:
                t.daemon = True
            t.start()
            return t

        return get_thread

    if function:
        return wrapper_factory(function)
    else:
        return wrapper_factory


class T:
    def __init__(self):
        self.running = False

    @threaded
    def print_2(self):
        if self.running:
            print("already running")
            return

        self.running = True

        while self.running:
            print(2)
            time.sleep(10)

        print("done done")

    def stop(self):
        self.running = False
