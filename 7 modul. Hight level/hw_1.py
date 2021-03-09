"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д."""


class Matrix:
    def __init__(self, number):
        self.number = number

    #    def __str__(self):
    #        for number in self.number:
    #            print(number)

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.number]))

    # работает только для матриц одинакового количества ячеек!!!
    def __add__(self, other):
#        print(f"Количество строк матрицы 1: {len(self.number)} шт")
#        print(f"Количество столбцов матрицы 1:{len(self.number[0])} шт")
#        print(f"Количество строк матрицы 2:{len(other.number)} шт")
#        print(f"Количество столбцов матрицы 2:{len(other.number[0])} шт")
        # количество строк
        n = len(self.number) - len(other.number)
        # количество столбцов
        m = len(self.number[0]) - len(other.number[0])

        if n > 0:
            i = 1
            while i <= len(self.number) - len(other.number):
                j = 0
                c=[]
                while j <= len(self.number[0]):
                    c.append(0)
                    j += 1
                other.number.append(c)
                i += 1
        elif n < 0:
            i = 1
            while i <= len(other.number) - len(self.number):
                j = 0
                c=[]
                while j <= len(other.number[0]):
                    c.append(0)
                    j += 1
                self.number.append(c)
                i += 1
        if m > 0:
            for el in self.number:
                for elem in other.number:
                    j = 1
                    while j <= len(el) - len(elem):
                        elem.append(0)
                        j += 1
        elif m < 0:
            for el in self.number:
                for elem in other.number:
                    j = 1
                    while j <= len(elem) - len(el):
                        el.append(0)
                        j += 1
        for i in range(len(self.number)):
            for j in range(len(other.number[i])):
                self.number[i][j] = self.number[i][j] + other.number[i][j]
        return Matrix.__str__(self)


mtrx1 = Matrix([[31, 22], [37, 43], [51, 86]])
mtrx2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
mtrx3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
#print(mtrx1.number)
print(f"Матрица 1 имеет вид:\n{mtrx1}")
#print(mtrx2.number)
print(f"Матрица 2 имеет вид:\n{mtrx2}")
#print(mtrx3.number)
print(f"Матрица 3 имеет вид:\n{mtrx3}")
print(f"В результате сложения матрица приняла вид:\n{mtrx2 + mtrx3}")
