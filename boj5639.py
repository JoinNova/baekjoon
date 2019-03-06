#boj5639 이진검색 트리
#by qtyp456987
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

arr = []

def postorder(root, end):
    if root >= end:
        return
    right = root + 1
    for i in range(root + 1, end):
        if arr[root] < arr[i]:
            right = i
            break
    postorder(root + 1, right)
    postorder(right, end)
    print(arr[root])

for v in map(int, sys.stdin.read().split()):
    arr.append(v)
if len(arr) > 0:
    postorder(0, len(arr))

#by y305205
import sys;sys.setrecursionlimit(50000)
R=[]
def hui(s,e):
    if s==e: return
    root=R[s]
    i=s+1
    while i<e and R[i]<root: i+=1
    hui(s+1,i)
    hui(i,e)
    print(root)
try:
    while True:
        n = int(input())
        R.append(n)
except:
    pass
hui(0,len(R))


#by axcee
import sys; input = lambda: sys.stdin.readline().rstrip()

def sol(pre) :
    res = []
    st = [(0, len(pre))]
    while len(st) :
        lo, hi = st.pop()
        if lo == hi :
            continue
        res.append(pre[lo])
        d = lo+1
        while d < hi and pre[d] < pre[lo] :
            d += 1
        st.append((lo+1, d))
        st.append((d, hi))
    return res[::-1]

p = []
while True :
    inp = input()
    if not inp :
        break
    p.append(int(inp))
r = sol(p)
for i in r :
    print(i)

'''
#by sait2000
import sys
sys.setrecursionlimit(9**9)
a=[*map(int,sys.stdin.read().split())]
def f(i,j):
    if i<j:
        l=i+1;h=j
        while l<h:
            m=l+h>>1
            if a[m]>a[i]:h=m
            else:l=m+1
        f(i+1,l);f(l,j);print(a[i])
f(0,len(a))
'''
'''
#by yskang

import sys

sys.setrecursionlimit(10 ** 6)

read_single_int = lambda: int(sys.stdin.readline().strip())


def pre_order_2_post_order(pre_order: list, start: int, end: int):
    if start >= end:
        return

    root = pre_order[start]
    point = start+1

    for i, n in enumerate(pre_order[start+1:end], start+1):
        if n > root:
            point = i
            break

    pre_order_2_post_order(pre_order, start+1, point)
    pre_order_2_post_order(pre_order, point, end)
    print(root)
    return


def solution(pre_order: list):
    pre_order_2_post_order(pre_order, 0, len(pre_order))
    return


def main():
    pre_order = []
    while True:
        try:
            pre_order.append(read_single_int())
        except:
            break
    solution(pre_order)


if __name__ == '__main__':
    main()


#by cprayer
import sys

def dfs(pos, min_v):
    ret = 0
    if pos + 1 < len(orders) and orders[pos] > orders[pos + 1]:
        ret += dfs(pos + 1, min(min_v, orders[pos]))
    if pos + ret + 1 < len(orders) and orders[pos] < orders[pos + ret + 1] \
        and orders[pos + ret + 1] < min_v:
        ret += dfs(pos + ret + 1, min_v)
    print(orders[pos])
    return ret + 1

sys.setrecursionlimit(10009)

orders = []
for v in map(int, sys.stdin.read().split()):
    orders.append(v)
dfs(0, 0x3c3c3c3c)

#by anyj0527
import sys
sys.setrecursionlimit(10100)

def printPostOrder(preorder):
    if len(preorder) == 0:
      return
    if len(preorder) == 1:
      print(preorder[0])
      return
    root = preorder[0]
    rightTreeIdx = -1
    for i in range(1, len(preorder)):
      if preorder[i] > root:
        rightTreeIdx = i
        break
    if rightTreeIdx != -1:
      printPostOrder(preorder[1:rightTreeIdx])
      printPostOrder(preorder[rightTreeIdx:])
    else:
      printPostOrder(preorder[1:])
    print(root)
    
def main():
  tree = sys.stdin.readlines()
  for i in range(len(tree)):
        tree[i] = int(tree[i])

 
  printPostOrder(tree)

main()

'''

'''
#by ggbbng
class Node:
    def __init__(self, n, min, max):
        self.n = n
        self.min = min
        self.max = max
        self.left = None
        self.right = None
        self.parent = None

    def append_left(self, left):
        # print("Attach ", left, " on the left of ", self)
        self.left = left
        left.parent = self

    def append_right(self, right):
        # print("Attach ", right, " on the right of ", self)
        self.right = right
        right.parent = self

    def __repr__(self):
        return str(self.n)


def post_order(node):
    stack = [node]
    while stack:
        node = stack.pop()
        if not node.left and not node.right:
            print(node.n)
        else:
            left = node.left
            right = node.right
            node.left = None
            node.right = None
            stack.append(node)

            if right:
                stack.append(right)
            if left:
                stack.append(left)

data = []
while True:
    try:
        data.append(int(input()))
    except:
        break

root = Node(data[0], 0, int(1e9))
current = root

for n in data[1:]:
    while n < current.min or n > current.max:
        current = current.parent

    if n < current.n:
        node = Node(n, current.min, current.n - 1)
        current.append_left(node)
    else:
        node = Node(n, current.n + 1, current.max)
        current.append_right(node)
    current = node

post_order(root)
'''
'''
#by tjdgns8047(fixed by Nova)
import sys
sys.setrecursionlimit(150000)
class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None
    
    def get(self):
        return self.val
    
    def set(self, val):
        self.val = val
        
    def getChildren(self):
        children = []
        if(self.leftChild != None):
            children.append(self.leftChild)
        if(self.rightChild != None):
            children.append(self.rightChild)
        return children

    def print_tree(self):
        if self.leftChild:
            self.leftChild.print_tree()
        if self.rightChild:
            self.rightChild.print_tree()
        print(self.val)
        
class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def insert(self, val):
        if(self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if(val <= currentNode.val):
            if(currentNode.leftChild):
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        elif(val > currentNode.val):
            if(currentNode.rightChild):
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)

    def find(self, val):
        return self.findNode(self.root, val)

    def findNode(self, currentNode, val):
        if(currentNode is None):
            return False
        elif(val == currentNode.val):
            return True
        elif(val < currentNode.val):
            return self.findNode(currentNode.leftChild, val)
        else:
            return self.findNode(currentNode.rightChild, val)

    

bst = BST()

# Insert value
while True:
    try:
        bst.insert(int(input()))
    except EOFError:
        break
bst.root.print_tree()
'''
