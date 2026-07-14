while True:
    try:
        h, g = input().split()
        h = float(h)
        g = int(g)

        if g == 1:
            print(f"{(h - 80) * 0.7:.1f}")
        else:
            print(f"{(h - 70) * 0.6:.1f}")

    except EOFError:
        break