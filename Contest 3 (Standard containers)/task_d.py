from collections import deque

n = int(input())
q1 = deque()
q2 = deque()
for _ in range(n):
    inpt = input().split()
    if inpt[0] == "+":
        q2.append(inpt[1])
    elif inpt[0] == "*":
        q2.appendleft(inpt[1])
    else:
        print(q1.popleft())
    if len(q1) < len(q2):
        q1.append(q2.popleft())