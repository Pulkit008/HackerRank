from itertools import combinations
a,s=input().split(' ')
for i in range(1,int(s)+1):
    print( *list(map(''.join,combinations(sorted(list(a)),i))),sep='\n')
