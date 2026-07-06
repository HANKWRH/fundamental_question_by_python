while True:
    try:
        a = list(map(int, input().split()))

        d = {}

        for i in a:
            d[i] = d.get(i, 0) + 1

        ans = "NO"

        for k, v in d.items():
            if v > len(a) / 2:
                ans = k
                break

        print(ans)

    except EOFError:
        break