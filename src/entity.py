import sdl2.ext

class Carre:
    def __init__(self, sprite, x=0, y=0):
        self.sprite = sprite
        self.sprite.position = x, y
        self.sprite.owner = self
        self.x = x
        self.y = y
        self.vx = 100 
        self.vy = 100 

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        
        self.sprite.x = int(self.x)
        self.sprite.y = int(self.y)


from sdl2 import sdlgfx

class Cercle:
    def __init__(self, x, y, rayon, couleur):
        self.x = x
        self.y = y
        self.vx = 150 # pixels/s
        self.vy = 150
        self.rayon = rayon
        self.couleur = couleur # ex: (0, 255, 255, 255) -> R, G, B, A

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def draw(self, renderer_ptr):
        # renderer_ptr est maintenant un LP_SDL_Renderer, exactement ce qu'il veut !
        sdlgfx.filledCircleRGBA(
            renderer_ptr, 
            int(self.x), int(self.y), 
            int(self.rayon), 
            self.couleur[0], self.couleur[1], self.couleur[2], self.couleur[3]
        )