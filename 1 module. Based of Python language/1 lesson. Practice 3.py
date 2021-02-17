n = str(input("Определим сумму чисел n + nn + nnn. Введите !ЦЕЛОЕ! число n."))
nn = n + n
nnn = nn + n
sum = int(n)+int(nn)+int(nnn)
print("Числа для суммирования: ",n,",",nn,",",nnn)
print("Сумма составила: ",sum)