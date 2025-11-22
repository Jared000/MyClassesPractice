from abc import ABC , abstractmethod

class Boton(ABC):
    @abstractmethod
    def mostrar(self):
        pass

class Ventana(ABC):
    @abstractmethod
    def mostrar(self):
        pass

class BotonClaro(Boton):
    def mostrar(self):
        return "Claro"
    
class BotonOscuro(Boton):
    def mostrar(self):
        return "Oscuro"
    
class VentanClara(Ventana):
    def mostrar(self):
        return "Ventana Clara"
class VentanaOscura(Ventana):
    def mostrar(self):
        return "Ventana Oscura"
    
#AbstractFatory

class GUIFactory(ABC):
    @abstractmethod
    def crearBoton(self) -> Boton:
        pass
    def crearVentana(self) -> Ventana:
        pass


class FabricaTemaClaro(GUIFactory):
    def crearBoton(self):
        return BotonClaro()
    def crearVentana(self):
        return VentanClara()
    
class FabricaTemaOscuro(GUIFactory):
    def crearBoton(self):
        return BotonClaro()
    def crearVentana(self):
        return VentanaOscura()
    
def crearInterfaz(fabrica: GUIFactory):
    boton = fabrica.crearBoton()
    ventana = fabrica.crearVentana()

    print(boton.mostrar())
    print(ventana.mostrar())

print("Interfaz tema claro: ")
crearInterfaz(FabricaTemaClaro())
print("Interfaz tema oscuro")
crearInterfaz(FabricaTemaOscuro())