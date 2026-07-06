def solve():
    rows_lo = [
        "`1234567890-=",
        "qwertyuiop[]\\",
        "asdfghjkl;'",
        "zxcvbnm,./"
    ]
    rows_hi = [
        "~!@#$%^&*()_+",
        "QWERTYUIOP{}|",
        'ASDFGHJKL:"',
        "ZXCVBNM<>?"
    ]

    line = input()
    result = []

    for c in line:
        rc = c 
        found = False

        for r in range(4):
            idx = rows_lo[r].find(c)
            if idx != -1:
                if idx + 1 < len(rows_lo[r]):
                    rc = rows_lo[r][idx + 1]
                found = True
                break

            idx = rows_hi[r].find(c)
            if idx != -1:
                if idx + 1 < len(rows_hi[r]):
                    rc = rows_hi[r][idx + 1]
                found = True
                break

        result.append(rc)

    print("".join(result))


solve()