# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
sa=set(map(int,input().split()))
for _ in range(int(input())):
    c=input().split()
    eval("sa."+c[0]+"(set(map(int,input().split())))")
print(sum(sa))
