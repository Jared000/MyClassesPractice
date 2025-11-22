class Messenger:
    def update(self, text):
        pass

class Normal(Messenger):
    def update(self, text):
        print(text)
    
class Archive(Messenger):
    def update(self, text):
        try:
            with open('StrategyMessengerSimple.txt', 'w', encoding='utf-8') as archive:
                archive.write(text)
        except ImportError as e:
            print(f'Error al escribir en el archivo {e}')
    
class Upper(Messenger):
    def update(self, text):
        try:
            with open('StrategyMessengerSimple.txt', 'w', encoding='utf-8') as archive:
                archive.write(text.capitalize())
            print('Exito')
        except ImportError as e:
            print(f'Error al escribir en el archivo {e}')

class PrintText():
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def show(self, text):
        self.strategy.update(text)

obj = PrintText(Normal())
obj.show("hola mundo")
obj.set_strategy(Archive())
obj.show('hola mundo')
obj.set_strategy(Upper())
obj.show("hola mundo")

        