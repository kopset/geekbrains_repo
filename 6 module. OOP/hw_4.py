"""4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""

class Car:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        if self.speed>0:
            print(f"Your {self.color} car {self.name} is going!")
            wantStop=input("Do you want to stop it (in English: yes, no)? ")
            if str.lower(wantStop) == "yes":
                self.speed = 0
                return print(f"You was stopped! Your speed is {self.speed} km/h now")
            else:
                wantFaster=int(input(f"Your steel going. Your speed is {self.speed} km/h now.\n"
                                 f"Do you want to drive faster? Insert a new speed "))
                if wantFaster<self.speed:
                    print(f"Faster that mean that your new speed will be more {self.speed}")
                else:
                    self.speed=wantFaster
                    print(f"Your new speed is {self.speed}")

    def stop(self):
        if self.speed==0:
            print(f"Your {self.color} car {self.name} is parked!")
            wantGo = input("Do you want to start riding (in English: yes, no)? ")
            if str.lower(wantGo) == "yes":
                self.speed = 20
                return print(f"Take your steering wheel, Driver! Your speed is {self.speed} km/h now")
            else:
                print(f"Your steel parking. Your safety is very well!")
        else:
            print(f"Your {self.color} car {self.name} is going!")
            wantStop = input("Do you want to stop it (in English: yes, no)? ")
            if str.lower(wantStop) == "yes":
                self.speed = 0
                return print(f"You was stopped! Your speed is {self.speed} km/h now")

    def turn(self):
        turnSide=input("Are you want to turn your driving wheel? Choose the direction (left, right) ")
        if self.speed == 0:
            print("Are you serious? You shell to start riding first!")
        else:
            if turnSide == "left":
                print("Look to the sky. Oh, sh...t...it was a some beast in the road. Sorry for that.\n"
                      "At next time look where you driving!")
            else:
                print("Good move! Let's drive more!")

    def show_speed(self):
        print(f"Your driving speed is {self.speed} km/h")

class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed>60:
            print("Your driving speed is too hight! Please, drive some slowly.\n"
                  "May be you know but your maximum speed is 60 km/h")
        else:
            print("Your speed is fine! Let's drive more!")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Your driving speed is too hight! Please, drive some slowly.\n"
                  "May be you know, but your maximum speed is 40 km/h")
        else:
            print("Your speed is fine! Let's drive more!")

class PoliceCar(Car):
    pass

car=TownCar(70,"Черный","VW")
car.go()
car.stop()
car.turn()
car.show_speed()

car=WorkCar(50,"Yellow","Caterpilar")
car.go()
car.stop()
car.turn()
car.show_speed()