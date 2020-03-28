# Either
print(*sorted(input(),key=lambda a: ((1,a) if a.islower() else (2,a)) if a.isalpha() else ((3,a) if int(a)%2==1 else (4,a))),sep='')

# or
def ck(a):
    if a.isalpha():
        if a.islower():
            return (1,a)
        else:
            return (2,a)
    else:
        if int(a)%2==1:
            return (3,a)
        else:
            return (4,a)
print(*sorted(input(),key=ck),sep='')
