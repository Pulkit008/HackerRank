# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
a,s=input().split(' ')
for i in list(permutations(sorted(list(a)),int(s))):
    print(''.join(i))
