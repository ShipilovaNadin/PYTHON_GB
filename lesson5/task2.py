# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def max_to_min(list):
    minimum = min(list)
    maximum = max(list)
    return [minimum if i == maximum else i for i in list]

print(*max_to_min([int(i) for i in input().split()]))   