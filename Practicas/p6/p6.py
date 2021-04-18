import math


class Calculator:

    def add(self, x, y):
        self.x = x
        self.y = y
        a = self.x + self.y
        return a

    def subtract(self, x, y):
        self.x = x
        self.y = y
        a = self.x - self.y
        return a

    def multiply(self, x, y):
        self.x = x
        self.y = y
        a = self.x * self.y
        return a

    def divide(self, x, y):
        self.x = x
        self.y = y

        if (y == 0):
            a = "You can't divide by zero!"
        else:
            a = self.x / self.y
        return a

    def potence(self, x, powP):
        self.x = x
        self.powP = powP
        return pow(x, powP)

    def square(self, number):
        self.number = number
        return round(math.sqrt(number))

    def module(self, x, y):
        self.x = x
        self.y = y
        return x % y


loop = True
while loop == True:
    op = input(
        'Operación a realizar\n1-Suma\n2-Resta\n3-Multiplicacion\n4-Division\n5-Potencia\n6-Raiz\n7-Modulo\n')
    calc = Calculator()
    selected=int(op)
    if selected == 1:
        num_one=int(input('Ingresa primer numero'))
        num_two=int(input('Ingresa segundo numero'))
        result=calc.add(num_one,num_two)
    if selected == 2:
        num_one=int(input('Ingresa primer numero'))
        num_two=int(input('Ingresa segundo numero'))
        result=calc.subtract(num_one,num_two)
    if selected == 3:
        num_one=int(input('Ingresa primer numero'))
        num_two=int(input('Ingresa segundo numero'))
        result=calc.multiply(num_one,num_two)
    if selected == 4:
        num_one=int(input('Ingresa primer numero'))
        num_two=int(input('Ingresa segundo numero'))
        result=calc.divide(num_one,num_two)
    if selected == 5:
        num_one=int(input('Ingresa primer numero'))
        num_two=int(input('Ingresa segundo numero'))
        result=calc.potence(num_one,num_two)
    if selected == 6:
        num_one=int(input('Ingresa primer numero'))
        num_two=int(input('Ingresa segundo numero'))
        result=calc.square(num_one,num_two)
    if selected == 7:
        num_one=int(input('Ingresa primer numero'))
        num_two=int(input('Ingresa segundo numero'))
        result=calc.module(num_one,num_two)
        
    print(result)