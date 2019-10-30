from builtins import len

def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    print(phone_book)
    dic = {}
    for p in phone_book:
        if p[0] not in dic:
            dic[p[0]] = Tree()
        tree = dic[p[0]]
        if tree.find(p):
            return False
    return True

class Node:
    def __init__(self, data):
        self.children = []
        self.data = data

class Tree:
    def __init__(self):
        self.root = None

    def find(self, value):
        if self.root is None:
            self.root = Node(value[0])
            self._add(self.root, value[1:])
            return False
        return self._find(self.root, value[1:])


    def _find(self, node, value):
        if 0 == len(node.children):
            self._add(node, value)
            return True
        for child in node.children:
            if child.data == value[0]:
                return self._find(child, value[1:])
        self._add(node, value)
        return False

    def _add(self, node, value):
        if 0 == len(value):
            return
        child = Node(value[0])
        node.children.append(child)
        self._add(child, value[1:])