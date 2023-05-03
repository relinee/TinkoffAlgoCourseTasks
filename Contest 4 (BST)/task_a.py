import random
# TODO: Добавить решение задания B

class Node:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
        self.p = random.random()


def merge(l, r):
    if l is None:
        return r
    if r is None:
        return l
    if l.p < r.p:
        l.right = merge(l.right, r)
        return l
    else:
        r.left = merge(l, r.left)
        return r


def split(node, x):
    if node is None:
        return None, None
    if node.value < x:
        l, r = split(node.right, x)
        node.right = l
        return node, r
    else:
        l, r = split(node.left, x)
        node.left = r
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


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if find(self.root, value):
            return
        l, r = split(self.root, value)
        self.root = merge(merge(l, Node(value)), r)


    def next(self, value):
        node = self.root
        result = -1
        while node is not None:
            if node.value >= value:
                result = node.value
                node = node.left
            else:
                node = node.right
        return result



if __name__ == '__main__':
    n = int(input())
    queries = list()
    for _ in range(n):
        queries.append(input().split(' '))
    dTree = Tree()
    last_get = 0
    for str in queries:
        query = [str[0], int(str[1])]
        if query[0] == '+':
            query[1] = (query[1] + last_get) % (10 ** 9)
            last_get = 0
            dTree.insert(query[1])
        else:
            last_get = dTree.next(query[1])
            print(last_get)
