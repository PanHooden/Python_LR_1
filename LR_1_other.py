import random as r
import math as m
import typing as t


# Пункт 1.1
"""Создать кортеж и заполнить его значениями от 1 до 10.
Вывести результат."""

list_1=[]
for i in range(1,11):
    list_1.append(i)
tuple_1=tuple(list_1)
print("\nП1.1",str(tuple_1)[1:-1])
del list_1, i, tuple_1


# Пункт 1.2
"""Создать список и заполнить его числами из кортежа, увеличив четные в 5 раз, а нечетные на три.
Добавить в конец списка все элементы кортежа.
Вывести результат.
Отсортировать список от большего к меньшему.
Вывести результат."""

list_2=[]
for i in range(11):
    list_2.append(i)
tuple_2=tuple(list_2)
list_2.clear()

for i in tuple_2:
    if i%2==0:
        list_2.append(i*5)
    else:
        list_2.append(i+3)
list_2+=list(tuple_2)
print("\nП1.2",list_2)

#Может не очень "quick", но прикольно. Лучше использовать list.sort() и list.reverse()
def quick_sort(input_list,rule="up"):
    if rule not in ["up","down"]:
        raise ValueError(f"Некорректные данные. Вместо {rule} выберете 'up' или 'down'.")
    
    main_element=input_list[r.randint(0,(len(input_list)-1))]
    list_low=[]
    list_high=[]
    list_equal=[]
    
    for i in input_list:
        if main_element>i:
            list_low.append(i)
        elif main_element<i:
            list_high.append(i)
        else:
            list_equal.append(i)
    
    if len(list_low)>1:
        list_low=quick_sort(list_low,rule)
    if len(list_high)>1:
        list_high=quick_sort(list_high,rule)
    
    if rule=="up":
        return list_low+list_equal+list_high
    else:
        return list_high+list_equal+list_low

list_2=quick_sort(list_2,"down")
print("П1.2",list_2)
del i, tuple_2, list_2

# Пункт 1.3
"""Создать множество и заполнить его данными из списка.
Вывести результат."""

def random_list(min=1, max=10, count=20):
    r_list=[]
    for i in range (count):
        r_list.append(r.randint(min,max))
    return r_list

set_3=set()
for i in random_list():
    set_3.add(i)
print("\nП1.3",set_3)
del set_3, i


# Пункт 1.4
"""Задать произвольный список и поменять местами первый и последний элемент в списке."""

list_4=random_list()
list_4=[list_4[-1]]+list_4[1:-1]+[list_4[0]]
print("\nП1.4",list_4)
del list_4


# Пункт 1.5
"""Написать функцию, на вход которой подается наименьшее, наибольшее значение и шаг.
По этим параметрам сгенерировать заполненный список и рассчитать корень из суммы квадратов четных чисел.
Создать множество и добавить туда нечетные числа кратные 3.
Итоговое множество вернуть и вывести на экран.
При выполнении задания использовать функцию filter()."""

def func_1_5(start=1, stop=10, step=1):
    list_5=[]
    for i in range(start, stop, step):
        list_5.append(i)
    summa=0
    for i in list_5:
        if i%2==0:
            summa+=i
    koren=m.sqrt(summa)
    set_5=set(list(filter(lambda x: x%3==0,\
        list(filter(lambda x: x%2!=0,\
            list(range(100)))))))
    return set_5
print("\nП1.5",func_1_5())


# Пункт 1.6
"""Написать функцию, на вход которой подается словарь,
содержащий ключ в виде строки и значение в виде целого числа.
Также на вход подается список из ключей.
По ключам из этого списка нужно достать значения и найти медиану для полученных чисел.
Удалить из словаря все пары ключ-значение значение которых меньше медианы.
Итоговый словарь вернуть и вывести на экран.
При выполнении задания использовать функцию filter()."""

def func_1_6(input_dictionary: t.Dict [str, int], input_list: t.List[str])->t.Dict[str, int]:
    value_list=[]
    for key in input_list:
        value_list.append(input_dictionary[key])
    value_list.sort()
    
    len_value_list=len(value_list)
    if len_value_list%2==0:
        median=(value_list[(len_value_list//2)-1]+value_list[len_value_list//2])/2
    else:
        median=value_list[len_value_list//2]
    del value_list, key, len_value_list
    
    filtered_list=list(filter(lambda key: input_dictionary[key]<median,input_list))
    for key in filtered_list:
        del input_dictionary[key]
    return input_dictionary

def key_gen (size:int=20)->t.List[str]:
    key_list=[]
    for i in range(size):
        key_list.append(chr(r.randint(65,90))+chr(r.randint(97,122))+chr(r.randint(97,122))\
            +"|"+chr(r.randint(10241,10495)))
    return key_list

key_list=key_gen()
dictionary=dict()
for i in key_list:
    dictionary[i]=r.randint(10,100)
    
print("\nП1.6",func_1_6(dictionary,key_list))
del key_list, dictionary, i


# Пункт 1.7
"""Написать функцию, которая запрашивает, сколько времени вам потребовалось, чтобы пробежать 10 км в минутах.
Функция продолжает спрашивать, сколько времени потребовалось для дополнительных пробежек,
пока пользователь не нажмет Enter в консоли.
В этот момент функция завершает работу — но только после вычисления и отображения среднего времени,
затраченного на пробег в 10 км."""

def running():
    print("\nДля результата расчёта нажмите Enter")
    count=0
    summa=0
    while True:
        count+=1
        time=input(f"\nВведите время {count} пробежки в минутах: ")
        if time=='':
            count-=1
            break
        try: 
            time=float(time)
            summa+=time
        except ValueError:
            print("Некорректные данные. Введите число.")
            count-=1
            continue
    if summa==0:
        print("Необходимы хоть какие-то данные.")
        running()
    else:
        print(f"Среднее время: {round(summa/count,4)}")

running()