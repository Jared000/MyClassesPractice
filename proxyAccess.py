class Archivo:
    def leer(self):
        return "Contenido super secreto"
    
class ProxyArchivoSecreto:
    def __init__(self, rol):
        self.rol = rol
        self._archivo = Archivo()


    def leerP(self):
        if self.rol == "admin":
            return self._archivo.leer()
        else:
            print("Accesso denegado")

admin = ProxyArchivoSecreto("admin")

print(admin.leerP())