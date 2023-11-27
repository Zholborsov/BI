from math import floor
'''Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно.
Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.'''
def sum_range(start: int, end: int):
    if start > end:
        start, end = end, start
    i = start
    sumOfNumbers = 0
    while i <= end:
        sumOfNumbers = sumOfNumbers + i
        i += 1
    print("Sum of numbers =", sumOfNumbers)
sum_range(1,5)

'''Создайте функцию three_args(), которая принимает 1, 2 или 3 строго ключевых параметра.
В результате её работы на печать в консоль выводятся значения переданных переменных, но только если они не равны None.
Получим, например, следующее сообщение: «Переданы аргументы: var1 = 2, var3 = 10».'''
# На примере вебинара
def three_args(arg1, arg2 = None, arg3 = None):
    argument = arg1
    if arg2 != None:
        argument = argument + ', ' + str(arg2)
    elif arg3 != None:
        argument = argument + ', ' + str(arg3)
    print(f"Переданы аргументы: {argument}")

three_args(arg1 = 21)
three_args(arg1 = "Python", arg3 = 3)
three_args(arg1 = "Python", arg2 = 3, arg3 = 9)

# Способ с выводом аргументов в консоль
def three_args(var1 = None, var2 = None, var3 = None):
    resultString = "Переданы аргументы: "
    if var1 != None:
        resultString += "var1 = " + str(var1)
    if var2 != None:
        resultString += ", var2 = " + str(var2)
    if var3 != None:
        resultString += ", var3 = " + str(var3)
    print(resultString)

three_args(var1 = 21)
three_args(var1 = "Python", var3 = 3)
three_args(var1 = "Python", var2 = 3, var3 = 9)

'''В функцию передается переменная, в которой хранится слово из латинских букв.
Напишите код, который вернет из функции: среднюю букву, если число букв в слове нечетное; две средних буквы, если число букв четное.
После выполнения функции возвращаемый результат вывести на экран.'''
def middleChar(someString: str):
    lenOfString = len(someString)
    centerIndex = floor((lenOfString-1)/2)
    if lenOfString %2 != 0: # НЕчетное число
        return someString[centerIndex]
    else:
        return someString[centerIndex:centerIndex + 2]
print(middleChar("test"))
print(middleChar("testing"))

'''Напишите функцию, в которую будут передавать 2 числа.
Верните результат умножения если, произведение равно или больше 1000, в противном случае верните сумму двух чисел.'''
def multipleOrAdd(numberOne: int, numberTwo: int):
    if numberOne * numberTwo >= 1000:
        print(numberOne * numberTwo)
    else:
        print(numberOne + numberTwo)
multipleOrAdd(10, 10)
multipleOrAdd(10, 100)
multipleOrAdd(10, 1000)

'''Напишите функцию, которая принимает положительное целое число от 0 до 100.
Если это четное число, то функция возвращает сумму всех чисел от 0 до переданного числа (включая его),
если число нечетное, то функция возвращает произведение всех чисел от 0 до переданного.'''
def addOrMultiple(number):
    if number <0 or number > 100:
        print("Введено некорректное значение! Требуется число от 0 до 100 включительно.")
    else:
        if number %2 == 0:
            sumOfNumbers = 0
            for number in range(0, number + 1):
                sumOfNumbers += number
            print(sumOfNumbers)
        else:
            multipleOfNumbers = 1  # Тут единица, так как умножение на 0 даст результат 0 в любом случае
            for number in range(1, number + 1):  # И тут начальное число не 0 по тому же принципу
                multipleOfNumbers *= number
            print(multipleOfNumbers)
addOrMultiple(10)
age = int(input("Введите ваш возраст\n"))

try:
    name = input("What is your name? ")
    print(name)
except EOFError:
    print("EOFError raised")