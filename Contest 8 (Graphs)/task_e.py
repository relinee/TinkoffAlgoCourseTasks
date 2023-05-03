import sys

def top_sort():
    top_srt = []
    used = [False] * n

    def dfs(vertex):
        used[vertex] = True
        for u in graph[vertex]:
            if not used[u[0]]:
                dfs(u[0])
        top_srt.append(vertex)

    dfs(0)
    return top_srt[::-1]


# https://kik0s.github.io/tinkoff-algos-for-students/9.pdf + чат в тг
if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    n, m, s, t = map(int, input().split())
    graph = [[] for _ in range(n)]
    dist = [float('inf')] * n

    for i in range(m):
        b, e, w = map(int, input().split())
        graph[b - 1].append((e - 1, w))

    tsort = top_sort()
    dist[s - 1] = 0
    for i in range(n):
        if len(tsort) > i:
            for edge in graph[tsort[i]]:
                dist[edge[0]] = min(dist[edge[0]], dist[tsort[i]] + edge[1])

    if dist[t - 1] == float('inf'):
        print("Unreachable")
    else:
        print(dist[t - 1])