"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

dictionary = {"One": "Один",
            "Two": "Два",
            "Three": "Три",
            "Four": "Четыре"}

note = open("hw_4.txt", "r", encoding='UTF-8')
output = open("hw_4_1.txt", "w", encoding='UTF-8')
info = note.readlines()
for line in info:
    upd_list = line.split(" — ")
    output.write(f"{dictionary[upd_list[0]]} - {upd_list[1]}")