ah,am = map(int,input().split())
bh,bm = map(int,input().split())
c = (bh*60+bm)-(ah*60+am)
m = [30,40,60]
i = 0
ans = 0

while True:
    if c > 120:
       ans += 4*m[i]
    else:
        ans += (c//30)*m[i]
        break;
    c -= 120
    if i != 2:
        i+=1

print(ans)