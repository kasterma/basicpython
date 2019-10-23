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
    def __init__(self, debug=False):
        self.debug = debug

    def minCameraCover(self, root: TreeNode) -> int:
        rv = self.minCameraCover_h(root)
        return rv[0] if rv[0] > 0 else 1

    def minCameraCover_h(self, root) -> (int, int):
        "Returns count needed for tree below root, and if below root is already monitored"
        if root is None:
            return (0, 1)
        rv1 = self.minCameraCover_h(root.left)
        rv2 = self.minCameraCover_h(root.right)
        if rv1[1] > 0 and rv2[1] > 0:
            return (rv1[0] + rv2[0], max(rv1[1], rv2[1]) - 1)
        else:
            return (rv1[0] + rv2[0] + 1, 2)


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

def test3():
    # selfmade test
    in3 = [0, 0, 0, 0, 0, 0, 0]
    t3 = TreeNode.createTree(in3)
    print(repr(t3))
    assert Solution(True).minCameraCover(t3) == 2

def test4():
    in4 = [0]
    t4 = TreeNode.createTree(in4)
    print(repr(t4))
    assert Solution(True).minCameraCover(t4) == 1

def test5():
    in5 = [0,0,None,None,0,0,None,None,0,0]
    t5 = TreeNode.createTree(in5)
    print(repr(t5))
    assert Solution(True).minCameraCover(t5) == 2
