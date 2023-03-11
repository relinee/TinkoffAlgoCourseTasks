def find_min_elem_on_sub(k: int, arr: list[int]):
    q_ind = list()
    for i in range(k):
        while len(q_ind) > 0 and arr[i] < arr[q_ind[-1]]:
            q_ind.pop()
        q_ind.append(i)
    for i in range(k, len(arr)):
        print(arr[q_ind[0]], end=" ")

        while len(q_ind) > 0 and q_ind[0] <= i - k:
            del q_ind[0]

        while len(q_ind) > 0 and arr[i] < arr[q_ind[-1]]:
            q_ind.pop()

        q_ind.append(i)
    print(arr[q_ind[0]], end=" ")


if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    find_min_elem_on_sub(k, arr)
