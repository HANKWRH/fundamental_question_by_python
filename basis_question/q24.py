from decimal import Decimal
r = Decimal(input())
n = int(input())
p = int(input())

total = 0
for _ in range(n):
    total = (total + p) * (1 + r)

print(int(total))