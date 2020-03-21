# Enter your code here. Read input from STDIN. Print output to STDOUT
t=[x for x in input()]
a=t[0]
c=0
u=[]
for i in t:
    if i==a:
        c+=1
    else:
        p=(c,int(a))
        print(p,'',end='')
        a=i
        c=1
print((c,int(a)))
