n=int(input())
for i in range(n):
    ans=0
    k=input()
    for j in k:
        for a in j:
            
            ans+=ord(a)
    print(ans)