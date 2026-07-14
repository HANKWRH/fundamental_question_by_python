            # s   ns
# 120     2.10 2.10
# 121-330 3.02 2.68
# 331-500 4.39 3.61
# 501-700 4.97 4.01
# 701     5.63 4.50
def summ(a,ans):
    
    
        if a>700:
            ans+=(a-700)*5.63
            return summ(700,ans)
        elif a>500:
            ans+=(a-500)*4.97
            return  summ(500,ans)
        elif a>330:
            ans+=(a-330)*4.39
            return  summ(330,ans)
        elif a>120:
            ans+=(a-120)*3.02
            return  summ(120,ans)
        else:
            ans+=a* 2.10
            return ans
    
def nonsumm(a,ans):
    
        if a>700:
            ans+=(a-700)*4.50
            return nonsumm(700,ans)
        elif a>500:
            ans+=(a-500)*4.01
            return  nonsumm(500,ans)
        elif a>330:
            ans+=(a-330)*3.61
            return  nonsumm(330,ans)
        elif a>120:
            ans+=(a-120)*2.68
            return  nonsumm(120,ans)
        else:
            ans+=a* 2.10
            return ans
        
a=float(input())
if a==0:
    print("Summer months: 0.00")
    print("Non-Summer months: 0.00")
else:
    print("Summer months:",f"{summ(a,0):.2f}",sep='')
    print("Non-Summer months:",f"{nonsumm(a,0):.2f}",sep='')