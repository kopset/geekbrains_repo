#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

Name = str(input("Введите Ваше имя"))
Surname = str(input("Введите Вашу фамилию"))
Birthday = str(input("Введите дату Вашего рождения"))
YourTown =str(input("Введите город Вашего проживания"))
email =str(input("Введите Ваш email"))
Phone = str(input("Введите Ваш номер телефона"))

def about(Name,Surname,Birthday,YourTown,email,Phone):
    return Name+Surname+Birthday+YourTown+email+Phone

print(about(Name,Surname,Birthday,YourTown,email,Phone))