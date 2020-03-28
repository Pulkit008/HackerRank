from collections import deque
d=deque()
for _ in range(int(input())):
    c = input().split()
    cmd = c[0]
    args = c[1:]
    cmd += "("+ ",".join(args) +")"
    eval("d."+cmd)
print(*d)
