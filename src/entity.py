import sdl2.ext

class Carre:
    def __init__(self, sprite, x=0.0, y=0.0):
        self.sprite = sprite
        self.sprite.position = x, y
        self.sprite.owner = self
        self.x = x
        self.y = y
        self.v_x = 0
        self.v_y = 0
        self.GRAVITE = 800 


    def retourner_position(self):
        """Retourne la position du carré"""
        return self.x, self.y


    def calcul_gravite(self, dt):
        """calcul de la gravité"""
        pass

        
    def update_movement(self, dt):   
        """Met à jour la position du carré en fonction de sa vitesse et du temps écoulé"""
        self.x += self.v_x * dt
        self.v_y += self.GRAVITE * dt 
        self.y += self.v_y * dt
        
        self.sprite.x = float(self.x)
        self.sprite.y = float(self.y)


