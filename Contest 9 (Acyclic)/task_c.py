import sys
sys.setrecursionlimit(10**5)
def dfs(v):
    used[v] = True
    for u in graph[v]:
        if not used[u]:
            dfs(u)
    topsort.append(v)


if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    used = [False] * n

    for i in range(n):
        inpt_list = list(map(int, input().split()))
        for v in inpt_list[1:]:
            graph[i].append(v - 1)

    topsort = []
    dfs(0)

    k = len(topsort)
    sum_outp = 0
    str_outp = ""
    for i in topsort:
        sum_outp += p[i]
        str_outp += f"{i+1} "
    print(sum_outp, k)
    print(str_outp)

