"""Tiene 4 componentes
Command (interfaz base)
Clase abstracta con el método execute().

ConcreteCommand (comandos concretos)
Implementan execute() y llaman al receptor.

Receiver (receptor)
El que hace el trabajo real.

Invoker (invocador)
El que ejecuta los comandos sin saber cómo funcionan."""

class Command:
    def execute(self):
        pass

class ConcreteCommand(Command):
    def execute(self):
        print("Hola mundo")

class Invoker:
    def __init__(self):
        self.commands = []
    
    def add(self, comand):
        self.commands.append(comand)

    def run(self):
        for comand in self.commands:
            comand.execute()


objCon = ConcreteCommand()

invoker = Invoker()

invoker.add(objCon)

invoker.run()

