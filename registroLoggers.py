from pathlib import Path

class Logger:
    _instancia = None
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._write = Path("app.log")
        return cls._instancia
    
    def write(self, _writeArchive):
        with self._write.open("a") as f:
            f.write(_writeArchive + " \n")
        print(f"[LOG] {_writeArchive}")

write = Logger()
write2 = Logger()

write.write("Init")
write2.write("Enter")
        
