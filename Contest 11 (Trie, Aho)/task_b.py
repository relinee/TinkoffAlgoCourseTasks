from dataclasses import dataclass
import sys
sys.setrecursionlimit(10 ** 5)

@dataclass
class Node:
    pc: str
    parent: 'Node'
    go: {}
    suflink: 'Node'
    num_in_dict: []
    height: int


def char_to_num(c):
    return ord(c) - ord('a')


def get_suflink(v: Node, root):
    if v.suflink is not None:
        return v.suflink
    elif v == root:
        v.suflink = root
    elif v.parent == root:
        v.suflink = root
    else:
        v.suflink = get_go(get_suflink(v.parent, root), v.pc, root)
    return v.suflink


def get_go(v, c, root):
    if c in v.go:
        return v.go[c]
    elif v == root:
        v.go[c] = root
    else:
        v.go[c] = get_go(get_suflink(v, root), c, root)
    return v.go[c]


def add_string(root, s: str, j):
    node = root
    for c in s:
        if c not in node.go:
            node.go[c] = Node(pc=c, parent=node, suflink=None,
                                num_in_dict=[], go={}, height=node.height + 1)
        node = node.go[c]
    node.num_in_dict.append(j)


if __name__ == '__main__':
    s = input()
    sz = int(input())
    root = Node(None, None, {}, None, None, 0)
    for i in range(sz):
        add_string(root, input(), i)

    ans = [[] for _ in range(sz)]
    node = root
    for i in range(len(s)):
        node = get_go(node, s[i], root)
        vert = node
        while vert != root:
            if len(vert.num_in_dict) > 0:
                for j in vert.num_in_dict:
                    ans[j].append(i - vert.height + 2)
            vert = get_suflink(vert, root)

    for i in range(sz):
        if len(ans[i]) == 0:
            print(0)
        else:
            print(f'{len(ans[i])} {" ".join(str(x) for x in ans[i])}')
