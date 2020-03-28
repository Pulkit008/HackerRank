from collections import namedtuple
n=int(input())
stu=namedtuple('stu',input().split())
print(sum([int(stu(*list(input().split())).MARKS) for _ in range(n)])/n)
