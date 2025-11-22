class IConvert:
    def convert(self, word):
        pass

class Upper(IConvert):
    def convert(self, word):
        return word.upper()
    
class Lower(IConvert):
    def convert(self, word):
        return word.lower()
    
class OneUpper(IConvert):
    def convert(self, word):
        return word.capitalize()
    
class Strategy():
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy =     strategy
    
    def newWord(self, word):
        return self.strategy.convert(word)

obj = Strategy(OneUpper())

print(obj.newWord("HOLA MUNDO !!!"))

obj.set_strategy(Upper())

print(obj.newWord("wasaaaaaaaaa!!!!"))

