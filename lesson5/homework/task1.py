# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def degree(a, b):
    if b == 0:
        return 1
    if b < 0:
        return degree(a, b + 1) * 1/a
    return degree(a, b - 1) * a
  
a = int(input("Введите число А "))
b = int(input("Введите число В "))
print(degree(a, b))   

