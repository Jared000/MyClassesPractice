class Potenciador:
    def elevar(self, base, exponente):
        print("Calculando potencia...")
        return base ** exponente 
    
class PotenciadorProxy:
    def __init__(self):
        self._potenciador = Potenciador()
        self.di = {}

    def elevar(self, base, exponente):
        clave = (base, exponente)
        if clave in self.di:
            print("Usando cache")
            return self.di[clave]
        result = self._potenciador.elevar(base, exponente)
        self.di[clave] = result
        return result

obj = PotenciadorProxy()
print(obj.elevar(2,1))
print(obj.elevar(2,1))
print(obj.elevar(2,9))