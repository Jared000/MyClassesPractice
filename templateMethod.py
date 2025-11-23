from abc import ABC, abstractmethod

class LoginProcess(ABC):
    def login(self):
        user = self.userRequest()
        password = self.passwordRequest()
        valid= self.validar(user, password)
        show = self.mostrar_resultado(valid)
        
    @abstractmethod
    def userRequest(self):
        pass
    @abstractmethod
    def passwordRequest(self):
        pass
    @abstractmethod
    def validar(self, name, password):
        pass

    def mostrar_resultado(self, valid):
        if valid:
            print("Login Exitoso")
        else:
            print("Login Fallido")

class LoginAdmin(LoginProcess):
    def __init__(self):
        self.admin = 'root'
        self.password = '1234'

    def userRequest(self):
        return input("Admin user: ")

    def passwordRequest(self):
        return input("Admin password: ")
    
    def validar(self, name, password):
        return name == self.admin and password == self.password

class LoginUser(LoginProcess):
    def __init__(self):
        self.user = 'Gary'
        self.password = '2345'

    def userRequest(self):
        return input("User: ")
    
    def passwordRequest(self):
        return input("User Password: ")
    
    def validar(self, name, password):
        return name == self.user and password == self.password

login = LoginAdmin()
login.login()

login2 = LoginUser()
login.login()