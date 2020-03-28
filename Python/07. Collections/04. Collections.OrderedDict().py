from collections import OrderedDict
d=OrderedDict()
for _ in range(int(input())):
    l=input().split()
    n,p=' '.join(l[:-1]),int(l[-1])
    if n in d:
        d[n]+=p
    else:
        d[n]=p
for k,v in d.items():
    print(k,v)
