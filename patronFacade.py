class Suma:
    def sumar(self,a,b):
        return a + b

class Resta:
    def restar(self,a,b):
        return a - b
class Multiplicar:
    def multiplicar(self,a,b):
        return a*b

class Facade:
    def __init__(self):
        self.suma = Suma()
        self.resta = Resta()
        self.multiplicar = Multiplicar()

    def union(self,a,b):
        return{
        "s": self.suma.sumar(a,b),
       "r" : self.resta.restar(a,b),
        "m": self.multiplicar.multiplicar(a,b)
        }

obj = Facade()

print(obj.union(1,2))