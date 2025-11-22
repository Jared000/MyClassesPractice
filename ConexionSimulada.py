class Conexion:
    _instancia = None
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._conexionStatue = False
        return cls._instancia
    
    def activeConexion(self, newConexionStatue):
        self._conexionStatue = newConexionStatue
        print("Ejecutando: SELECT * FROM users")

obj = Conexion()

obj.activeConexion(True)
print(obj._conexionStatue)