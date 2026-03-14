import sdl2
import sdl2.ext
import time
from entity import Carre
from sdl2 import SDL_KEYDOWN, SDLK_SPACE
import code



class MoteurPhysique:
    def __init__(self):
        """"Initialisation du moteur physique et de la fenêtre"""
        sdl2.ext.init()
        self.window = sdl2.ext.Window("Moteur Physique NSI", size=(600, 700))
        self.window.show()

        self.renderer = sdl2.ext.Renderer(self.window)
        self.factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=self.renderer)  
        self.last_time = sdl2.SDL_GetTicks()

        # Initialisation du carré
        self.CUBE_X = 20
        self.CUBE_Y = 300
        sprite_carre = self.factory.from_color(sdl2.ext.Color(255, 0, 0), size=(self.CUBE_X, self.CUBE_Y))
        self.mon_carre = Carre(sprite_carre, x=100, y=100)
        
        # Définition des limites du monde
        self.WORLD_X = 40
        self.WORLD_Y = 40
        self.WORLD_WIDTH = 520
        self.WORLD_HEIGHT = 620

        # Framerate
        self.FPS = 60

    
    def construire(self):
        """Construction de la scène"""
        

        raw_r = self.renderer.sdlrenderer

        
        # 1. Fond
        sdl2.render.SDL_SetRenderDrawColor(raw_r, 0, 0, 0, 255)
        sdl2.render.SDL_RenderClear(raw_r)
        
        # 2. Bordure 
        container_rect = sdl2.SDL_Rect(self.WORLD_X, self.WORLD_Y, self.WORLD_WIDTH, self.WORLD_HEIGHT)
        sdl2.render.SDL_SetRenderDrawColor(raw_r, 0, 255, 0, 255) 
        sdl2.render.SDL_RenderDrawRect(raw_r, container_rect)

        # 3. Carré
        dst_rect = sdl2.SDL_Rect(int(self.mon_carre.x), int(self.mon_carre.y), self.CUBE_X, self.CUBE_Y)
        sdl2.render.SDL_RenderCopy(raw_r, self.mon_carre.sprite.texture, None, dst_rect)

        # 4. Affichage
        sdl2.render.SDL_RenderPresent(raw_r)
        
        return 1




    def handle_input(self):
        """Gestion des entrées utilisateur"""
        events = sdl2.ext.get_events()
        for event in events:
           if event.type == SDL_KEYDOWN:
            # Mode débug : permet d'exécuter du code Python en temps réel
                if event.key.keysym.sym == SDLK_SPACE :
                    while True:
                        input_debug = input("Commande debug >")
                        if input_debug == "help":
                            print("Commandes disponibles :")
                            print("- dir(objet) : Permet d'accéder aux méthodes et attributs d'un objet")
                            print("- vars(objet) : Affiche les valeurs d'un objet")
                            print("- python code : Permet d'exécuter du code Python en temps réel")
                            print("- exit : Quitte le mode debug")
                        if input_debug == "exit":
                            break
                        try:
                            exec(input_debug)
                        except Exception as e:
                            print(f"Erreur : {e}")

    

    
    def colision(self, dt):
        limite_sol = self.WORLD_Y + self.WORLD_HEIGHT - self.CUBE_Y -1
        limite_plafond = self.WORLD_Y + 1
        seuil = self.mon_carre.GRAVITE * dt 
        prochaine_y = self.mon_carre.y + (self.mon_carre.v_y * dt)

        #print(f"limite_sol: {limite_sol}, prochaine_y: {prochaine_y}, seuil: {seuil}")

        if prochaine_y <= limite_plafond:
            self.mon_carre.v_y *= -0.6
            

        if prochaine_y >= limite_sol:
            self.mon_carre.y = limite_sol 
            
            if abs(self.mon_carre.v_y) < seuil:
                self.mon_carre.v_y = 0
                self.mon_carre.y = limite_sol  
                self.mon_carre.on_ground = True
            else:
                self.mon_carre.v_y *= -0.6
                self.mon_carre.on_ground = False  
        else:
            self.mon_carre.on_ground = False

        if (self.mon_carre.x < self.WORLD_X or
            self.mon_carre.x + self.CUBE_X > self.WORLD_X + self.WORLD_WIDTH):
            self.mon_carre.v_x *= -1

        self.mon_carre.update_movement(dt)
        return 1
        
    


    def run_app(self):
        """Lance la boucle principale du moteur """
        running = True

        while running:
            events = sdl2.ext.get_events()
            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    break

            current_time = sdl2.SDL_GetTicks()
            frame_time = current_time - self.last_time

            if frame_time < (1000 // self.FPS):
                sdl2.SDL_Delay((1000 // self.FPS) - frame_time)

            self.last_time = sdl2.SDL_GetTicks()
            dt = 1.0 / self.FPS  # dt fixe et stable = 0.016 

            self.handle_input()
            self.construire()
            self.colision(dt)
            

        sdl2.ext.quit()
        return 1













if __name__ == "__main__":
    moteur = MoteurPhysique()
    moteur.run_app()