class Saludador:
    def saludar(self, nombre):
        print(f"Hola, {nombre}")

class ProxySaludador():
    def __init__(self):
        self.saludarReal = Saludador()
    
    def saludarP(self, nombre):
        if nombre is None:
            print("Nombre invalido")
        else:
            self.saludarReal.saludar(nombre)
    
obj = ProxySaludador()

print(obj.saludarP("Gary"))