#Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.val}, {self.left}, {self.right})"

    @staticmethod
    def createTree(l: List) -> 'TreeNode':
        # No empty trees since number notes >= 1
        r = TreeNode(l.pop(0))
        s = [(r, 'left'), (r, 'right')]
        while len(l) > 0:
            print(f"{l} : {s}")
            v = l.pop(0)
            a = s.pop(0)
            if v is not None:
                if a[1] == 'left':
                    nn = a[0].left = TreeNode(v)
                elif a[1] == 'right':
                    nn = a[0].right = TreeNode(v)
                else:
                    raise Exception("stack error")
                s.extend([(nn, 'left'), (nn, 'right')])

        return r


class Solution:
    def __init__(self, debug):
        self.debug = debug

    def minCameraCover(self, root: TreeNode) -> int:
        pass


def test1():
    in1 = [0, 0, None, 0, 0]
    t1 = TreeNode.createTree(in1)
    print(repr(t1))
    assert Solution(True).minCameraCover(t1) == 1

def test2():
    in2 = [0, 0, None, 0, None, 0, None, None, 0]
    t2 = TreeNode.createTree(in2)
    print(repr(t2))
    assert Solution(True).minCameraCover(t2) == 2
