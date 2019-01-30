#1991 트리순회
'''
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        
class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node
    
    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)
        
    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                # replace the node to the leftmost of node.right
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted
    
    def pre_order_traversal(self):
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                print(root.data)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self.root)

    def in_order_traversal(self):
        def _in_order_traversal(root):
            if root is None:
                pass
            else:
                _in_order_traversal(root.left)
                print(root.data)
                _in_order_traversal(root.right)
        _in_order_traversal(self.root)

    def post_order_traversal(self):
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                print(root.data)
        _post_order_traversal(self.root)
        
    def level_order_traversal(self):
        def _level_order_traversal(root):
            queue = [root]
            while queue:
                root = queue.pop(0)
                if root is not None:
                    print(root.data)
                    if root.left:
                        queue.append(root.left)
                    if root.right:
                        queue.append(root.right)
        _level_order_traversal(self.root)

array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinarySearchTree()
for x in array:
    bst.insert(x)


# Find
print(bst.find(15)) # True
print(bst.find(17)) # False

# Delete
print(bst.delete(55)) # True
print(bst.delete(14)) # True
print(bst.delete(11)) # False

# depth first
bst.pre_order_traversal()   # 40 4 34 14 13 15 45 55 48 47 49
bst.in_order_traversal()    # 4 13 14 15 34 40 45 47 48 49 55
bst.post_order_traversal()  # 13 15 14 34 4 47 49 48 55 45 40
# breadth first
bst.level_order_traversal() # 40 4 45 34 55 14 48 13 15 47 49
'''
'''
p='ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:int(input())]
l=[];ll=[];lll=[];pre=[];order=[];post=[];left=[];right=[]
for i in'a'*len(p):
    a,b,c=map(str,input().split())
    if a not in pre:
        pre+=[a]
    if b not in pre and b!='.':
        pre+=[b]
    if a!='A' and l.count(a)==0:
        for _ in l[::-1]:
            if _ not in order and _!='.':
                order+=[_]
    l+=[a]
    if [b]!='.':l+=[b]
    #print(c)
    if [c]!='.':ll+=[c]
    k=[a,b,c]
    if k.count('.')!=0:
        for _ in k[::-1]:
            if _ not in post and _!='.':
                post+=[_]
    else:lll+=[a]+[b]+[c]
    #ll+=[[a,b],[a,c]]
#print(ll)
if len(order)!=len(p):
    for _ in ll:
        if _ not in order and _!='.':
            order+=[_]
if len(post)!=len(p):
    for _ in lll[::-1]:
        if _ not in post and _!='.':
            post+=[_]
#print(l,pre,left,right,sep='\n')
print(*pre,sep='')
print(*order,sep='')
print(*post,sep='')
'''

d={};i=1
for i in range(int(input())):
    s=input()
    d[s[0]]=s[2],s[4]
pre=""
cur=""
post=""
def r(n):
    global pre,cur,post,d,i
    if n==".":return
    i+=1
    print('start',i,pre,cur,post)
    pre+=n;
    r(d[n][0])
    cur+=n
    r(d[n][1])
    post+=n
    print('end',i,pre,cur,post)
r("A")
print(pre)
print(cur)
print(post)
