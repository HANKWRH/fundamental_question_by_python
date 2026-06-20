b=int(input())
for i in range(b):
    a=[x for x in input().split()]

    if  a[0]=='+':
        print(int(a[1])+int(a[3]), " ", int(a[2])+int(a[4]), sep='')
    elif a[0]=='-':
        print(int(a[1])-int(a[3]), " ", int(a[2])-int(a[4]), sep='')
    elif a[0]=='*':
        print(int(a[1])*int(a[3])-int(a[2])*int(a[4]), " ", int(a[1])*int(a[4])+int(a[2])*int(a[3]),sep='')
    else:
        pass
