from abc import ABC, abstractmethod

class contadorglobal:
    _instancia = None
    count = 0
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia   
    
   # @abstractmethod
    def incrementar(cls):
        cls.count = cls.count +1 
    

obj = contadorglobal()

obj.incrementar()
obj.incrementar()
obj.incrementar()
print(obj.count)