from itertools import product
k,m=map(int,input().split())
sm=-1
lis=[]
for _ in range(k):
    lis.append(list(map(int,input().split()))[1:])
for i in list(product(*lis)):
    t=sum(map(lambda x:x**2,i))%m
    if t>sm:
        sm=t
print(sm)
