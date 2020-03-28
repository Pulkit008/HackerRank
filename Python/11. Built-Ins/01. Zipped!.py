n,x=map(int,input().split())
l=[list(map(float,input().split())) for _ in range(x)]
z=zip(*l)
for i in z:
    print(sum(i)/x)
