import sdl2.ext

class Carre:
    def __init__(self, sprite, x=0, y=0):
        self.sprite = sprite
        self.sprite.position = x, y
        self.sprite.owner = self
        self.x = x
        self.y = y
        self.v_x = 300 
        self.v_y = 300 

    def update_movement(self, dt):   
        """Met à jour la position du carré en fonction de sa vitesse et du temps écoulé"""
        self.x += self.v_x * dt
        self.y += self.v_y * dt

        self.sprite.x = int(self.x)
        self.sprite.y = int(self.y)


