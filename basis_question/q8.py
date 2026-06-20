a=int(input())
ispri=True

if(a<=3):
    print("YES")
else:
    for i in range(2,int(a**0.5)+1):
        if(a%i==0):
            ispri=False
    if ispri:
        print("YES")
    else:
        print("NO")   
