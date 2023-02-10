# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

set1 = {int(input("Введите элементы множества n: ")) for _ in range(n)}
print(set1)
set2 = {int(input("Введите элементы множества m: ")) for _ in range(m)}
print(set2)

print("Элементы входящие в оба множества: ", *list(set1.intersection(set2)))