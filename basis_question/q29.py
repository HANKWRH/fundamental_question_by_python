a = input()

d = {
    'A':10,'B':11,'C':12,'D':13,'E':14,
    'F':15,'G':16,'H':17,'J':18,'K':19,
    'L':20,'M':21,'N':22,'P':23,'Q':24,
    'R':25,'S':26,'T':27,'U':28,'V':29,
    'X':30,'Y':31,'W':32,'Z':33,'I':34,'O':35
}

if len(a)!=10 or a[0] not in d or not a[1:].isdigit():
    print("WRONG!!!")
else:
    x1 = d[a[0]] // 10
    x2 = d[a[0]] % 10
    ans = (x1 + 9*x2 +
        8*int(a[1]) +
        7*int(a[2]) +
        6*int(a[3]) +
        5*int(a[4]) +
        4*int(a[5]) +
        3*int(a[6]) +
        2*int(a[7]) +
        int(a[8]) +
        int(a[9]))
    if ans % 10 == 0:
        print("CORRECT!!!")
    else:
        print("WRONG!!!")