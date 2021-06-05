from io import TextIOWrapper

# l = ["Первая строка\n", "Вторая строка\n", "Третья строка\n"]
l = ["Первая строка", "Вторая строка", "Третья строка"]


f_o = open("my_shiny_file.txt", "w", encoding='UTF-8')
print("hhtyhthty", file=f_o)
# f_o = open("sample.pdf", "rb")
# print(f_o.read())

# [open("testfile.txt", "w") for _ in range(102300)]

# print(f_o)
# for el in l:
#     print(f_o.write(el))
# f_o.writelines(l)
# res = f_o.read()
# res = f_o.readlines()
# print(res)
# res = f_o.readline()

# print(f_o.tell())
# f_o.seek(6)
# print(f_o.tell())
# for el in f_o:
#     c = 1
#     print(el, end='')

# print(f_o.closed)
# f_o.close()
# print(f_o.closed)


# class MyPirozhok:
#     def __enter__(self):
#         print("начинаю работу с пирожком в менеджере контекста")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("заканчиваю работу с пирожком в менеджере контекста")
#
#
# pirozhok = MyPirozhok()
#
# print("начало работы")
# with pirozhok:
#     raise ZeroDivisionError
#     print("работаю")
#
# print("конец")


import json
#
# # получаем данные из json
with open("json_example.json", "r") as json_obj:
    data = json.load(json_obj)
    print(data)
    print(type(data))
    # some_data = {"user_id": 123123,
    #              "position": "devloper",
    #              "city": "Moscow",
    #              "l": [1, 2, 3, {"fd": 123}]
    #              }
    # s = json.dump(some_data, json_obj)
    # print(s)




import sys from io import BufferedReader, TextIOWrapper


# class SimpleClass:
#     def __enter__(self):
#         print("зашли в энтер")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("зашли в экзит")


# simple_class = SimpleClass()
#
# with simple_class:
#     print("работаем!")
#     raise Exception("ОШИБКА ОШИБОК!!!")
#
# print("закончили совсем работать")




# f_o = open("testfile.txt", "r")
# f_o.seek(12)
# print(f_o.tell())
# f_o.readline()
# print(f_o.tell())
























def test_func():
    file_object = open("testfile.txt", "w")
    file_object.write("dsfgsfgsd")
    raise Exception


def second_func():
    try:
        test_func()
    except Exception as err:
        c = 1
        print("error")


# second_func()
# file_object_2 = open("testfile.txt", "w")
# print(file_object_2.tell())
# file_object_2.write('sdasf')
# x = [open("testfile.txt", "w") for _ in range(102300)]








# a = 1
# b = 2
#
# BufferedReader









class SomeClassWithContext:
    def __enter__(self):
        print("Этот метод запускается, когда мы передаём объект в менеджер контекста")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Этот метод запускается, когда мы заканчиваем работу с объектом в менеджере контекста")
        if exc_type:
            print("Случиласть ошибка!!!")

    def some_meth(self):
        pass

# c = 1
# some_obj = SomeClassWithContext()
# with some_obj:
#     print("какая-то логика")
#     some_obj.some_meth()
#     raise ValueError("Ошибка!!!", 1, 2, [123123412341234, 232345345])
#     c = 1
# c = 1





# file_object = open("testfile.txt", "w")
# with file_object:
#     pass

# with SomeClassWithContext():
#     print("контекст")
#     print("контекст")
#     print("контекст")
#     print("контекст")
#     raise Exception("Error message", 'asfdsf', 'asdasdf', 'asdadsf')
#     print("контекст")
#     print("контекст")
#     print("контекст")







# some_io_wrapper = open("testfile.txt", "w")
#
# # Делаем объект, с которым можно работать в менеджере контекста
# some_context_object = SomeClassWithContext()
# with some_context_object, some_io_wrapper:
#     some_io_wrapper.write("Первая строка\n")
#     print('выполнение контекста')
#     print('выполнение контекста')
#     print('выполнение контекста')
#     print('выполнение контекста')
#     print('выполнение контекста')
#     # raise ValueError("Древнее зло вырвалось на свободу!!!")
# print("ЗАВЕРШЕНО")

# ЗАДАЧА МЕтОДОВ enter и exit - автоматизировать процессы работы с какими-то объектами и защитить нас
# от ситуаций, где мы можем что-то недосмотреть.


# Пример с плитой
# class AutomaticPlita():
#     def __enter__(self):
#         print("Плита автоматически включилась")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Плита автоматически выключилась")


# time_to_cook = 5
# autimatic_plite = AutomaticPlita()
# with autimatic_plite:
#     current_time = 0
#     while current_time <= time_to_cook:
#         user_status = input(f"Прошло времени: {current_time}. Вы там случайно не уснули? y/n? : ")
#         if user_status.lower() == "y":
#             raise Exception("ПОЛЬЗОВАТЕЛЬ ПЛИТЫ ЗАСНУЛ!!!")
#         current_time += 1
#     print("пельмешки готовы")