import random


class Node:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
        self.p = random.random()
        self.count_sub_node = 1


def merge(l, r):
    if l is None:
        return r
    if r is None:
        return l
    if l.p < r.p:
        l.right = merge(l.right, r)
        update_count_sub_node(l)
        return l
    else:
        r.left = merge(l, r.left)
        update_count_sub_node(r)
        return r


def split(node, x):
    if node is None:
        return None, None
    if node.value < x:
        l, r = split(node.right, x)
        node.right = l
        update_count_sub_node(node)
        return node, r
    else:
        l, r = split(node.left, x)
        node.left = r
        update_count_sub_node(node)
        return l, node


def find(node, x):
    if node is None:
        return None
    if node.value == x:
        return node
    elif node.value < x:
        return find(node.right, x)
    else:
        return find(node.left, x)


def update_count_sub_node(self):
    if self is not None:
        self.count_sub_node = 1
        if self.left is not None:
            self.count_sub_node += self.left.count_sub_node
        if self.right is not None:
            self.count_sub_node += self.right.count_sub_node



class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        l, r = split(self.root, value)
        self.root = merge(merge(l, Node(value)), r)

    def remove(self, value):
        l1, r1 = split(self.root, value)
        l2, r2 = split(r1, value + 1)
        self.root = merge(l1, r2)
        update_count_sub_node(self.root)

    def find_k_max(self, value):
        node = self.root
        while node is not None:
            cnt_sub_node_r = 0
            if node.right is not None:
                cnt_sub_node_r = node.right.count_sub_node
            if cnt_sub_node_r + 1 == value:
                return node.value
            if value <= cnt_sub_node_r:
                node = node.right
            else:
                node = node.left
                value -= cnt_sub_node_r + 1
        return None


if __name__ == '__main__':
    n = int(input())
    dTree = Tree()
    for _ in range(n):
        sgn, num = input().split()
        if sgn == '+1' or sgn == '1':
            dTree.insert(int(num))
        elif sgn == '-1':
            dTree.remove(int(num))
        else:
            print(dTree.find_k_max(int(num)))
