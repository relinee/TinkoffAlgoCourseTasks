class Node:
    def __init__(self):
        self.next = {}
        self.terminal = False
        self.count_sub_node = 0


def add(root: Node, s: str):
    node = root
    for c in s:
        if c not in node.next:
            node.next[c] = Node()
        node = node.next[c]
        node.count_sub_node += 1
    node.terminal = True


def search(root, k):
    node = root
    ans = ''
    while k != 0 or not node.terminal:
        for item in sorted(node.next.items()):
            if item[1].count_sub_node >= k:
                ans += item[0]
                node = node.next[item[0]]
                if node.terminal:
                    k -= 1
                break
            else:
                k -= item[1].count_sub_node
    return ans


root = Node()
n = int(input())
for i in range(n):
    line = input().rsplit()
    if int(line[0]) == 1:
        add(root, line[1])
    else:
        print(search(root, int(line[1])))
