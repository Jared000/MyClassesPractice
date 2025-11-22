class Configuracion:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._modo = "oscuro"
            cls._instancia._idioma = "espanol"
        return cls._instancia
    
    def cambiarModo(self, nuevo_modo):
        self._modo = nuevo_modo

    def cambiarIdioma(self, nuevo_idioma):
        self._idioma = nuevo_idioma
    


    
obj = Configuracion()
obj2 = Configuracion()

print(obj.cambiarIdioma("ingles"))
#print(obj.cambiarModo("claro"))

print(obj._modo)