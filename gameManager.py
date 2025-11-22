class GameManager:
    _instancia = None
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._life = 10
            cls._instancia._level = 1 
            cls._instancia._points = 0
        return cls._instancia
    
    def lifeManager(self, newLife):
        self._life = newLife
    def levelManager(self, newLevel):
        self._level = newLevel
    def pointManager(self, newPoint):
        self._points = newPoint

obj = GameManager()

print("Hurt")
obj.lifeManager(obj._life-1)
print(obj._life)
print("Upgrade!!")
obj.levelManager(obj._level+1)
print(obj._level)
print("Enemy kill")
obj.pointManager(obj._points+10)
print(obj._points)