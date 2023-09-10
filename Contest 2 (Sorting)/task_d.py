def palindrome_create(a: list[str]):
    a = sorted(a)
    i = 0
    res = ""
    center = ""
    while i + 1 < len(a):
        if a[i] == a[i + 1]:
            res += a[i]
            i += 2
        else:
            if center == "":
                center = a[i]
            i += 1
    if i < len(a) and center == "":
        center = a[i]
    if center == "":
        res += str(res[:])[::-1]
    else:
        res += center
        res += str(res[:len(res)-1])[::-1]
    return res

if __name__ == '__main__':
    n = int(input())
    a = list(input().rsplit()[0])
    print(palindrome_create(a))


