student=[]
mar=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        s=[]
        s.append(input())
        s.append(float(input()))
        mar.append(s[1])
        student.append(s)
m=min(mar)
mar.remove(m)
while min(mar)==m:
    mar.remove(m)
m=min(mar)
student.sort()
for i in range(len(student)):
    if m == student[i][1]:
        print(student[i][0])
