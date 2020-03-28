n,m = map(int,input().split())
rows = [input() for _ in range(n)]
k = int(input())
print(*sorted(rows, key=lambda row: int(row.split()[k])),sep='\n')
