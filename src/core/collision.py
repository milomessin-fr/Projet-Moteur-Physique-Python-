#import divers
import threading
import sdl2
import time

#import de fichiers
from ..config import config_collision as config

class Collision:
    def __init__(self): # mettre entity en paramètre
        self.running = True
        #self.entity = entity
        self.verrou = threading.Lock()
        self.thread = threading.Thread(target=self.colision)

        

    def colision(self): 
        last_ticks = sdl2.SDL_GetTicks()
        
        while self.running:
            current_ticks = sdl2.SDL_GetTicks()
            local_dt = (current_ticks - last_ticks) / 1000.0
            last_ticks = current_ticks

            if local_dt > 0.1: local_dt = 0.1

            with self.verrou:
               return
            
            sdl2.SDL_Delay(1)




    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.colision, daemon=True)  
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join() 
