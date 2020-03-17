n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    c = input().split()
    cmd = c[0]
    args = c[1:]
    cmd += "("+ ",".join(args) +")"
    eval("s."+cmd)
print(sum(s))
