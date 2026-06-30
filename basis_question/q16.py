tar = input()
text = input()

#print(text.find(tar))

ans = 0
#print(text[0:1+len(tar)])

for i in range(len(text) - len(tar) + 1):
    if text[i:i+len(tar)] == tar:
        ans += 1
print(ans)