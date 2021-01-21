import logging
import sys
import collections

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger("ex1")


class LoggingDict(dict):
    def __setitem__(self, key, value):
        log.info("Setting %r to %r" % (key, value))
        super().__setitem__(key, value)


l = LoggingDict()
l[1] = 2


class LoggingOD(LoggingDict, collections.OrderedDict):
    pass


LoggingOD.mro()
