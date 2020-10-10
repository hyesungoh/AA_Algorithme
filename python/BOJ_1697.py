# 2*x, x-1, x+1
from collections import deque
n, k = map(int, input().split())
q = deque([n])
d = {n: 0}

while True:
    node = q.popleft()
    if node == k:
        print(d[node])
        break
    else:
        t_n1 = node * 2
        t_n2 = node + 1
        t_n3 = node - 1

        if t_n1 not in d:
            d[t_n1] = d[node] + 1
            q.append(t_n1)

        if t_n2 not in d:
            d[t_n2] = d[node] + 1
            q.append(t_n2)

        if t_n3 not in d:
            d[t_n3] = d[node] + 1
            q.append(t_n3)
