class Fraccion:
    __numerador = None
    __denominador = None
    def __init__(self, numerador, denominador = 1):
        self.__numerador = numerador
        self.__denominador = denominador
    def __str__(self):
        return '{}/{}'.format(self.__numerador, self.__denominador)
    def __add__(self, other):
        denominador = self.__denominador * other.getDen()
        numerador = (self.__numerador * other.getDen()) + (other.getNum() * self.__denominador)
        #resultado = '{}/{}'.format(numerador, denominador)
        self.__numerador = numerador
        self.__denominador = denominador
        return self
    def __sub__(self, other):
        denominador = self.__denominador * other.getDen()
        numerador = (self.__numerador * other.getDen()) - (other.getNum() * self.__denominador)
        #resultado = '{}/{}'.format(numerador, denominador)
        self.__numerador = numerador
        self.__denominador = denominador
        return self
    def __mul__(self, other):
        numerador = self.__numerador * other.getNum()
        denominador = self.__denominador * other.getDen()
        #resultado = '{}/{}'.format(numerador, denominador)
        self.__numerador = numerador
        self.__denominador = denominador
        return self
    def __mod__(self, other): #LA SOBRECARGA DEL __div__ NO FUNCIONABA
        numerador = self.__numerador * other.getDen()
        denominador = self.__denominador * other.getNum()
        #resultado = '{}/{}'.format(numerador, denominador)
        self.__numerador = numerador
        self.__denominador = denominador
        return self
    def getNum(self):
        return self.__numerador
    def getDen(self):
        return self.__denominador
    #SIMPLICAR UNA FRACCIÓN v0.3
    def mcd(self):
        a = self.__numerador
        b = self.__denominador
        maximo = 1
        if(b == 0):
            maximo = a
        while b != 0:
            x = a%b
            a = b
            b = x
        maximo = a
        return maximo
    def simplificar(self):
        mcd = self.mcd()
        self.__numerador //= mcd
        self.__denominador //= mcd
        return '{}/{}'.format(self.__numerador, self.__denominador)