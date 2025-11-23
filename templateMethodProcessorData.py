from abc import ABC, abstractmethod

class Dataprocess(ABC):
    def process(self):
        load = self.load()
        clean= self.clean()
        transform = self.transform()
        export = self.export()
    @abstractmethod
    def load(self):
        pass
    @abstractmethod
    def clean(self):
        pass
    @abstractmethod
    def transform(self):
        pass
    @abstractmethod
    def export(self):
        pass

class CsvProcessor(Dataprocess):
    def load(self):
        print('cargando CSV')
    def clean(self):
        print('eliminando filas vacías')
    def transform(self):
        print('onvirtiendo a mayúsculas')
    def export(self):
        print('exportando a JSON')
    
class ApiProcessor(Dataprocess):
    def load(self):
        print('consumiendo API')
    def clean(self):
        print('filtrando resultados inválidos')
    def transform(self):
        print('parseando JSON')
    def export(self):
        print('guardando en base de datos')

csv = CsvProcessor()

csv.process()

api = ApiProcessor()

api.process()