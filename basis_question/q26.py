n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

a.sort(key=digit_sum)
a.sort()                 
a.sort(key=digit_sum) 

print(*a)