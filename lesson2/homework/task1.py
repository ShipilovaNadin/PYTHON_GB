# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

n = int(input("Number of all coins: "))
heads_num = tails_num = 0

for _ in range(n):
    num = int(input("Введите 1 если монета повернута гербом вверх и 0 если вверх решкой "))
    if num == 1:
        heads_num += 1
    else:
        tails_num += 1
print(heads_num, tails_num)

if heads_num > tails_num:
    print(tails_num)
else:
    print(heads_num)