# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр 
# равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

n = str(input("enter number of ticket: "))
a = int(n[0]) + int(n[1]) + int(n[2])
b = int(n[3]) + int(n[4]) + int(n[5])
if a == b:
    print("Yes - lucky ticket")
else:
    print("No")

    """Вариант считать математически   
    ticket_number = int(input())
    
    sum_first = 0
    sum_second = 0

    while ticket_number:
        digit = ticket_number % 10
        if ticket_number>999:
            sum_first += digit
        else:
            sum_second += digit
        ticket_number //= 10

    print(f"The ticket is lucky: {sum_first == sum_second}")
    
    """
