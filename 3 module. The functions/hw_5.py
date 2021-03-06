# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def summa():
    s = 0
    while True:
        l1 = input("Введите строку из нескольких чисел, разделенных пробелом. "
             "\nЕсли хотите остановить расчет введите букву s ")
        count=l1.count("s")
        if count>=1:
            s += sum(map(int, l1[:l1.index("s") - 1].split()))
            break
        s += sum(map(int, l1.split()))
        print(f"Сумма составила: {s}")
    return s

print(f"Общая сумма составила: {summa()}")

