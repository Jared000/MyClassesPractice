class mensaje:
    def enviar(self, mensaje):
        return "Enviando", mensaje

class MensajeProxy:
    def __init__(self):
        self._mensaje = mensaje()
        self.count = 0

    def enviar(self, mensaje):
        self.count = self.count + 1
        return self._mensaje.enviar(mensaje)
    
    def countM(self):
        return self.count
    
obj = MensajeProxy()
print(obj.enviar("ping"))
print(obj.enviar("ping"))

print(obj.countM())