from itertools import combinations
n=int(input())
l=list(input().split())
k=int(input())
c=0
com=list(combinations(l,k))
for i in com:
    if 'a' in i:
        c+=1
print(c/len(com))
