n,a,b,c=map(int, input().split(','))

n-=15*a+20*b+30*c
if n<0:
    print(0)
else:
    re_l=[0]*3
    re_l[2]=n//50
    n-=re_l[2]*50
    re_l[1]=n//5
    n-=re_l[1]*5
    re_l[0]=n
    print(*re_l,sep=',')