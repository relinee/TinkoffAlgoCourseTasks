def search_horizontal(dist, q, v, d_j):
    for i in range(1, m + 2):
        ind_i, ind_j = v[0], v[1] + i * d_j

        if g[ind_i][ind_j] == 2:
            return dist[v[0]][v[1]] + 1
        elif g[ind_i][ind_j] == 1:
            if dist[ind_i][ind_j - 1 * d_j] == 10 ** 9:
                dist[ind_i][ind_j - 1 * d_j] = dist[v[0]][v[1]] + 1
                q.insert(0, (ind_i, ind_j - 1 * d_j))
                #print(q)
            break


def search_vertical(dist, q, v, d_i):
    for i in range(1, n + 2):
        ind_i, ind_j = v[0] - i * d_i, v[1]
        if g[ind_i][ind_j] == 2:
            return dist[v[0]][v[1]] + 1
        elif g[ind_i][ind_j] == 1:
            if dist[ind_i + 1 * d_i][ind_j] == 10 ** 9:
                dist[ind_i + 1 * d_i][ind_j] = dist[v[0]][v[1]] + 1
                q.insert(0, (ind_i + 1 * d_i, ind_j))
                #print(q)
            break


def bfs():
    dist = [[10 ** 9 for _ in range(m + 2)] for _ in range(n + 2)]
    dist[1][1] = 0
    q = [(1, 1)]
    # count_s = 0
    while len(q) > 0:
        v = q.pop()
        ans = search_horizontal(dist, q, v, 1)
        if ans is not None:
            return ans
        ans = search_horizontal(dist, q, v, -1)
        if ans is not None:
            return ans
        ans = search_vertical(dist, q, v, 1)
        if ans is not None:
            return ans
        ans = search_vertical(dist, q, v, -1)
        if ans is not None:
            return ans


n, m = map(int, input().split())
g = [[1] * (m + 2)] * (n + 2)
for i in range(1, n + 1):
    line = list(map(int, input().rsplit()))
    g[i] = [1]
    g[i].extend(line)
    g[i].append(1)
# g = [[0]*(m)]*(n)
# for i in range(0, n):
#     line = list(map(int, input().rsplit()))
#     g[i] = line

print(bfs())
