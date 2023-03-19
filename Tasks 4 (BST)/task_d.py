import random


class Node:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
        self.p = random.random()
        self.sum_branch = x


def merge(l, r):
    if l is None:
        return r
    if r is None:
        return l
    if l.p < r.p:
        l.right = merge(l.right, r)
        update_sum_branch(l)
        return l
    else:
        r.left = merge(l, r.left)
        update_sum_branch(r)
        return r


def split(node, x):
    if node is None:
        return None, None
    if node.value < x:
        l, r = split(node.right, x)
        node.right = l
        update_sum_branch(node)
        return node, r
    else:
        l, r = split(node.left, x)
        node.left = r
        update_sum_branch(node)
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


def update_sum_branch(self):
    self.sum_branch = self.value
    if self.left is not None:
        self.sum_branch += self.left.sum_branch
    if self.right is not None:
        self.sum_branch += self.right.sum_branch


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if find(self.root, value):
            return
        l, r = split(self.root, value)
        self.root = merge(merge(l, Node(value)), r)

    def sum(self, l, r):
        left, mid = split(self.root, l)
        mid, right = split(mid, r + 1)
        result = 0
        if mid is not None:
            result = mid.sum_branch
        self.root = merge(left, merge(mid, right))
        return result


if __name__ == '__main__':
    n = int(input())
    queries = list()
    for _ in range(n):
        queries.append(input())
    dTree = Tree()
    last_sum = 0
    for str in queries:
        query = str.split(" ")
        if query[0] == '+':
            query[1] = (int(query[1]) + last_sum) % (10 ** 9)
            last_sum = 0
            dTree.insert(query[1])
        else:
            last_sum = dTree.sum(int(query[1]), int(query[2]))
            print(last_sum)
