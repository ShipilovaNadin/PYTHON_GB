# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# вариант 1
# import random, os
# os.system('cls')
	
# N = [random.randint(-10, 10) for _ in range(int(input("Введите количество элементов в первом массиве ")))]
# M = [random.randint(-10, 10) for _ in range(int(input("Введите количество элекментов во втором массиве ")))]
	
# print(f"{N}\n{M}")
# result = list()
# for n in N:
#     if n not in M:
#         result.append(n)
#     print(result)
	
# print([n for n in N if n not in M])

#вариант 2

a = list(map(int, input("Введите элементв массива N ").split()))
b = list(map(int, input("Введите элементв массива M ").split()))
print(*list([items for items in a if items not in b]))