import sdl2.ext

class Carre:
    def __init__(self, sprite, x=0.0, y=0.0):
        self.sprite = sprite
        self.sprite.position = x, y
        self.sprite.owner = self
        self.x = x
        self.y = y
        self.v_x = 70
        self.v_y = 2000
        self.GRAVITE = 800
        self.on_ground = False 


    def retourner_position(self):
        """Retourne la position du carré"""
        return self.x, self.y


    def calcul_gravite(self, dt):
        """calcul de la gravité"""
        pass

        
    def update_movement(self, dt):   
        """Met à jour la position du carré en fonction de sa vitesse et du temps écoulé"""
        self.x += self.v_x * dt

        if not self.on_ground:
            self.v_y += self.GRAVITE * dt

        self.y += self.v_y * dt
        #print(f"v_y={self.v_y:.2f} | y={self.y:.2f} | on_ground={self.on_ground}")
        self.sprite.x = round(self.x)
        self.sprite.y = round(self.y)

