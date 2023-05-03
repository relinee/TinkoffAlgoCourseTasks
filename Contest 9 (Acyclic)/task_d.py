import sys
from collections import defaultdict
from sys import stdin
sys.setrecursionlimit(10**5)

def two_sat(n, m, lst_elem):
    graph = [[] for _ in range(2*n)]
    graph_r = [[] for _ in range(2*n)]
    # здесь можно и без e_i
    for x1, e1, x2, e2 in lst_elem:
        # graph[x1+n].append(e1)
        # graph[n+e1].append(x1)
        # graph[n+x2].append(e2)
        # graph[n+e2].append(x2)
        #
        # graph_r[e1].append(n+x1)
        # graph_r[x1].append(n+e1)
        # graph_r[e2].append(n+x2)
        # graph_r[x2].append(n+e2)
        graph[x1 + n].append(x2)
        graph[x2 + n].append(x1)

        graph_r[x2].append(x1 + n)
        graph_r[x1].append(x2 + n)

    topsort = []
    used =[False] * (2*n)

    def dfs(v):
        used[v] = True
        for u in graph[v]:
            if not used[u]:
                dfs(u)
        topsort.append(v)

    for i in range(2*n):
        if not used[i]:
            dfs(i)

    color = [0] * (2*n)
    def unite(v, c):
        color[v] = c
        for u in graph_r[v]:
            if color[u] == 0:
                unite(u, c)

    c = 1
    for v in topsort[::-1]:
        if not color[v] :
            unite(v, c)
            c += 1
    res = []
    for i in range(0, n):
        if color[i] < color[n+i]:
            # здесь выписать e_i
            res.append(i)
        else:
            res.append(0)
    return res



if __name__ == '__main__':
    # lines = [line.rstrip() for line in stdin]
    # n, m = -1, -1
    # i = 0
    # while i < len(lines):
    #     n, m = map(int, lines[i].split())
    #     i += 1
    #     if m == 0:
    #         print("0"*n)
    #         continue
    #     lst_elem = []
    #     for j in range(i,m+i):
    #         x1, x2, x3, x4 = map(int, lines[j].split())
    #         lst_elem.append((x1, x2, x3, x4))
    #     i += m
    #     res = two_sat(n, m, lst_elem)
    #     strr = ''
    #     for i in res:
    #         strr += f'{i} '
    #     print(strr)
    n, m = 2, 2
    lst_elem = [(0, 0, 1, 0), (0, 1, 1, 1)]
    # n, m = 3, 4
    # lst_elem =  [(0, 1, 1, 0), (0, 0, 2, 1), (1, 1, 2, 0), (0, 0, 0, 1)]
    print(two_sat(n, m, lst_elem))