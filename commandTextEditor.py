from abc import ABC, abstractmethod

class ReceiverWrite:
    def action(self,text):
        with open('commandTextEditor.txt', 'a') as f:
            f.write(text)
class ReceiverDelete:
    def action(self, num_chars):
        num_chars = int(num_chars)

        # Leer el contenido actual
        with open('commandTextEditor.txt', 'r') as f:
            content = f.read()

        # Borrar N caracteres
        new_content = content[:-num_chars] if num_chars <= len(content) else ""

        # Reescribir el archivo
        with open('commandTextEditor.txt', 'w') as f:
            f.write(new_content)
class Command():
    @abstractmethod
    def execute(self):
        pass

class WriteCommand(Command):
    def __init__(self, receiver, line):
        self.receiver = receiver
        self.line = line
    def execute(self):
        self.receiver.action(self.line)
class DeleteCommand(Command):
    def __init__(self, receiver, line):
        self.receiver = receiver
        self.line = line
    def execute(self):
        self.receiver.action(self.line)

class Invoker():
    def __init__(self):
        self.commands = []
        #

    def add(self,command):
        self.commands.append(command)

    def run(self):
        for command in self.commands:
            command.execute()

write_receiver = ReceiverWrite()
delete_receiver = ReceiverDelete()

invoker = Invoker()

# Escribir algo
cmd_write = WriteCommand(write_receiver, "Hola mundo")
invoker.add(cmd_write)

# Borrar los últimos 5 caracteres
cmd_delete = DeleteCommand(delete_receiver, 5)
invoker.add(cmd_delete)

invoker.run()
