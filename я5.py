n = int(input('Введите количество чисел: ')) 

max1 = 0
max2 = 0

for _ in range(n):
    num = int(input('Введите число: ')) 

    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num

print(max1)
print(max2)


