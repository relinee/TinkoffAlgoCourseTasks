
def bfs(n, x_start, y_start):
    dx = [1, -1, 1, -1, 2, -2, 2, -2]
    dy = [2, 2, -2, -2, 1, 1, -1, -1]
    d = [[float('inf')] * n for _ in range(n)]
    d[x_start - 1][y_start - 1] = 0
    q = ([(x_start - 1, y_start - 1)])
    while len(q) > 0:
        curr_x, curr_y = q.pop()
        for i in range(8):
            new_x, new_y = curr_x + dx[i], curr_y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n and d[new_x][new_y] > d[curr_x][curr_y] + 1:
                d[new_x][new_y] = d[curr_x][curr_y] + 1
                q.append((new_x, new_y))
    return d


def find_shorted_path(d, x_s, y_s, x_f, y_f, n):
    dx = [1, -1, 1, -1, 2, -2, 2, -2]
    dy = [2, 2, -2, -2, 1, 1, -1, -1]
    path = [(x_f - 1, y_f - 1)]
    curr_x, curr_y = x_f - 1, y_f - 1
    while curr_x != x_s - 1 or curr_y != y_s - 1:
        for i in range(8):
            new_x, new_y = curr_x + dx[i], curr_y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n and d[new_x][new_y] == d[curr_x][curr_y] - 1:
                path.append((new_x, new_y))
                curr_x, curr_y = new_x, new_y
                break
    return path


if __name__ == '__main__':
    N = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    dist = bfs(N, x1, y1)
    s_path = find_shorted_path(dist, x1, y1, x2, y2, N)

    s_path = reversed(s_path)
    print(dist[x2 - 1][y2 - 1])
    for x, y in s_path:
        print(x + 1, y + 1)
