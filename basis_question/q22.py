board = [list(map(int, input().split())) for _ in range(3)]

win = False

# 檢查列
for i in range(3):
    if board[i][0] == board[i][1] == board[i][2]:
        win = True

# 檢查行
for j in range(3):
    if board[0][j] == board[1][j] == board[2][j]:
        win = True

# 主對角線
if board[0][0] == board[1][1] == board[2][2]:
    win = True

# 副對角線
if board[0][2] == board[1][1] == board[2][0]:
    win = True

if win:
    print("True")
else:
    print("False")