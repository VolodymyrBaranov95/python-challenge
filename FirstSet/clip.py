# coding: utf-8

"""
Напишите функцию, которая получает на вход последовательность чисел, а также ниж-
нюю границу a и верхнюю границу b и “обрезает” все числа в соответствии с этим диапа-
зоном. То есть все числа, меньшие a, должны быть заменены на a, а все числа, большие
b, — на b.
"""

def clip(sequnce, min_value, max_value):
    result =[]
    for value in sequnce:
        clipped = max(min(value , max_value), min_value)
        result.append(clipped)
    return result


l1 = [1,2,3,4,5,6,7,8,9]
l2 = [1,2,3,-10,-5,6,7]

print(clip(l1,2,4))
print(clip(l2,1,100))