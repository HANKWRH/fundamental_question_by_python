s = input()
n = int(input())

for ch in s:
    if 'A' <= ch <= 'Z':
        print(chr((ord(ch) - ord('A') + n) % 26 + ord('A')), end="")
    elif 'a' <= ch <= 'z':
        print(chr((ord(ch) - ord('a') + n) % 26 + ord('a')), end="")
    elif '0' <= ch <= '9':
        print(chr((ord(ch) - ord('0') + n) % 10 + ord('0')), end="")
    else:
        print(ch, end="")