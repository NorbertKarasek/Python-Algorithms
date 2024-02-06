class BinaryTree:
    def __init__(self,value):
        self.key = value
        self.left_child = None
        self.right_child = None

    def insert_left(self,value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree

    def insert_right(self,value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree

    def bredth_first_search(self,n):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.key == n:
                    return True
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
            current = next
            next = []
        return False

    def show_nodes(self):
        current = [self]
        next = []
        list = []
        while current:
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
                list.append(node.key)
            current = next
            next = []
        return list

    def invert(self):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
                temp = node.left_child
                node.left_child = node.right_child
                node.right_child = temp
            current = next
            next = []

    def invert_rec(self):
        if self:
            change = self.left_child
            self.left_child = self.right_child
            self.right_child = change
            invert_rec(self.left_child)
            invert_rec(self.right_child)

    def has_leaf_nodes(self):
        if self.left_child or self.right_child:
            return True
        else:
            return False



tree = BinaryTree(1)
tree.insert_left(4)
tree.insert_left(2)
tree.insert_right(6)
tree.insert_right(3)
tree.right_child.insert_left(5)
tree.right_child.left_child.insert_left(7)
tree.right_child.left_child.insert_right(8)

#funkcje przeszukiwania wszerz
print('------------\nPREORDER')

def preorder(tree):
    if tree:
        print(tree.key)
        preorder(tree.left_child)
        preorder(tree.right_child)

preorder(tree)
print('-------------\nPOSTORDER')

def postorder(tree):
    if tree:
        postorder(tree.left_child)
        postorder(tree.right_child)
        print(tree.key)

postorder(tree)
print('--------------\nINORDER')

def inorder(tree):
    if tree:
        inorder(tree.left_child)
        print(tree.key)
        inorder(tree.right_child)

inorder(tree)

print('-------------\n INVERTED PREORDER')
tree.invert()
preorder(tree)

print('---------------\nrecursively invert')
def invert_rec(tree):
    if tree:
        change = tree.left_child
        tree.left_child = tree.right_child
        tree.right_child = change
        invert_rec(tree.left_child)
        invert_rec(tree.right_child)

invert_rec(tree)
preorder(tree)

print(tree.has_leaf_nodes())
print(tree.show_nodes())