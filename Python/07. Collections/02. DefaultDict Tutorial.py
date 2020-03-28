from collections import defaultdict
a,b=map(int,input().split())
d = defaultdict(list)
for i in range(1,a+1):
    d[input()].append(i)
for i in range(b):
    s=input()
    if s in d:
        print(*d[s])
    else:
        print(-1)
