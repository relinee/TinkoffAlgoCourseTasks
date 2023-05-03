def summands_num(num, pos, max_val, elems):
    if num == 0:
        str_outp = ""
        for i in range(pos):
            str_outp += str(elems[i]) + " "
        print(str_outp)
        return
    for i in range(1, min(num, max_val) + 1):
        elems[pos] = i
        summands_num(num - i, pos + 1, i, elems)


if __name__ == "__main__":
    n = int(input())
    arr_elem = [0] * n
    summands_num(n, 0, n, arr_elem)