r,l=int(input()),list(map(int,input().split()))
print((sum(set(l))*r-sum(l))//(r-1))
