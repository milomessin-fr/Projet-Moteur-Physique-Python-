import sys
import sdl2
import sdl2.ext
from entity import Carre 

class MoteurPhysique:
    def __init__(self):
        sdl2.ext.init()

        self.WIDTH, self.HEIGHT = 600, 700
        self.window = sdl2.ext.Window("Moteur Physique NSI", size=(self.WIDTH, self.HEIGHT))
        self.window.show()

        self.renderer = sdl2.ext.SoftwareSpriteRenderSystem(self.window)
        self.factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)

        sprite_carre = self.factory.from_color(sdl2.ext.Color(255, 0, 0), size=(50, 50))
        self.mon_carre = Carre(sprite_carre, x=450, y=100)
        
        

        self.running = True
        self.last_tick = sdl2.SDL_GetTicks()

    def handle_input(self):
        #récupere tous les événements et les traite
        events = sdl2.ext.get_events()
        for event in events:
            self.update(0.03)
            if event.type == sdl2.SDL_QUIT:
                self.running = False

    def update(self, dt):
        """Gestion de la logique et de la physique"""
        self.mon_carre.update(dt)
        
        #collison avec bord 
        if self.mon_carre.x < 0 or self.mon_carre.x + 50 > self.WIDTH:
            self.mon_carre.vx *= -1 
            
        if self.mon_carre.y < 0 or self.mon_carre.y + 50 > self.HEIGHT:
            self.mon_carre.vy *= -1 

    def render(self):
        """Gestion de l'affichage"""
        sdl2.ext.fill(self.renderer.surface, sdl2.ext.Color(33, 37, 41)) # sombre trés pro et cool
        
        self.renderer.render(self.mon_carre.sprite)
        self.window.refresh()
        
    def run(self):
        #Lance la boucle principale du moteur 
        while self.running:
            now = sdl2.SDL_GetTicks()
            dt = (now - self.last_tick) / 1000.0  
            self.last_tick = now

            self.handle_input()
            self.update(dt)
            self.render()
        sdl2.ext.quit()

if __name__ == "__main__":
    engine = MoteurPhysique()
    engine.run()