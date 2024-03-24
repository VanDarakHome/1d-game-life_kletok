import time
print("Привет, это игра 1D жизнь клеток, с правилами можно ознакомится в README")
print("Введи длину строки")
string_len = input() # Вводим длину строки
# ---------------------------------
while not string_len.isdigit():
    print("Введи число")               # Блок отвечающий за то что вводится длина строки
    string_len = input()               # превращающий строку в число
string_len = int(string_len)
# ----------------------------------
line = ['*'] * string_len
print("Теперь введите саму строку")
string = input()
while len(string) != len(line):
    print("А вам не кажется уважаемый игрок, что если длина строки", len(line), 'символов(так вы указали),')
    print("то длина строки не может быть равна", len(string), '(если что это длина строки, которую вы ввели)')
    string = input()
for i in range(string_len):          # Блок отвечающий за ввод самой строки с последующий превращением в символы
    if string[i] == ' ':             # Пример: fgр г ю   Шифр: *** * *
        line[i] = ' '
# ---------------------------------
print("Введите количество поколений")
pokoleniya = input()
while not pokoleniya.isdigit():      # Ввод поколений
    print("Введи число")
    pokoleniya = input()
pokoleniya = int(pokoleniya)
# ----------------------------------
for i in line:
    print(i, end="")
print()                                          # Подготовка к следующему поколению
line.append(line[0])
x = line # Копия строки
line = x[:-1] # все эл. кроме последнего
# -----------------------------------
for i in range(pokoleniya):
    for j in range(string_len):
        x2 = 0
        if line[j - 1] == "*":
            x2 += 1
        if x[j + 1] == "*":
            x2 += 1
        if x[j] == "*":
            if x2 != 1:
                x[j] = " "
        else:
            if x2 == 1:                          # Работа самих поколений
                x[j] = "*"
    if line == [' '] * string_len:
        print('В мире не осталось живых клеток!')
        break
    line = x[:-1]
    x[-1] = x[0]
    for j in line:
        print(j, end="")
    print()
    time.sleep(0.5)
# x - Копия строки x2 - счётчик
# line - строка вывод на экран
# j - элемент строки
