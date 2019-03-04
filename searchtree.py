import unittest


class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class A(metaclass=Singleton):
    pass


class B(metaclass=Singleton):
    pass


class C(metaclass=Singleton):
    __instances = {}

a = A()
b = B()
c = C()


class SearchTree:
    @staticmethod
    def tree(key=None, val=None):
        if key is None:
            assert(val is None)
            return EmptySearchTree()
        else:
            assert(val is not None)
            return NonEmptySearchTree(key=key, val=val)


class EmptySearchTree(SearchTree, metaclass=Singleton):
    @staticmethod
    def insert(key, val):
        return SearchTree.tree(key=key, val=val)

    @staticmethod
    def find(key):
        return None

    def __repr__(self):
        return "EmptyTree"


class NonEmptySearchTree(SearchTree):
    def __init__(self, key: int, val: int, *, left: SearchTree=EmptySearchTree(), right: SearchTree=EmptySearchTree()):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def insert(self, key, val):
        """
        Insert the value at the key in the search tree.  As much of the tree as possible is shared, but the original
        tree is unaffected.
        """
        if self.key == key:   # overwrite value if key is given with a new value
            return NonEmptySearchTree(key=self.key, val=val, left=self.left, right=self.right)
        elif self.key > key:
            return NonEmptySearchTree(key=self.key, val=self.val, left=self.left.insert(key, val), right=self.right)
        else:
            return NonEmptySearchTree(key=self.key, val=self.val, left=self.left, right=self.right.insert(key, val))

    def find(self, key):
        if self.key == key:
            return self.val
        elif self.key > key:
            return self.left.find(key)
        else:
            return self.right.find(key)

    def __repr__(self):
        return f"Tree({self.key}->{self.val}, [{repr(self.left)}][{repr(self.right)}])"


class TestSearchTree(unittest.TestCase):
    def test_basics(self):
        self.assertEqual(SearchTree.tree().find(1), None)
        t0 = SearchTree.tree(1, 33)
        self.assertEqual(t0.find(1), 33)
        t1 = SearchTree.tree()
        t1 = t1.insert(1, 2)
        t1 = t1.insert(2, 22)
        t1 = t1.insert(0, 11)
        self.assertEqual(t1.find(1), 2)
        self.assertEqual(t1.find(2), 22)
        print(repr(t1))