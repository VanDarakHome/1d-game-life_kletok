import time
print("Привет, это игра 1D жизнь клеток, с правилами можно ознакомится в README")
print("Введи длину строки")
string_len = input()
while not string_len.isdigit():
    print("Введи число")
    string_len = input()
string_len = int(string_len)
line = ['*'] * string_len
print("Теперь введите саму строку")
string = input()
while len(string) != len(line):
    print("А вам не кажется уважаемый игрок, что если длина строки", len(line), 'символов(так вы указали),')
    print("то длина строки не может быть равна", len(string), '(если что это длина строки, которую вы ввели)')
    string = input()
for i in range(string_len):
    if string[i] == ' ':
        line[i] = ' '
print(line)
