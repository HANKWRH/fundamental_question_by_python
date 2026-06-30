a = list(input().lower())
d = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

if a!='' or a!=' ' or a!='\n':
    n = 1
else:
    n = 0

for i in a:
    if i != ' ':
        d[i] += 1
    else:
        n+=1

print(n)

for i in sorted(d, key=lambda x: d[x], reverse=True):
    if d[i] > 0:
        print(f'{i} : {d[i]}')
print()