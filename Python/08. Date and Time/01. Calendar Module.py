import calendar as c
d=list(map(int,input().split()))
wd=['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY','SUNDAY']
print(wd[c.weekday(d[2],d[0],d[1])])
