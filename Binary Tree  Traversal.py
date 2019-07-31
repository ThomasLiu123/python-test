class Node:
#Class 初始化
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
#Class 初始化
    def __init__(self, root):
        self.root = Node(root)
#Print Tree Function
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            print (self.preorder_print(tree.root, ""))
        elif traversal_type == "inorder":
            print (self.inorder_print(tree.root, ""))
        elif traversal_type == "postorder":
            print (self.postorder_print(tree.root, ""))
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
#前序 Function
    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-->")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
#中序 Function
    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-->")
            traversal = self.inorder_print(start.right, traversal)
        return traversal
#後序 Function
    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-->")
        return traversal

#     Binary Tree
#          1
#        /   \
#       2     3
#      / \    / \
#     4   5  6   7


#Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
#Print Traversal
tree.print_tree("preorder")
tree.print_tree("inorder")
tree.print_tree("postorder")
