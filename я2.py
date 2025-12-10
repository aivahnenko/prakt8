x = 0

num1 = int(input('введите 1 число '))
num2 = int(input('введите 2 число '))
num3 = int(input('введите 3 число '))
num4 = int(input('введите 4 число '))
num5 = int(input('введите 5 число '))
num6 = int(input('введите 6 число '))
num7 = int(input('введите 7 число '))
num8 = int(input('введите 8 число '))
num9 = int(input('введите 9 число '))
num10 = int(input('введите 10 число '))

for i in range(num1, num10):
    if i % 2 == 0:
        x = x + 1
    else:
        x == 0
if x > 0:
    print('YES')
else:
    print('NO')