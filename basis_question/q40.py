k=input().split()
p=[]
for i in k:
    if i!='X':
        p.append(int(i))
    else:p.append(int(10))
p_1=[]
p_2=[]
for i in range(1,11):
    p_1.append(sum(p[:i]))
# print(p_1)
for i in range(1,11):
    p_2.append(sum(p_1[:i]))
if p_2[-1]%11==0:
    print("YES")
else:print("NO")