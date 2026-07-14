special = input()
head = [input() for _ in range(3)]

n = int(input())

price = [0] * 7
money = [2000000, 200000, 40000, 10000, 4000, 1000, 200]

for _ in range(n):
    s = input()

    # 特獎
    if s == special:
        price[0] += 1
        continue

    # 頭獎～六獎
    for h in head:
        if s == h:
            price[1] += 1
            break
        elif s[-7:] == h[-7:]:
            price[2] += 1
            break
        elif s[-6:] == h[-6:]:
            price[3] += 1
            break
        elif s[-5:] == h[-5:]:
            price[4] += 1
            break
        elif s[-4:] == h[-4:]:
            price[5] += 1
            break
        elif s[-3:] == h[-3:]:
            price[6] += 1
            break

print(*price)
print()
print(sum(price[i] * money[i] for i in range(7)))