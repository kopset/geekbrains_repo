"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

note = open("hw_5.txt", "w", encoding='UTF-8')
digit = input("Введите числа через пробел: ")
note.write(digit)
note = open("hw_5.txt", "r", encoding='UTF-8')
summary = note.read()
sum_list = summary.split()
sum_list=[int(item) for item in sum_list]
print(f"Сумма введенных чисел составила: {sum(sum_list)}")