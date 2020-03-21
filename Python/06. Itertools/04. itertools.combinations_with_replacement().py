from itertools import combinations_with_replacement
a,s=input().split(' ')
for i in list(combinations_with_replacement(sorted(list(a)),int(s))):
    print(''.join(i))
