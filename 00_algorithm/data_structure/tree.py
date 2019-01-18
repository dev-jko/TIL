class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def preorder(tree):
    if tree == None:
        return
    print(tree.data)
    preorder(tree.left)
    preorder(tree.right)


def inorder(tree):
    if tree == None:
        return
    print(tree.data)
    inorder(tree.left)
    inorder(tree.right)


def postorder(tree):
    if tree == None:
        return
    postorder(tree.left)
    postorder(tree.right)
    print(tree.data)


def levelorder(tree, level_queue):
    level_queue.append(tree)
    while len(level_queue) > 0:
        temp = level_queue.pop(0)
        print(temp.data)
        if temp.left != None:
            level_queue.append(temp.left)
        if temp.right != None:
            level_queue.append(temp.right)


root = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, Tree(6), Tree(7)))
print('\npre')
preorder(root)
print('\nin')
inorder(root)
print('\npost')
postorder(root)
print('\nlevel')
queue = []
levelorder(root, queue)



class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return not self.root == None

    def _insert_value(self, node, data):
        if node is None:
            node = Tree(data)
        else:
            if node.data <= data:
                node.right = self._insert_value(node.right, data)
            else:
                node.left = self._insert_value(node.left, data)
        return node


    def find(self, key):
        return self._find_key(self.root, key)

    def _find_key(self, node, key):
        if node == None:
            return False
        if node.data == key:
            return True
        if node.data <= key:
            return self._find_key(node.right, key)
        else:
            return self._find_key(node.left, key)
        

    def delete(self, key):
        return self._delete_value(self.root, key)

    def _delete_value(self, node, key):
        if node == None:
            return False
        if node.data == key:

            if node.left and node.right:
                # 자식이 2 모두 있을떄

            elif node.left != None:
                node = node.left
            elif node.right != None:
                node = node.right
            else:
                node = None
            return True
        elif node.data <= key:
            return self._delete_value(node.right, key)
        else:
            return self._delete_value(node.left, key)



    