
def ab_pruning(ind, state, a, b, c, m, player, alpha, beta):
    if state == 0:
        return (a * ind % m * ind + b * ind + c) % m
    if player == 2:
        for move in range(ind * 2, (ind + 1) * 2):
            beta = min(beta, ab_pruning(move, state - 1, a, b, c, m, 1, alpha, beta))
            if beta <= alpha:
                break
        return beta
    else:
        for move in range(ind * 2, (ind + 1) * 2):
            alpha = max(alpha, ab_pruning(move, state - 1, a, b, c, m, 2, alpha, beta))
            if beta <= alpha:
                break
        return alpha


if __name__ == '__main__':
    n, a, b, c, m = map(int, input().split())
    #n, a, b, c, m = 3, 10, 7, 9, 20
    print(ab_pruning(0, n, a, b, c, m, 1, 9, 10 ** 9 + 1)) # 11