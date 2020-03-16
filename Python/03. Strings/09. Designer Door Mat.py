# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b=map(int, input().split())
m=a//2+1
for i in range(1,m):
    print(('.|.'*(i*2-1)).center(b,'-'))
print('WELCOME'.center(b,'-'))
for i in range(m-1,0,-1):
    print(('.|.'*(i*2-1)).center(b,'-'))
