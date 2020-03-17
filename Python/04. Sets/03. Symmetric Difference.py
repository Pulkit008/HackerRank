# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
l1=set(map(int,input().split()))
input()
l2=set(map(int,input().split()))
print(*sorted(l1.symmetric_difference(l2)),sep='\n')
