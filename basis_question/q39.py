n=int(input())

for i in range(n):
    a, b, c=map(int, input().split())
    ba = int(a >= 60)
    bb = int(b >= 60)
    bc = int(c >= 60)


    if (ba and bb and bc) or (ba+bb+bc==2 and a+b+c>=220):
        print("P")
    elif (ba+bb+bc==2 and a+b+c<220) or (ba+bb+bc==1 and max(a, b, c)>=80):
        print("M")
    else:
        print("F")