import random as r
import math as m
import typing as t

def key_gen (size:int=20)->t.List[str]:
    key_list=[]
    for i in range(size):
        key_list.append(chr(r.randint(65,90))+chr(r.randint(97,122))+chr(r.randint(97,122))\
            +"|"+chr(r.randint(10241,10495)))
    return key_list

def random_list(min_value:int=1, max_value:int=10, size:int=20):
    r_list=[]
    for i in range (size):
        r_list.append(r.randint(min_value,max_value))
    return r_list

# Пункт 2.3
"""Создать словарь и заполнить его следующим образом:
ключ – элемент множества, значение – элемент списка.
Вывести результат."""

set_key=set(key_gen())
list_value=random_list()
dictionary=dict()
i=0
for key in set_key:
    dictionary[key]=list_value[i]
    i+=1
print("\nПункт 2.3:", dictionary)
del set_key, list_value, dictionary, i, key

# Пункт 2.4
"""В массиве из n элементов найти порядковый номер элемента x с помощью написания функции."""
# Если мы берём отсортированный массив
def bi_find(target, input_list):
    central_element_index=len(input_list)//2
    if len(input_list)<2:
        return input_list[0]
    if target<input_list[central_element_index]:
        element=bi_find(target, input_list[0:central_element_index])
    elif target>input_list[central_element_index]:
        element=bi_find(target, input_list[central_element_index+1:len(input_list)])
    else:
        element=input_list[central_element_index]
    return element

longer=99
for item in range(longer):
    f_1=bi_find(item,list(range(longer)))
    f_2=list(range(longer)).index(item)
    if f_1==f_2:
        print(f"Верно для: {f_1}")
    else:
        print(f"Неверно для: {f_1}")
del longer, item, f_1, f_2

# Пункт 2.4
"""В массиве из n элементов найти порядковый номер элемента x с помощью написания функции."""