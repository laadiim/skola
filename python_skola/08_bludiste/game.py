from world import World
from gameobject import GameObject
from vector2 import Vector2
from gui import Gui


class Game:
    '''
    Trida reprezentujici hru

    @Author: cakoral
    @Date: 01.12.2023
    '''
    def __init__(self, world, hero, home):
        '''
        Konstruktor tridy Game

        Args:
            world: svet hry
            hero: hrdina
            home: cil
        '''
        self.world = world
        self.hero = hero
        self.home = home
        self.symbols = [world.symbols[0], world.symbols[1], hero.symbol, home.symbol]
    
    def run(self):
        '''
        Spusti hru

        Retruns:
            bool
        '''
        reached = False

        while True:
            gui = Gui(self.world.width, self.world.height)
            self.world.draw(gui)
            self.hero.draw(gui)
            self.home.draw(gui)
            gui.show()

            dir = gui.input_direction()
            new_pos = self.hero.position + dir

            if self.world.is_empty(new_pos):
                self.hero.move(dir)

                if self.hero.position == self.home.position:
                    reached = True
                    break
            elif self.world.val(new_pos):
                self.hero.move(dir)
                self.world.draw(gui)
                self.hero.draw(gui)
                self.home.draw(gui)
                gui.show()
                break
            
        return reached            

                
            


if __name__ == "__main__":
    world = World([[1,1,1,1,1,1],[1,0,0,1,0,1],[1,0,0,1,0,1],[1,0,0,0,0,1],[1,1,1,1,1,1]],[' ','#'])
    hero = GameObject(Vector2(1,1),"@")
    home = GameObject(Vector2(4,1),"^")

    destination = Game(world,hero,home).run()
    if destination: 
        print("Vitej doma!")
    else:
        print("... a uz ho nikdy nikdo nevidel... ")