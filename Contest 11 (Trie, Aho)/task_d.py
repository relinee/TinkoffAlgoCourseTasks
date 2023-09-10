from dataclasses import dataclass
import sys
sys.setrecursionlimit(10 ** 5)

@dataclass
class Node:
    pc: str
    parent: 'Node'
    go: {}
    suflink: 'Node'
    id: int
    terminal: bool


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


def add_string(root, s: str):
    global id
    node = root
    for c in s:
        if c not in node.go:
            node.go[c] = Node(pc=c, parent=node, suflink=None, go={}, id=id, terminal=False)
            id += 1
        node = node.go[c]
    node.terminal = True


def dfs(v: Node, used, prev_u):
    used[v.id] = True
    prev_u[v.id] = True
    for u in v.go:
        if v.go[u].id != v.id:
            if not used[v.go[u].id]:
                if dfs(v.go[u], used, prev_u):
                    return 1
            elif prev_u[v.go[u].id] is True:
                return 1
    if v.terminal:
        node = get_suflink(v, root)
        if node.id != v.parent.id or node.id == 0:
            if not used[node.id]:
                if dfs(node, used, prev_u):
                    return 1
            elif prev_u[node.id] is True and v.parent.id != node.id and node.suflink != root:
                return 1
            prev_u[node.id] = False
    prev_u[v.id] = False
    return 0


if __name__ == '__main__':
    id = 1
    sz = int(input())
    root = Node(None, None, {}, None, 0, False)

    for i in range(sz):
        add_string(root, input())

    prev_u = [False] * id
    used = [False] * id
    node = root
    if dfs(root, used, prev_u):
        print("TAK")
    else:
        print("NIE")