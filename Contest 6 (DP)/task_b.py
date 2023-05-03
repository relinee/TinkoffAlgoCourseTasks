def count_safe_options(n):
    d1 = [1]*n
    d2 = [1]*n
    d3 = [1]*n
    for i in range(1,n):
        d1[i] = d2[i - 1] + d3[i - 1]
        d2[i] = d1[i - 1] + d2[i - 1] + d3[i - 1]
        d3[i] = d1[i - 1] + d2[i - 1] + d3[i - 1]
    return d1[n-1]+d2[n-1]+d3[n-1]


if __name__ == "__main__":
    n = int(input())
    print(count_safe_options(n))