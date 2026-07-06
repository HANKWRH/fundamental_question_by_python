ans=list(input())

while True:
    s = input()
    if s == "0000":
        break
    A = 0
    B = 0
    num=list(s)
    for i in range(4):
        if num[i] == ans[i]:
            A += 1
        elif num[i] in ans:
            B += 1
        

    print(f"{A}A{B}B")


