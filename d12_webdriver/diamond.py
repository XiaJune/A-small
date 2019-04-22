
# 空心的菱形打印
r = 5
for y in range(2 * r + 1):
    for x in range(2 * r + 1):
        if y == x -r or y == x + r or y == -x + r or y == -x + 3 * r:
            print('*', end='')
        else:
            print(' ', end='')
    print()


# 实心的菱形
r = 5
for y in range(2 * r + 1):
    for x in range(2 * r + 1):
        if y >= x -r and y <= x + r and y >= -x + r and y <= -x + 3 * r:
            print('*', end='')
        else:
            print(' ', end='')
    print()
