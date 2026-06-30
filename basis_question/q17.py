s=input().lower()
list_a=s.split()
list_b=[]
#print(list_a)
for k in list_a:
    if k in s and k not in list_b:
        list_b.append(k)
print(*list_b)