class Entity:
    def __init__(self, x, y, sprite, static=False):
        self._x = float(x)
        self._y = float(y)
        self._v_x = 0.0 if static else 200.0
        self._v_y = 0.0 if static else 200.0
        self.sprite = sprite
        self.static = static
        
        self.sprite.x = int(self._x)
        self.sprite.y = int(self._y)
        
        self.w = float(self.sprite.size[0])
        self.h = float(self.sprite.size[1])
       

    # --- Propriétés pour X ---
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not self.static:
            self._x = value
            self.sprite.x = int(self._x)

    # --- Propriétés pour Y ---
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not self.static:
            self._y = value
            self.sprite.y = int(self._y)
            
    # --- Propriétés pour V_Y ---
    @property
    def v_y(self):
        return 0.0 if self.static else self._v_y

    @v_y.setter
    def v_y(self, value):
        if not self.static:
            self._v_y = value

     # --- Propriétés pour V_X ---
    @property
    def v_x(self):
        return 0.0 if self.static else self._v_x

    @v_x.setter
    def v_x(self, value):
        if not self.static:
            self._v_x = value