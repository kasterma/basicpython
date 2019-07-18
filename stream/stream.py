import itertools
import logging
import yaml
from logging.config import dictConfig

with open("stream/logging.yaml") as f:
    d = yaml.safe_load(f)
    dictConfig(d)

log = logging.getLogger("stream")


class Source:
    def __init__(self):
        self.next = 0

    def __next__(self):
        val = self.next
        self.next += 1
        log.info(f"Source: {val}")
        return val


class Group:
    def __init__(self, size, src):
        self.src = src
        self.size = size

    def __next__(self):
        buf = [next(self.src) for _ in range(self.size)]
        log.info(f"Group: {buf}")
        return buf


g = Group(3, Source())
