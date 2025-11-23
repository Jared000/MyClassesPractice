from abc import ABC, abstractmethod

class ReceiverStart:
    def action(self):
         print("Start")

class ReceiverStop:
    def action(self):
        print('Stop')

class ReceiverReset:
    def action(self):
        print('Reset')

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class ConcreteCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver
    def execute(self):
        self.receiver.action()

class Invoker():
    def __init__(self):
        self.commands = []
    
    def add(self, command):
        self.commands.append(command)

    def run(self):
        for command in self.commands:
           command.execute()


start = ReceiverStart()
conCommand = ConcreteCommand(start)
invoker = Invoker()

invoker.add(conCommand)

invoker.run()


