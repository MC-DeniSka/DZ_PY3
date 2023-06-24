# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
n = int(input('Введите колличество элементов массива '))
Massive = [random.randint(1,10) for i in range(n)]
print (Massive)
a = int(input('Введите число '))
m = abs(a-Massive[0])
index_element = 0
for i in range(1,n):
    buf = abs(a-Massive[i])
    if buf < m:
        m = buf
        index_element = i
print (Massive[index_element])



# import random
#
# N = int(input("Введите количество элементов в массиве "))
# list = [random.randint(1, 20) for i in range(N)]
# print(list)
# x = int(input("Введите искомое число "))
# index_element = 0
# min_element = abs(x - list[0])
# for i in range(1, N):
#     buffer_element = abs(x -list[i])
#     if buffer_element < min_element:
#         min_element = buffer_element
#         index_element = i
#
# print(list[index_element])