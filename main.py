name = input('Введите своё имя: ')
sure_name = input('Введите свою фамилию: ')
old = int(input('Введите свой возраст: '))
weight = float(input('Введите свой вес: '))
print('Ваши данные: ', name, sure_name, ':', 'возраст', old, 'вес', weight)

if old <= 30 and weight >= 50 <= 120:
    print(name, sure_name, 'возраст', old, 'вес', weight, ' - Пациент в хорошем состоянии!')  #Если <= 30 лет, вес => 50 и =< 120 кг

elif old > 30 <= 40 and weight < 50 > 120:
    print(name, sure_name, 'возраст', old, 'вес', weight, ' - Пациенту требуется заняться собой!')  #Если > 30, вес < 50 или > 120 кг

elif old > 40 and weight < 50 > 120:
    print(name, sure_name, 'возраст', old, 'вес', weight, ' - Пациенту требуется врачебный осмотр!')  #Если > 40, вес < 50 или > 120 кг

else:
    print(name, sure_name, 'Ты МОЛОДЕЦ!')  #Выполняется во всех других случаях
