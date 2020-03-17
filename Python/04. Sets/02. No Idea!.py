n,m=map(int,input().split())
ar=list(map(int,input().split()))
s1=set(map(int,input().split()))
s2=set(map(int,input().split()))
c=0
for i in ar:
    if i in s1:
        c+=1
    if i in s2:
        c-=1
print(c)
