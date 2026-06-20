a=int(input())
C=False
if(a%4==0):
    if(a%400==0):
        pass
    elif a%100==0:
        C=True
else:
    C=True
if C:
    print("Common Year")
else:
    print("Bissextile Year")
