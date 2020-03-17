sa=set(map(int,input().split()))
o=True
for _ in range(int(input())):
    s=set(map(int,input().split()))
    if sa.issuperset(s):
        if sa==s:
            o=False
    else:
        o=False
print(o)
