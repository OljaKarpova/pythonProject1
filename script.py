per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("money "))
list = list(per_cent.values()) #создаем список значений словаря per_cent
for i in range (0,4):
    list[i] = round(list[i]/100*money, 2) #заменяем каждое значение списка list вычисленным депозитом с округлением до сотых (копейки)
print("deposit = ", list)
print("Максимальная сумма, которую вы можете заработать —", max(list))

