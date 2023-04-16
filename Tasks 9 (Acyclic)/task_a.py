import sys
sys.setrecursionlimit(10 ** 5)

n = int(input())
m = int(input())
graph = [[] for _ in range(n)]
graph_r = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph_r[v - 1].append(u - 1)

topsort = []
used = [False] * n


def dfs(v):
    used[v] = True
    for u in graph[v]:
        if not used[u]:
            dfs(u)
    topsort.append(v)


dfs(0)
for i in range(n):
    if not used[i]:
        dfs(i)

color = [0] * (n)
g_res = [{} for _ in range(n)]


def unite(v, c):
    color[v] = c
    for u in graph_r[v]:
        if color[u] == 0:
            unite(u, c)
        elif color[u] != c:
            g_res[color[u]] = c


c = 1
for v in topsort[::-1]:
    if color[v] == 0:
        unite(v, c)
        c += 1

used = [1] * (c-1)
for v in range(n):
    for u in graph[v]:
        if color[v] != color[u]:
            used[color[v]] = 0

print(sum(used))
# ответ - количество вершин, из которой не исходит ребер
