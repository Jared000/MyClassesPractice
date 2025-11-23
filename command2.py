from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, a,b ):
        pass
class AddCommand(Command):
    def execute(self ,a , b):
        return a+b
class SubCommando(Command):
    def execute(self,a , b):
        return a-b
class MulCommand(Command):
    def execute(self,a , b):
        return a*b
    
class Invoker:
    def __init__(self):
        self.commands= []

    def add(self,comand):
        self.commands.append(comand)
    
    def run(self,a ,b):
        for command in self.commands:
            print(command.execute(a,b))

add = AddCommand()
sub = SubCommando()
mul = MulCommand()

invoker = Invoker()

invoker.add(add)
invoker.add(sub)
invoker.add(mul)
invoker.run(3,2)