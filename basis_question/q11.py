while True:
    try:
        a, b = map(int, input().split())
        l_1 = [input().split() for _ in range(a)]

        for i in range(b):
            print(" ".join(l_1[j][i] for j in range(a)))

    except EOFError:
        break