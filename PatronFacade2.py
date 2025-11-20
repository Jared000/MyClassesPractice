class ValidadorLetra:
    def validarL(self,a):
        return a.isalpha()

class ValidadorNumeros:
    def validarN(self, a):
        return a.isdigit()
        
class ValidadorLongitud:
    def validarL(self, a):
        return len(a) >= 3
    
class Facade:
    def __init__(self):
        self.validadorLetra = ValidadorLetra()
        self.validadorNumero = ValidadorNumeros()
        self.validadorLongitud = ValidadorLongitud()

    def union(self, a):
        return{
       "L" : self.validadorLetra.validarL(a),
        "N": self.validadorNumero.validarN(a),
        "Lon": self.validadorLongitud.validarL(a)
        }

obj = Facade()

print(obj.union("123"))