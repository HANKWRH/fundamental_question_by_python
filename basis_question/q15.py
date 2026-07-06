s = input().lower()
s = s.replace(',', ' ')
s = s.replace('.', ' ')
print(len(s.split()))

d = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

for ch in s:
    if ch.isalpha():
        d[ch] += 1

for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True):
    if v > 0:
        print(f"{k} : {v}")