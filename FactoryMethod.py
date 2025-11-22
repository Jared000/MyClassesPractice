from abc import ABC, abstractmethod

class abrastactClass(ABC):
    @abstractmethod
    def herencyMethod(self):
       pass
    

class claseNormal(abrastactClass):
    def herencyMethod(self):
        return 2 +2
    
class claseNormalDos(abrastactClass):
    def herencyMethod(self):
        return 2+3
    

#Factory Method

class FactoryClass(ABC):
    @abstractmethod
    def factoryMethod(self):
        pass

class CreatorOne(FactoryClass):
    def factoryMethod(self):
        return claseNormal()
    
class CreatorTwo(FactoryClass):
    def factoryMethod(self):
        return claseNormalDos()
    

creatorNormal = CreatorOne()
creatorNormalDos = CreatorTwo()

obj1 = creatorNormal.factoryMethod()
obj2 = creatorNormalDos.factoryMethod()

print(obj1.herencyMethod())
print(obj2.herencyMethod())


    
