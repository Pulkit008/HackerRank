from collections import deque
d=deque()
for _ in range(int(input())):
    n=int(input())
    d.extend(map(int,input().split()))
    a='Yes'
    if max(d) not in (d[0],d[-1]):
        a='No'
    d.clear()
    print(a)
