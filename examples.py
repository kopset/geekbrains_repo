#Класс со словарем
class Sevice:
    def __init__(self,months):
        self.__dict__.update(months)

months = {"jan":1,"feb":2,"march":3}
service=Sevice(months)
print(service.jan)

#Запрос из словаря
income = {'wage': 10000, 'bonus': 1500}
return income['wage']+income['bonus']

