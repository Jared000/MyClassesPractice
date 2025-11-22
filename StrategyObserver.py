class WeatherStation:
    def __init__(self):
        self.observers = []
    
    def attach(self, observer):
        self.observers.append(observer)

    def  notify(self, message):
        for obs in self.observers:
            obs.update(message)

class Observer():
    def update(self, message):
        print(message)

#Mas tarde