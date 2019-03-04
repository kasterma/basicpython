"""Huet's Zipper basic implementation"""

import unittest
import logging
import logging.config
import yaml

with open("tree_zipper_logging.yaml") as log_conf_file:
    log_conf = yaml.load(log_conf_file)
logging.config.dictConfig(log_conf)
log = logging.getLogger("tree_zipper")


class Tree:
    def __init__(self, val: int, children=None):
        self.val = val
        if children is None:
            self.children = []
        else:
            self.children = children

    def __repr__(self):
        children_str = ",".join([repr(ch) for ch in self.children])
        if len(children_str) > 0:
            children_str = "->" + children_str
        return f"({self.val}{children_str})"

    def __eq__(self, other):
        return (self.val == other.val and
                len(self.children) == len(other.children) and
                all(self.children[i] == other.children[i] for i in range(len(self.children))))


class Path:
    def __init__(self, val, larger_siblings, up, smaller_siblings):
        self.val = val
        self.larger_siblings = larger_siblings
        self.up = up
        self.smaller_siblings = smaller_siblings

    def __repr__(self):
        return f"P({self.val}, {self.larger_siblings}, {self.up}, {self.smaller_siblings})"


class Location:
    """Current focus in a tree.

    A location is a current subtree of focus stored in tree, and the information to rebuild the full tree from it in
    path.

    Note: no proper error handling; if an operation is not possible just return self"""

    def __init__(self, tree, path=None):
        self.tree = tree
        self.path = path

    def update(self, f):
        return Location(f(self.tree), self.path)

    def down(self):
        if len(self.tree.children) == 0:
            return self
        else:
            return Location(self.tree.children[0], Path(self.tree.val, [], self.path, self.tree.children[1:]))

    def up(self):
        p = self.path
        if p is None:
            return self
        else:
            return Location(Tree(p.val, p.larger_siblings + [self.tree] + p.smaller_siblings),
                            p.up)

    def right(self):
        if self.path.smaller_siblings:
            p: Path = self.path
            path = Path(p.val, p.larger_siblings + [self.tree], p.up, p.smaller_siblings[1:])
            return Location(p.smaller_siblings[0], path)
        else:
            return self

    def left(self):
        if self.path.larger_siblings:
            p: Path = self.path
            path = Path(p.val, p.larger_siblings[:-1], p.up, [self.tree] + p.smaller_siblings)
            return Location(p.larger_siblings[-1], path)

    def to_tree(self):
        u = self.up()
        if u.path is None:
            return u.tree
        else:
            return u.to_tree()

    def __repr__(self):
        return f"L({self.tree}, {self.path})"


class T1(unittest.TestCase):
    log = logging.getLogger("T1")

    @staticmethod
    def f(t: Tree):
        return Tree(99, t.children)

    def test_tree(self):
        t1 = Tree(3, [Tree(1), Tree(5)])
        self.assertEqual(repr(t1), "(3->(1),(5))")
        self.assertTrue(t1 == t1)
        self.assertFalse(t1 == Tree(3))
        self.assertFalse(t1 == Tree(3, [Tree(1)]))
        self.assertFalse(t1 == Tree(3, [Tree(5), Tree(1)]))
        self.assertEqual(self.f(t1), Tree(99, [Tree(1), Tree(5)]))

    def test1(self):
        t1 = Tree(3, [Tree(1), Tree(5)])
        self.log.info(t1)

        l1 = Location(t1)
        self.log.info(l1)

        self.log.info(l1.down())
        self.log.info(l1.down().down())

        l2 = l1.down()
        l3 = l2.right()
        self.log.info(l3)
        self.log.info(l3.left())
        l3.to_tree()
        self.log.info(repr(l3.to_tree()))
