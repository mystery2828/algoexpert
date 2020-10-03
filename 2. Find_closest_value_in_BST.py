'''
Given a value K and a Binary Search Tree BST find the node whose value is close to the given value K
The node's value can be equal to the value of K.

'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

mini = float("infinity")
ele = None
def findLeast(node, K):
    global mini,ele
    if not node:
        return 
    
    if abs(K-node.val) < mini:
        mini = abs(K-node.val)
        ele = node.val
    
    if mini==0:
        return 'Found --> {}'.format(K)
    
    if node.val < K:
        findLeast(node.right, K)
    else:
        findLeast(node.left, K)
    return 'Found --> {}'.format(ele)

K = 12
N = Node(10)
N.left =  Node(5)
N.right = Node(15)
N.left.left = Node(2)
N.left.right = Node(5)
N.right.left = Node(13)
N.right.right = Node(22)
N.left.left.left = Node(1)
N.right.left.right = Node(14)
print(findLeast(N,K))