n=int(input('введите число n '))

num = 0
for i in range(1, n+1):
    if i % 2 == 0:
        num -= i
    else:
        num += i
print(f'Знакочередующаяся сумма {num}')