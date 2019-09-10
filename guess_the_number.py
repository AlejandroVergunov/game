# -*- coding: utf-8 -*-
import random
b = None
c = []
a = random.randint(1, 100)
while True:
    while b != a:
        try:
            b = int(input('Введи число от 1 до 100 и нажми Enter -> '))            
            while b < 1 or b > 100 or b == 0:
                b = int(input('Русским языком написано от 1 до 100... -> '))
            for i in [c]:
                if b in i:
                    b =int(input('Такое число уже было -> '))
                    break
            if b < a:
                print('Ваше число меньше')
            elif b > a:
                print('Ваше число больше')
        except ValueError:
            print('Это не число...')
        c.append(b)
    print('\n' + '#' * 23 + '\n' + 'Поздравляю! Ты угадал!' + '\n' + '#' * 23)
    break