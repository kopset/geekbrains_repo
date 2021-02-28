"""Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) - 50(пр) - 20(лаб).
Физика: 30(л) —  - 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""



print("")
dictionary = {}
note = open("hw_6.txt", "r", encoding='UTF-8')
note = note.readlines()
c=[]
for line in note:
    subject, workload = line.split(":")
#    print(subject)
#    print(workload)
    workload_s=sum(map(int,''.join([i for i in workload if i==" " or i.isdigit()]).split()))
#    print(workload_s)
    dictionary[subject] = workload_s
print(f"Результирующий словарь имеет вид: {dictionary}")