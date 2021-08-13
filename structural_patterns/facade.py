"""
Used to add an interface or control panel for complex subsytem

like operating systems they have too many sub systems and classes
but what user really want is a simple interface to deal with that have all functionality he needs

for example let's look at a game 
the game have many subsystems like main charachter system or the map sytem and so on ...

to start the game each system has to load and then maybe some operation to begin with
"""

class Map:
    def load(self):
        print("Map loaded")
    
    def mission(self):
        print("Mission for This map is to defeat Master")

class MainCharacter:
    def load(self):
        print("Main character loaded")

    def respawn(self):
        print("Main character respawned")
    
class GameFacade:

    def __init__(self, map, maincharacter) -> None:
        self.map = map()
        self.m_c = maincharacter()
    
    def start(self):
        self.map.load()
        self.m_c.load()
        print("game loaded")
        
    def play(self):
        self.m_c.respawn()
        self.map.mission()
    
if __name__ == '__main__':
    g = GameFacade(Map, MainCharacter)
    g.start()
    g.play()