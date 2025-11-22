class Subject():
    def __init__(self):
        self.observers = []
        self.state = False
    
    def attach(self,observer): 
        self.observers.append(observer)

    def notify(self, message):
        for obj in self.observers:
            obj.update(message)
        

    def set_state(self):
        if self.state is False:
            self.state = True
            self.notify(self.state)
        else:
            self.state = False
            self.notify(self.state)

class Observer():
    def update(self, message):
        print("Hola", message)

obs= Observer()

sub = Subject()

sub.attach(obs)
#sub.attach(obs)

sub.notify("Mundo")

sub.set_state()
sub.set_state()