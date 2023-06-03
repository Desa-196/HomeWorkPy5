'''
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
'''

def read_float_from_console(text):
    read_int = 0
    while(True):
        try:
            read_int = float(input(text))
        except:
            print('Введено не число!')
            continue
        return read_int

        
def read_int_from_console(text):
    while(True):
        try:
            #Ввод пытаемся преобразовать в число с плавающей точкой, на случай если ввели не целое число
            readInt = float(input(text))
        #Если при преобразовании в float возникло исключение, выводим ошибку и завершаем иттерацию цикла while
        except:
            print('Введено не число!')
            continue
        #Если попали сюда, значит всё нормально, проверяем равны ли числа типа float и преобразованное в int(откинули дробную часть если она была)
        if  int(readInt) == readInt:
            return int(readInt)
        print('Число должно быть, целым!')

def stepen(a, b):
    if b == 0:
        return 1
    #Если степень положительная
    if b > 0: return a * stepen(a, b - 1)
    #Если степень отрицательная
    else: return 1/a * stepen(a, b + 1)

a = read_float_from_console("Введите число: ")
b = read_int_from_console("Введите целое число в степень которого нужно возвести: ")
print(stepen(a, b))

