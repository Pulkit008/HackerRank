# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x=input()
c=Counter(list(map(int,input().split())))
tm=0
n=int(input())
while n:
    s,r=map(int,input().split())
    if s in c:
        tm+=r
        c[s]-=1
        if c[s]==0:
            del c[s]
    n-=1
print(tm)
