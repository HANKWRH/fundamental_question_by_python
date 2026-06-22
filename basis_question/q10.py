a, b=map(int, input().split())
c=a+b
a=max(a, b)
b=c-a
ans=1
while a!=0 and b!=0:
    
    #print(a, b,end='\n')
    a-=a//b*b
    t=b
    b=a
    a=t

print(a)    