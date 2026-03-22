
 # Bibliothèque pysdl
import sdl2 
import sdl2.ext 
from sdl2 import SDL_KEYDOWN, SDLK_SPACE
import sdl2.sdlttf as ttf

 # divers import
import random
import time
import threading

# import de fichiers
from ..config import config_window as config
from .debug import DebugMenu
from ..scene import SceneBase
from ..core.collision import Collision 








class MoteurRendu:
    def __init__(self):
        """"Récupération des valeurs"""
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.FPS = config.FPS
        self.mode_debug = DebugMenu()
        self.collision = Collision() #mettre en parametre une table des entity non static
        
        #setup de la fenetre 
        self.set_window()


    def set_window(self):
        """Initialisation de la fenêtre"""
        sdl2.ext.init()
        self.window = sdl2.ext.Window("Moteur Physique NSI", size=(self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.window.show()
        
        self.renderer = config.renderer = sdl2.ext.Renderer(self.window)
        self.factory = config.FACTORY = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=self.renderer) 
        self.last_time = sdl2.SDL_GetTicks()
        ttf.TTF_Init()

        #initialisation de toutes les scenes
        self.scene_base = SceneBase(renderer=self.renderer, factory=self.factory)

        #lancement de la boucle
        self.run()
    


    def fixed_timestep(self):
        """mise à jour à intervalles de temps fixes et constants"""
        self.dt = 1.0 / self.FPS
        accumulator = 0

        current_time = sdl2.SDL_GetTicks() / 1000
        frame_time = current_time - self.last_time
        self.last_time = current_time

        accumulator += frame_time

        while accumulator >= self.dt:
            accumulator -= self.dt





    def event(self):
        """gère les events"""
        events = sdl2.ext.get_events()
        for event in events:

            if event.type == sdl2.SDL_QUIT: #ferme l'application
                self.running = False
            
            if event.type == SDL_KEYDOWN:
                if event.key.keysym.sym == SDLK_SPACE :
                    self.mode_debug.menu()
                    
               
                    

    def render_scene(self, scene="base"):
        """initialise une scene"""
        if scene == "base":
            self.scene_base.construire()
        pass

    


    def run(self):
        """Boucle de l'application"""

        self.running = True
        self.collision.start()

        while self.running:

            self.event()

            self.fixed_timestep()
            with self.collision.verrou:
                self.render_scene()


        self.collision.stop()
        sdl2.ext.quit()








if __name__ == "__main__":
    moteur_rendu = MoteurRendu()
    