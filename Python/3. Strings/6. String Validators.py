if __name__ == '__main__':
    s = input()
b=[False,False,False,False,False]
for x in s:
    if x.isalnum():
        b[0]=True
    if x.isalpha():
        b[1]=True
    if x.isdigit():
        b[2]=True
    if x.islower():
        b[3]=True
    if x.isupper():
        b[4]=True
for i in range(5):
    print(b[i])
