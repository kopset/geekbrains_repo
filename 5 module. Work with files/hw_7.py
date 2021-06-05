"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
+Пример строки файла: firm_1 ООО 10000 5000.
+Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
+Если фирма получила убытки, в расчет средней прибыли ее не включать.
+Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
+Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
+Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
+Итоговый список сохранить в виде json-объекта в соответствующий файл.
+Пример json-объекта:
+[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

+Подсказка: использовать менеджеры контекста."""

import json

j_file = open("hw_7.json", "w", encoding='UTF-8')
note = open("hw_7.txt", "r", encoding='UTF-8')
company_list= {}
average = {}
s_profit = 0
quant = 0
lines = note.read().split("\n")
print(lines)
for company_info in lines:
    company_info = company_info.split()
    profit = int(company_info[2]) - int(company_info[3])
    l1=company_info[0],profit
    if profit > 0:
        print(f"Прибыль компании {company_info[0]} составила {profit} у.е.")
    else:
        print(f"Убыток компании {company_info[0]} составила {abs(profit)} у.е.")
    company_list[company_info[0]] = profit
    if profit > 0:
        s_profit += profit
        quant += 1
    average["Average profit"] = s_profit / quant
    company_list[company_info[0]] = profit
print(f"Средняя прибыль компаний, которые имеют прибыль, составила {s_profit / quant} у.е.")
print(company_list)
company_list = [company_list, average]
print(company_list)

json.dump(company_list, j_file)