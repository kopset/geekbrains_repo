#git checkout -b homework3

#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
x1 = int(input("Введите первое число"))
x2 = int(input("Введите второе число"))

def discr(x1, x2):
    if x2==0:
        print("Выполнение деления на 0 запрещено")
    else:
        return x1/x2
print(discr(x1,x2))