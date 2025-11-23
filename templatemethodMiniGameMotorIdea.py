class GameEngine:
    def run(self):
        load_asstes = self.load_assets()
        init = self.init()
        game_loop = self.game_loop()
        shutdown = self.shutdown()

    def shutdown(self):
        print('Fin de la ejecucion')
    def load_assets(self):
        pass
    def init(self):
        pass
    def game_loop(self):
        pass
    def update(self):
            pass
    def render(self):
            pass


class SpaceGame(GameEngine):
    def load_assets(self):
        print('cargando naves y planetas')
    
    def game_loop(self):
        for i in range(1):
             self.update()
             self.render()

    def update(self):
        print("Dead Space is here")
    
    def render(self):
        print('Drepare to die')    

class ZombieGame(GameEngine):
    def load_assets(self):
        print('cargando zombies y armas')
    
    def game_loop(self):
        for i in range(1):
             self.update()
             self.render()
    def update(self):
        print("leeeeeoooon")

    def render(self):
        print('resident evil 7')

spaceG = SpaceGame()

spaceG.run()

zombie = ZombieGame()

zombie.run()