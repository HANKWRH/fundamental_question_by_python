n = int(input())
list_b = [0] * 25
list_a = [int(x) for x in input().split()]

for i in range(n):
    list_b[list_a[2*i]] += 1
    list_b[list_a[2*i+1]] -= 1

ans = 0
ma = -1
for a in list_b:
    ans += a
    ma = max(ma, ans)

print(ma)