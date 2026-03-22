class Entity:
    def __init__(self,x ,y, sprite, static=False): 
        self.x = x
        self.y = y
        self.sprite = sprite
        self.sprite.owner = self
        self.sprite.position = self.x, self.y

        if static == True:
            pass

        elif static == False:
            self.v_x = 0
            self.v_y = 200

       


    def retourner_position(self):
        """Retourne la position du carré"""
        return self.x, self.y