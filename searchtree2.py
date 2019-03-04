import unittest


class T1:
    @classmethod
    def __call__(self, *args, **kwargs):
        print("called")
        return 2


class T2:
    pass

T2.__call__ = lambda x: 3

T2()


class T3:
    @staticmethod
    def __call__(*args, **kwargs):
        print(333)


class CC(type):
    def __call__(cls, *args, **kwargs):
        cls.c__call__(cls, *args, **kwargs)


class T4(metaclass=CC):
    def c__call__(self, *args, **kwargs):
        print('yoyoyo')

T4()


class SearchTree(metaclass=CC):
    ET = None

    def c__call__(cls, *, key=None, val=None):
        if key is None:
            assert(val is None)
            if cls.ET is None:
                cls.ET = EmptySearchTree()
            return cls.ET
        else:
            assert(val is not None)
            return NonEmptySearchTree(key=key, val=val)


class EmptySearchTree(SearchTree):
    @staticmethod
    def insert(key, val):
        return SearchTree(key=key, val=val)

    @staticmethod
    def find(key):
        return None

    def __repr__(self):
        return "EmptyTree"


class NonEmptySearchTree(SearchTree):
    def __init__(self, key: int, val: int, *, left: SearchTree = EmptySearchTree(),
                 right: SearchTree = EmptySearchTree()):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def insert(self, key, val):
        """
        Insert the value at the key in the search tree.  As much of the tree as possible is shared, but the original
        tree is unaffected.
        """
        if self.key == key:  # overwrite value if key is given with a new value
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
        self.assertEqual(SearchTree.new_empty_tree().find(1), None)
        t0 = SearchTree.new_tree(1, 33)
        self.assertEqual(t0.find(1), 33)
        t1 = SearchTree.new_empty_tree()
        t1 = t1.insert(1, 2)
        t1 = t1.insert(2, 22)
        self.assertEqual(t1.find(1), 2)
        self.assertEqual(t1.find(2), 22)
        print(repr(t1))