class SumaReal:
    def suma(self, a,b):    
        return a + b
    
class SumaProxy:
    def __init__(self):
        self._sumaReal = SumaReal()
    def sumaP(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return self._sumaReal.suma(a ,b)
        else:
            print("Only digits")

obj = SumaProxy()

print(obj.sumaP(1, 2))