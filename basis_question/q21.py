a=[float(x) for x in input().split()]
# print(a)
a.sort()
# print(a)
print("maximum:",f"{a[-1]:.2f}", sep='')
print("minimum:", f"{a[0]:.2f}", sep='')