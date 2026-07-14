n = int(input())

for _ in range(n):
    T, m, k = map(int, input().split())

    a = list(map(int, input().split()))
    a.sort()

    ans = sum(a[:m])

    if ans <= T:
        print(ans)
    else:
        print("Impossible")