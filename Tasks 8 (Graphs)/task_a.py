import sys

def dfs(v, used, g, comp):
    used[v] = True
    comp.append(v)
    for u in g[v]:
        if not used[u]:
            dfs(u, used, g, comp)


if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    n, m = map(int, input().split())

    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        i, j = map(int, input().split())
        g[i].append(j)
        g[j].append(i)

    used = [False] * (n + 1)
    comps = []

    # Начинаем с 1, так как номера вершин у нас с 1 (если хочу с 0 - то в цикле записи i - 1 и j - 1
    for i in range(1, n + 1):
        if not used[i]:
            c = []
            dfs(i, used, g, c)
            comps.append(c)

    print(len(comps))
    for c in comps:
        print(len(c))
        print(*sorted(c))

# 6 7
# 1 2
# 2 3
# 3 1
# 3 4
# 4 5
# 5 6
# 6 4