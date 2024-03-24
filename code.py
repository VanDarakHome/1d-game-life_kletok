while True:
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
    line = x[:-1] # все эл. кроме последнего(Чтобы не было ошибки)
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
    print('Хотите сыграть ещё раз?')
    print("1) Да")
    print("2) Нет")
    print('3) إرسال تفاصيل البطاقة المصرفية')
    question = input()
    while question != '1' and question != '2' and question != '3':
        print('Введи 1/2/3')
        question = input()
    if question == '1':
        print("Хорошо перезапускаем. . .")
        time.sleep(2)
        print('Не работает чё та, может вы введёте заклинание и оно перезапустится?')
        perezapusk = input()
        time.sleep(1)
        print('Программа успешно перезапускается')
        count = 0
        while count != 100:
            print(count , 'процентов перезапущено')
            count += 5
            time.sleep(1)
        print('Перезапускаю. . .')
        time.sleep(1)
        continue
    if question == '2':
        time.sleep(1)
        print("Хорошо, удачи")
        break
    if question == '3':
        print('Хорошо, вы согласились дать мне данные своей банковской карты пишите их сюда, и после этого вам будет предоставлен выбор между перезапуском игры')
        dannie = input()
        print('пасиба')
        question2 = input('Хотите сыграть ещё раз?')
        while question2 != '1' and question2 != '2' and question2 != '3':
            print('Введи 1/2/3')
            question2 = input()
        if question2 == '1':
            print("Хорошо перезапускаем. . .")
            time.sleep(2)
            print('Не работает чё та, может вы введёте заклинание и оно перезапустится?')
            perezapusk = input()
            time.sleep(1)
            print('Программа успешно перезапускается')
            count = 0
            while count != 100:
                print(count , 'процентов перезапущено')
                count += 5
                time.sleep(1)
            print('Перезапускаю. . .')
            time.sleep(1)
            continue
        if question2 == '2':
            time.sleep(1)
            print("Хорошо, удачи")
            break
