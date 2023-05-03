import sys


def dfs(v, used, g, prev_u):
    used[v] = True
    prev_u[v] = True
    for u in g[v]:
        if not used[u]:
            if dfs(u, used, g, prev_u):
                return 1
        elif prev_u[u] is True:
            return 1
    prev_u[v] = False
    return 0


if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    n, m = map(int, input().split())

    g = [[] for _ in range(n)]
    for _ in range(m):
        i, j = map(int, input().split())
        g[i - 1].append(j - 1)

    used = [False] * n
    prev_u = [False] * n
    for i in range(n):
        if not used[i]:
            if dfs(i, used, g, prev_u) == 1:
                print(1)
                exit()
    print(0)
