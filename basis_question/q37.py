d = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}

for _ in range(4):
    d[input()] += 1

m = max(d.values())

if m == 4:
    print("WIN")
elif list(d.values()).count(2) == 2:
    for k in sorted(d, reverse=True):
        if d[k] == 2:
            print(int(k) * 2)
            break
elif list(d.values()).count(2) == 1:
    ans=0
    for k in sorted(d):
        if d[k] != 2:
            ans+=d[k]*int(k)
    print(ans)
else:
    print("R")
    