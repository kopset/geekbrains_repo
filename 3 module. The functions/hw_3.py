#Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов

a1 = int(input("Введите первое число"))
a2 = int(input("Введите второе число"))
a3 = int(input("Введите третье число"))

def my_func(a1, a2, a3):
    s = [a1, a2, a3]
    m = min(s)
    my_func=sum(s)-m
    return my_func

print(my_func(a1,a2,a3))

