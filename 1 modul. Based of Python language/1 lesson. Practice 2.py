a = int(input("Введите время в секундах для преобразования в формат ЧЧ:ММ:СС"))
det1 = 3600
hour = a // det1
det2 = 60
minutes = (a - hour * det1) // det2
s = a - hour * det1 - minutes * det2
if hour < 10:
    time = f"Время составляет: {hour:02}:{minutes:02}:{s:02}"
else:
    time = f"Время составляет: {hour}:{minutes:02}:{s:02}"
print(time)




