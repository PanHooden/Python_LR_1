import random as r
import math as m
import os
import time as t


print("\nРезультаты:")

#Пункт 1.
"""Используя цикл while, сгенерировать список с диапазоном значений от 0 до 15.
Вывести результат."""

list_1=[]
i=0
while i <16:
    list_1.append(i)
    i+=1
print (f"Пункт 1. Итоговый список: {list_1}\n")
del list_1, i


#Пункт 2.
"""На основе списка создать множество значений от 0 до 10,
использовать при этом цикл break.
Вывести результат."""

list_2=[]
i=0
while True:
    list_2.append(i)
    i+=1
    if i==11:
        break
print(f"Пункт 2. Итоговый список: {list_2}\n")
del list_2, i


#Пункт 3.
"""Удалить из списка все значения меньше 11, используя цикл while.
Вывести результат."""

list_3=[]
for i in range (25):
    list_3.append(r.randint(1,19))
del i
print(f"Пункт 3. Исходный случайный список: {list_3}")

count=0
len_list_3=len(list_3)
while count<len_list_3:
    if list_3[count]<11:
        del list_3[count]
        len_list_3-=1
        continue
    count+=1
print(f"Пункт 3. Итоговый список: {list_3}\n")
del count, len_list_3, list_3


#Пункт 4.
"""Очищенный список заполнить элементами кортежа,
увеличив на 39 все элементы больше или равные 50 и увеличив в 3 раза остальные.
Вывести результат.
Элементы кортежа добавить в конец списка в обратном порядке.
Вывести результат."""

list_4=[]
for i in range (25):
    list_4.append(r.randint(30,80))
tuple_4=tuple(list_4)
del i
print(f"Пункт 4. Исходный случайный кортеж: {tuple_4}")

list_4.clear()

len_tuple_4=len(tuple_4)
for i in range(len_tuple_4):
    if tuple_4[i]>=50:
        list_4.append(tuple_4[i]+39)
    else:
        list_4.append(tuple_4[i]*3)
del i
print(f"Пункт 4. Созданный из кортежа список: {list_4}")

for i in range(len_tuple_4):
    list_4.append(tuple_4[-i-1])
del i, tuple_4, len_tuple_4
print(f"Пункт 4. Итоговый список: {list_4}\n")
del list_4


#Пункт 5.
"""Написать функцию, на вход которой подается два списка
в одном значение длины, а другом ширины.
Найти площади круга, описывающего каждый из прямоугольников и записать в кортеж.
Найти среднее площадей и удалить все значения из списка больше неё на 10%.
Из полученных значений найти произведение и поделить его на длину входного списка
и вывести ответ. Итоговый ответ вернуть и вывести на экран.
При выполнении задания использовать функцию filter()."""

def random_list(maximum):
    r_list=[]
    for i in range (25):
        r_list.append(r.randint(1,maximum))
    return r_list

def area_circle_rectangle_transformation(list_lengh,list_width):
    """Диагональ прямоугольника это диаметр круга."""
    
    len_list_lengh=len(list_lengh)
    if len_list_lengh!=len(list_width):
        print("Неверные данные. Разное количество элементов.")
        return
    else:
        for i in range(len_list_lengh):
            if (list_lengh[i]<=0) or (list_width[i]<=0):
                print("Неверные данные. Нулевые или отрицательные значения.")
                return
        del i

    area_circle=[]
    for i in range(len_list_lengh):
        rectangle_diagonal=m.sqrt(m.pow(list_lengh[i],2)+m.pow(list_width[i],2))
        area_circle.append(m.pi*m.pow(rectangle_diagonal,2)/4)
    del i
    
    tuple_area_circle=tuple(area_circle)

    len_area_circle=len(area_circle)
    summ=0
    for i in range(len_area_circle):
        summ+=area_circle[i]
    del i
    average_area_circle=summ/len_area_circle
    del summ, len_area_circle
    
    filter_parameter=1.1*average_area_circle
    filtered_area_circle=list(filter(lambda x: x<=filter_parameter ,area_circle))

    answer=1
    len_filtered_area_circle=len(filtered_area_circle)
    for i in range(len_filtered_area_circle):
        answer*=filtered_area_circle[i]
    answer/=len_list_lengh
    return answer

r_list_lengh=random_list(50)
r_list_width=random_list(50)
thing=area_circle_rectangle_transformation(r_list_lengh,r_list_width)
print(f"Пункт 5. Итоговое значение: {thing}\n")
del r_list_lengh, r_list_width, thing


#Пункт 6.
"""Написать функцию, на вход которой подается наименьшее, наибольшее значение и шаг.
По этим параметрам сгенерировать заполненный список.
Посчитать количество чисел кратных 7 и отнять от него медиану всех чисел списка.
Если полученный результат отрицательный необходимо зеркально отобразить список,
если положительный, то создать копию старого списка и добавить в его начало полученное число.
Итоговый список вернуть и вывести на экран.
При выполнении задания использовать функцию filter()."""

def function(min_value=0, max_walue=100, step_value=1):
    
    input_list=list(range(min_value, max_walue+1, step_value))
    
    count_divisible_seven=len(list(filter(lambda x:x%7==0,input_list)))

    len_input_list=len(input_list)
    if len_input_list%2==0:
        median=(input_list[(len_input_list//2)-1]+input_list[len_input_list//2])/2
    else:
        median=input_list[len_input_list//2]
    del len_input_list
    
    result=count_divisible_seven-median
    del count_divisible_seven, median
    
    if result<0:
        input_list.reverse()
        output_list=input_list
    else:
        output_list=[result]+input_list
    
    return output_list

answer=function(1,7)
print(f"Пункт 6. Итоговый список: {answer}\n")
del answer


#Пункт 7.
"""Написать функцию, которая имитирует игру в кости.
На вход подается количество игроков, их имена.
На входе должны быть отображены их попытки выброса и итоговый результат с указанием победителя.
Результат выброса кости — это число от 1 до 6."""

def dice_game(numder_of_players, names):
    
    print("Пункт 7. Игра началась!")
    
    winner=[]
    round_counter=0
    while len(names)!=1:
        round_counter+=1
        print(f"\nРаунд: {round_counter}")
        
        print("Результаты бросков.")
        max_score=0
        for i in range(numder_of_players):
            score=r.randint(1,6)
            print(f"{names[i]}: {score}")
            if max_score>score:
                continue
            elif max_score==score:
                winner.append(names[i])
            else:
                winner.clear()
                winner.append(names[i])
                max_score=score
        
        names=list(winner)
        numder_of_players=len(winner)
        winner.clear()
        
        if numder_of_players!=1:
            print("В следующий раунд проходят: "+str(names)[1:-1].replace("\'",""))
    
    print(f"Победитель сегодняшней игры: {names[0]}\nПоздравляем победителя!\n")
    
players=['Лёша','Гриша','Миша','Гоша','Слава','Алина','Маша','Даша','Саша','Зоя',]
number_of_players=len(players)
dice_game(number_of_players, players)
del players, number_of_players
