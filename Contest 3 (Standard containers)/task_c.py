from collections import deque


def sort_wagons(n: int, arr: list[int]):
    deadlock_stack = deque()
    track_2 = deque()
    track_2.append(0)
    str_output = ""
    count_itt_all = 0
    while len(arr) > 0:
        count_itt = 0
        while True:
            if len(arr) == 0:
                break
            num = arr.pop()
            deadlock_stack.append(num)
            count_itt += 1
            if num == track_2[-1] + 1:
                break
        count_itt_all += 1
        str_output += str(1) + " " + str(count_itt) + "\n"
        count_itt = 0
        while len(deadlock_stack) > 0 and deadlock_stack[-1] == track_2[-1] + 1:
            track_2.append(deadlock_stack[-1])
            deadlock_stack.pop()
            count_itt += 1
        count_itt_all += 1
        str_output += str(2) + " " + str(count_itt) + "\n"
    if track_2[-1] == n:
        return str(count_itt_all) + "\n" + str_output
    return "0"


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.reverse()
    print(sort_wagons(n, arr))
