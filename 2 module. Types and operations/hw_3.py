#Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
#wint=[12, 1, 2]
#spr=[3, 4, 5]
#sum=[6, 7, 8]
#aut=[9, 10, 1]
season = {
    "зима": (12, 1, 2),
    "весна": (3, 4, 5),
    "лето": (6, 7, 8),
    "осень": (9, 10, 1)
}
print(season)

month = int(input("Введите месяц, сезон года которого хотите определить:"))
for i in season.keys():
    if month in season[i]:
        print(i)