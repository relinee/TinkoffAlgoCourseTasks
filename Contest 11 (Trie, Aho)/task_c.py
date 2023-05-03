import fileinput
import sys

sys.setrecursionlimit(10 ** 9)


class Node:
    def __init__(self):
        self.next = {}
        self.terminal = False
        self.count = 0
        self.height = 0


def add(root: Node, s: str):
    node = root
    for c in s:
        if c not in node.next:
            node.next[c] = Node()
            node.next[c].height = node.height + 1
        node.next[c].count += 1
        node = node.next[c]
    node.terminal = True


def calc_min(elems, min_elem, curr_str):
    curr_sum = 0
    m = len(elems)
    tmp_elems = elems.copy()
    for i in range(m - 1):
        tmp_elems[i] = elems[i] - tmp_elems[i + 1]
    sz = len(A)
    for i in range(sz):
        curr_sum += A[i] * tmp_elems[i]
    if curr_sum < min_elem[0][0]:
        min_elem[0] = (curr_sum, curr_str.copy())


def calc_min_not_full(elems, min_elem, curr_str, height):
    curr_sum = 0
    m = height
    tmp_elems = elems.copy()
    for i in range(m - 1):
        tmp_elems[i] = elems[i] - tmp_elems[i + 1]
    sz = m
    for i in range(sz):
        curr_sum += A[i] * tmp_elems[i]
    if curr_sum < min_elem[0][0]:
        min_elem[0] = (curr_sum, curr_str.copy())


def dfs_new(v: Node, elems, min_elem, curr_str):
    if v.height != 0:
        elems[v.height - 1] = v.count
    if v.terminal:
        calc_min(elems, min_elem, curr_str)
    elif len(v.next.keys()) != K:
        for i in range(K):
            if f'{i}' not in v.next.keys():
                curr_str[v.height] = f'{i}'
                for i in range(v.height + 1, M - v.height):
                    curr_str[i] = '0'
                elems[v.height] = 0
                calc_min_not_full(elems, min_elem, curr_str, v.height)
                return

    for i in range(len(v.next.keys())):
        key = list(v.next.keys())[i]
        curr_str[v.height] = key
        dfs_new(v.next[key], elems, min_elem, curr_str)


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    root = Node()
    for i in range(N):
        line = input().split()
        add(root, line[0])
    mass = [0] * M
    min_s = [(10 ** 12, '0')]
    dfs_new(root, mass, min_s, ["0"] * M)
    print("".join(min_s[0][1]))
    print(min_s[0][0])
