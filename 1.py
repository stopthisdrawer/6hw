a = input("Выберите действие: ")

if a == '+':
    print(int(input('Введите первое число: ')) + int(input("Введите первое число: ")))
elif a == '-':
    print(int(input('Введите первое число: ')) - int(input("Введите первое число: ")))
elif a == '*':
    print(int(input('Введите первое число: ')) * int(input("Введите первое число: ")))
elif a == '/':
    print(int(input('Введите первое число: ')) / int(input("Введите первое число: ")))
else:
    print("Я вас не понял")