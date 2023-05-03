
def gen_choose_k(curr_list, res, pos, sum):
    if pos == m:
        if sum == n:
            if len(res) == 0 or len(curr_list) < len(res):
                res = curr_list.copy()
            return res
        return res
    res = gen_choose_k(curr_list, res, pos + 1, sum)
    res = gen_choose_k(curr_list + [arr_elem[pos]], res, pos + 1, sum + arr_elem[pos])
    return res


# https://kik0s.github.io/tinkoff-algos-for-students/7.pdf  - 24 страница :D
if __name__ == "__main__":
    n, m = map(int, input().split())
    m = m * 2
    str = input()
    arr_elem = []
    for num in str.split():
        arr_elem += [int(num)] * 2
    if sum(arr_elem) < n:
        print("-1")
    else:
        ans = gen_choose_k([], [], 0, 0)
        if len(ans) == 0:
            print("0")
        else:
            print(len(ans))
            print(*ans)
