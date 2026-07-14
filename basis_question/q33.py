

try:
    while True:
        ans = 0
        cnt = 0
        k = input().split()
        for i in k:
            ans += int(i)
            cnt += 1
        print("Size:", cnt)
        if cnt > 0:
            print("Average:", f"{ans / cnt:.3f}")
except EOFError:
    pass

