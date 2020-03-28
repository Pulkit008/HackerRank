print(*sorted(input(),key=lambda a: ((1,a) if a.islower() else (2,a)) if a.isalpha() else ((3,a) if int(a)%2==1 else (4,a))),sep='')
