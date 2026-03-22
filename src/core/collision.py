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
        self.thread = threading.Thread(target=self.test)

        

    def test(self): # A supprimer car générer par l'ia pour test le systeme d'entity
        return
        last_ticks = sdl2.SDL_GetTicks()
        
        while self.running:
            current_ticks = sdl2.SDL_GetTicks()
            local_dt = (current_ticks - last_ticks) / 1000.0
            last_ticks = current_ticks

            if local_dt > 0.1: local_dt = 0.1

            with self.verrou:
                # 1. Mise à jour des positions (Gravité + Vitesse)
                for el in config.ENTITY:
                    el.v_y += config.GRAVITE * local_dt
                    el.y += el.v_y * local_dt
                    # Note : On ne met à jour le sprite qu'à la toute fin du calcul

                # 2. Détection et Réponse aux collisions (Double boucle)
                # On compare chaque entité avec toutes les autres
                for i in range(len(config.ENTITY)):
                    for j in range(i + 1, len(config.ENTITY)):
                        entite_a = config.ENTITY[i]
                        entite_b = config.ENTITY[j]

                        # Vérification de collision simple (AABB)
                        # On suppose que tes entités ont des attributs .x, .y, .w, .h
                        if (entite_a.x < entite_b.x + entite_b.w and
                            entite_a.x + entite_a.w > entite_b.x and
                            entite_a.y < entite_b.y + entite_b.h and
                            entite_a.y + entite_a.h > entite_b.y):
                            
                            # RÉPONSE : Rebond vertical simple (on inverse v_y)
                            # On ajoute un coefficient de restitution (0.8 = perd un peu d'énergie)
                            entite_a.v_y, entite_b.v_y = -entite_a.v_y * 0.8, -entite_b.v_y * 0.8
                            
                            # ANTI-CHEVAUCHEMENT : Pour éviter que les objets restent collés
                            # On les décolle légèrement selon l'axe Y
                            if entite_a.y < entite_b.y:
                                entite_a.y -= 1
                                entite_b.y += 1
                            else:
                                entite_a.y += 1
                                entite_b.y -= 1

                # 3. Mise à jour finale des sprites pour le thread de rendu
                for el in config.ENTITY:
                    el.sprite.y = int(el.y)
                    el.sprite.x = int(el.x)

            # 4. Très important pour ne pas figer l'ordinateur
            sdl2.SDL_Delay(1)




    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.test, daemon=True)  
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join() 
