# btree

import unittest
import logging

logging.basicConfig(level=logging.DEBUG)


class BTriple:
    def __init__(self, key, val, down):
        self.key = key
        self.val = val
        self.down = down


class BTree:
    """BTree implementation

    Note the keys are kept in increasing order in the node"""
    log = logging.getLogger("BTree")

    def __init__(self, *, key=None, val=None):
        self.log.debug(f"New btree with key={key} and val={val}.")
        self.dat = []
        if key is not  None:
            if val is None:
                self.log.error(f"key ({key}) is not None, but val is")
            self.dat.append(BTriple(key, val, None))

    def check_invariant(self):
        """check keys are increasing"""
        pass

    def find(self, key):
        for bt in self.dat:
            self.log.debug(bt.key)
            if bt.key == key:
                return bt.val
            elif key < bt.key:
                if bt.down is None:
                    return None
                else:
                    return bt.down.find(key)

    def insert(self, key, val):
        idx = 0
        while idx < len(self.dat) and key > self.dat[idx].key:
            idx += 1
        # We now have key <= self.dat[idx].key
        if idx < len(self.dat) and key == self.dat[idx].key:
            self.dat[idx].val = val
        else:
            self.dat.insert(idx, BTriple(key, val, None))
        # now rebalance

    def __repr__(self):
        return "[" + ", ".join([repr(bt.key) + "::" + repr(bt.val) for bt in self.dat]) + "]"


class TestBTree(unittest.TestCase):
    log = logging.getLogger("TestBTree")

    def test_init(self):
        self.log.info("testinit")
        empty_btree = BTree()
        self.assertEqual(empty_btree.dat, [])
        btree1 = BTree(key=1, val=2)
        self.assertTrue(len(btree1.dat) == 1)
        self.assertEqual(btree1.find(1), 2)
        btree1.insert(1, 22)
        self.assertEqual(btree1.find(1), 22)
        btree1.insert(2, 33)
        self.log.info(btree1)
        self.assertEqual(btree1.find(2), 33)




