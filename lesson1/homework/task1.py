# Найдите сумму цифр трехзначного числа.

n = int(input("enter number: "))
summa = 0
while n > 0:
#можно написать while n: это будет значит пока n истинно -> то есть больше нуля
    summa += n % 10 # summa = summa + n % 10
    n //= 10 # n = n // 10
print(summa)
