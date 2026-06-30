def p(a):
    if a<=1:
        return a+1
    else:
        return p(a-1)+p(int(a/2))
    
n=int(input())
print(p(n))