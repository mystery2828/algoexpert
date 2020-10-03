'''
Given a Binary Tree return the sum of each branches in an array.

'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def branchsum(root):
    sums = []
    helper(root, 0, sums)
    return sums

def helper(node, runningSum, sums):
    if not node:
        return 
    newRunningSum = runningSum + node.val
    if not node.left and not node.right:
        sums.append(newRunningSum)
        return 
    
    helper(node.left, newRunningSum, sums)
    helper(node.right, newRunningSum, sums)

N = Node(10)
N.left =  Node(5)
N.right = Node(15)
N.left.left = Node(2)
N.left.right = Node(5)
N.right.left = Node(13)
N.right.right = Node(22)
N.left.left.left = Node(1)
N.right.left.right = Node(14)
print(branchsum(N))