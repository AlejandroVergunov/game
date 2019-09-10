# -*- coding: utf-8 -*-
#Генератор четырех случайных цифр, значения не повторяются.
from random import randint

#unknown - множество сгенерировано автоматом
#unknown_list - список из 4-х значений сгенерированный автоматом
#list_user_input - список из 4-х значений из ввода пользователя

x_cow = 0
x_bull = 0
y_bull = 0

def random_number():
    '''Формирование списка из 4-х элементов  от  1  до 9'''
    unknown = set(str(randint(1, 9)))
    while len(unknown) != 4:                                                                         
        x = str(randint(1, 9))
        unknown.add(x)
    unknown_list = [i for i in unknown]
    return(unknown_list)

def user_input_number():
    '''Формирование списка из пользовательского ввода'''
    user_input = str(input('Введите 4-х значное число-> '))
    list_user_input = list(user_input)
    return list_user_input

unknown_list = random_number()    # - список из 4-х случайных цифр от 1 до 9
#print(unknown_list)
while y_bull != 4:
    y_bull  = 0
    y_cow = 0
    user_list = user_input_number()
    for i in user_list:
        x_bull = user_list.index(i)
        for j in unknown_list:
            x_cow = unknown_list.index(j)
            if ((x_bull == x_cow) and (i == j)):
                y_bull +=1
            if ((x_bull != x_cow) and (i == j)):
                y_cow +=1
    if y_bull == 0:
        bulls = 'быков'
    elif y_bull == 1:
        bulls = 'бык'
    else:
        bulls = 'быка'
    if y_cow == 0:
        cows = 'коров'
    elif y_cow == 1:
        cows = 'корова'
    else:
        cows = 'коровы'    
    print(y_bull, '', bulls, '',  y_cow, '' , cows)
input()    
