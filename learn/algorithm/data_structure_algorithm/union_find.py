class Node:
    def __init__(self, data):
        self.data = data
        self.parent = self

    def __repr__(self):
        return str(self.data)


def find(node):
    if node.parent == node:
        return node
    node.parent = find(node.parent)
    return node.parent


def union(node1, node2):
    p1 = find(node1)
    p2 = find(node2)
    if p1 == p2:
        return
    p1.parent = p2


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
union(node1, node2)
print(node1.parent, node2.parent)
union(node1, node3)
print(node1.parent, node2.parent, node3.parent)
find(node1)
print(node1.parent, node2.parent, node3.parent)
