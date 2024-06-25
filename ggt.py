class TreeNode:
    def __init__(self,key):
        self.left = Node
        self.right = Node
        self.val = key
class BinarySearchTree:
    def __init__(self):
        self.root = Node
    def insert(self, key):
        self.root = self._insert(self.root, key)
    def_insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.val:
            root.left = self._insert(root.left, key)
        elif key > root.val:
            root.right = self._insert(root.right, key)
        return root
    def in order traversal(self. root):
        if root:
            self in order traversal(root.left)
            print(root.val, end=" ")
            self.in_order_traversal(root.right)
    def pre_order_traversal(self, root):
        if root:
            print(root.val,end=" ")
            self.pre_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(root.val, end=" ")\