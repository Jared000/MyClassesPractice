class Subject:
    def __init__(self):
        self.observers = []

    def attach(self,observer):
        self.observers.append(observer)

    def notify(self,message):
        for obs in self.observers:
            obs.update(message)
    
class Observer():
    def update(self, message):
        print("hola", message)

objectObserver = Observer()
objectObserver2 = Observer()

objSubject= Subject()

objSubject.attach(objectObserver)
objSubject.attach(objectObserver2)

objSubject.notify("world")