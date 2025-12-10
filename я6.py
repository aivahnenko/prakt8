import random

s = random.randint(1, 10)

for i in range(3):
    guess = int(input('введите ваш вариант '))

    if guess == s:
        print("Угадали!")
        break
    else:
        print("Неверно")
        if guess < s:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")
else:
    print(f"Вы не угадали за 3 попытки. Загаданное число было: {s}")
