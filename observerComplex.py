class WeatherStation:
    def __init__(self):
        self.observers = []
    
    def attach(self, observer): 
        self.observers.append(observer)

    def notify(self, temperature):
        for obs in self.observers:
            obs.update(temperature)


class ObserverApp:

    def update(self, temperature):
        if temperature != "18" :
            print("Change !", temperature)
        else:
            print("Normal: ", temperature)
class ObserverDisplay:
    def update(self, temperature):
        if temperature != "12" :
            print("Change !", temperature)
        else:
            print("Normal: ", temperature)
class ObserverLogger:
    def update(self, temperature):
        if temperature != "19" :
            print("Change !", temperature)
        else:
            print("Normal: ", temperature)

app= ObserverApp()
display = ObserverDisplay()
logger = ObserverLogger()

ws = WeatherStation()

ws.attach(app)
ws.attach(display)
ws.attach(logger)

ws.notify("18")