"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

note = open("hw_3.txt", "w", encoding='UTF-8')
man = input("Введите ФИО сотрудника и его оклад в у.е. через пробел: ")
while man != " ":
    note.writelines(man + '\n')
    man = input("Для завершения введите пробел+Enter или введите ФИО сотрудника и оклад через пробел: ")
else:
    price = []
    inter = []
    name = []
    note = open("hw_3.txt", "r", encoding='UTF-8')
    chel = note.readlines()
    output = []
    money =[]
    for time in chel:
        name, price = time.split(" ")
        price=int(price)
        money.append(price)
        if price < 20000:
            output.append(price)
            print(f"Оклад сотрудника {name} составляет менее 20 тыс у.е.")
#    print(f"Количество строк {len(chel)}")
    print(f"Средний доход сотрудников, кто получает менее 20 тыс у.е. составляет {sum(output) / len(output)} у.е.")
    print(f"Средний доход всех сотрудников составляет {sum(money) / len(chel)} у.е.")