n,l=int(input()),list(input().split())
print(all([int(x)>0 for x in l]) and any([x==x[::-1] for x in l]))
