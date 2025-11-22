class Subject():
    def __init__(self):
        self.observers = []
    def attach(self, observer): 
        self.observers.append(observer)

    def notify(self, message):
        for obj in self.observers:
            obj.update(message)
            obj.saveList(self.observers)
            obj.validation(len(self.observers))
    

class Observer():
    def update(self, message):
        print("Hola", message)

    def saveList(self, list):
        save = list.copy
        print(save)

    def validation(self, value):
        if value > 3:
            print("Alert!!!")

obs = Observer()

sub = Subject()

sub.attach(obs)
sub.attach(obs)
sub.attach(obs)

sub.notify("mundo")
